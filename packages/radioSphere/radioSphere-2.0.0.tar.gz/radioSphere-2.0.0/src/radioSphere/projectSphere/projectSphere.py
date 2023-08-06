import numpy
import scipy.ndimage


def _disk(radius):
    y, x = numpy.ogrid[-radius : radius + 1, -radius : radius + 1]
    mask = x * x + y * y <= radius * radius
    return mask / mask.sum()


def pointToDetectorPixelRange(posMM, sourceDetectorDistMM=100, pixelSizeMM=0.1, detectorResolution=[512, 512]):
    """
    This function gives the detector pixel that a single point will affect.
    The main idea is that it will be used with `ROIaroundSphere` option for projectSphereMM() and
    in turn singleSphereToDetectorPixelRange() in order to only project the needed pixels.

    Parameters
    ----------
        posMM : 1x3 2D numpy array of floats
            xyz position of sphere in mm, with the origin being the middle of the detector

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector
            Set as numpy.inf for parallel projection
            Default = 100

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        detectorResolution : 2-component list of ints, optional
            Number of pixels rows, columns of detector
            Default = [512,512]

    Returns
    -------
        detectorPixel : tuple
            row, column (j,i) coordinate on detector as per figures/projectedCoords_v2.pdf
    """
    assert len(posMM.ravel()) == 3

    posMM = posMM.ravel()

    if sourceDetectorDistMM == numpy.inf:
        projectedPixelSize = 1.0
    else:
        zoomLevel = sourceDetectorDistMM / posMM[0]
        projectedPixelSize = pixelSizeMM / zoomLevel

    # This is the pixel position wrt to the middle of the detector
    YpositionProjectedPX = posMM[1] / projectedPixelSize
    ZpositionProjectedPX = posMM[2] / projectedPixelSize

    # Detector is rows, columns, so Z, Y
    detectorPX = numpy.array(detectorResolution) // 2 - [
        ZpositionProjectedPX,
        YpositionProjectedPX,
    ]

    return numpy.round(detectorPX).astype(int)


def singleSphereToDetectorPixelRange(
    spherePositionMM,
    radiusMM,
    radiusMargin=0.1,
    sourceDetectorDistMM=100,
    pixelSizeMM=0.1,
    detectorResolution=[512, 512],
    transformationCentreMM=None,
    transformationMatrix=None,
):
    """
    This function gives the detector pixel range that a single sphere will affect.
    The main idea is that it will be used with `ROIaroundSphere` option for projectSphereMM()
    in order to only project the needed pixels.

    Parameters
    ----------
        spherePositionMM : 1x3 2D numpy array of floats
            xyz position of sphere in mm, with the origin being the middle of the detector

        radiusMM : float
            Particle radius for projection

        radiusMargin : float
            Multiplicative margin on radius
            Default = 0.1

        ROIaroundSphere : bool, optional
            If there is only one sphere, only compute a region-of-interest radiography?
            Default = False

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector
            Set as numpy.inf for parallel projection
            Default = 100

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        detectorResolution : 2-component list of ints, optional
            Number of pixels rows, columns of detector
            Default = [512,512]

        transformationCentreMM : 3-component vector
            XYZ centre for a transformation
            Default = None

        transformationMatrix : 3x3 numpy array
            XYZ transformation matrix to apply to coordinates
            Default = None

    Returns
    -------
        JIrange : range in rows, colums of detector concerned by this grain
    """
    assert (transformationCentreMM is None) == (
        transformationMatrix is None
    ), """projectSphere.singleSphereToDetectorPixelRange():
     transformationCentreMM and transformationMatrix must both be set or unset"""

    # Transform coordinates if so asked
    if transformationCentreMM is not None:
        spherePositionMM = (
            numpy.dot(
                transformationMatrix,
                numpy.array(spherePositionMM).ravel() - numpy.array(transformationCentreMM).ravel(),
            )
            + transformationCentreMM
        )
        # spherePositionMM = numpy.array([numpy.dot(transformationMatrix,
        #                                 spherePositionMM[0] - transformationCentreMM) + transformationCentreMM])

    x = spherePositionMM.ravel()[0]
    y = spherePositionMM.ravel()[1]
    z = spherePositionMM.ravel()[2]

    # compute bounding square from the corners of the XYZ-aligned cube closest to the detector
    # scrap that, do all corners for safety
    corners = numpy.zeros((8, 2), dtype=int)
    n = 0
    for dx in [-1, 1]:
        for dy in [-1, 1]:
            for dz in [-1, 1]:
                corners[n] = pointToDetectorPixelRange(
                    numpy.array(
                        [
                            x + radiusMM * dx + radiusMM * radiusMargin * dx,
                            y + radiusMM * dy + radiusMM * radiusMargin * dy,
                            z + radiusMM * dz + radiusMM * radiusMargin * dz,
                        ]
                    ),
                    sourceDetectorDistMM=sourceDetectorDistMM,
                    pixelSizeMM=pixelSizeMM,
                    detectorResolution=detectorResolution,
                )
                n += 1

    # print("singleSphereToDetectorPixelRange():", numpy.max(corners, axis=0))
    # print("singleSphereToDetectorPixelRange():", numpy.min(corners, axis=0))
    maxRC = numpy.max(corners, axis=0)
    minRC = numpy.min(corners, axis=0)

    maxRC = numpy.minimum(maxRC, detectorResolution)  # clip bounding box if past limits
    minRC = numpy.maximum(minRC, [0, 0])  # clip bounding box if past limits
    return numpy.array([[minRC[0], maxRC[0]], [minRC[1], maxRC[1]]])


def projectSphereMM(
    spheresPositionMM,
    radiiMM,
    ROIcentreMM=None,
    ROIradiusMM=None,
    sourceDetectorDistMM=100,
    pixelSizeMM=0.1,
    detectorResolution=[512, 512],
    projector="numba",
    transformationCentreMM=None,
    transformationMatrix=None,
    blur=None,
    scattering=0,
    focalSpotSize=None,
    displacementsMM=None,
):
    """
    This is the python wrapping function for the C++ projector, it gets projection geometry,
    list of particle positions and radii, projected in the X direction.
    The output is the crossed distance for each sphere in mm.

    Please refer to the figures/projectedCoords_v2 for geometry

    In order to allow projections from diffferent angles, an XYZ centre and a transformation matrix can be provided,
    which will be applied to the particle positions.

    Parameters
    ----------
        spheresPositionMM : Nx3 2D numpy array of floats
            xyz positions of spheres in mm, with the origin being the middle of the detector

        radiiMM : 1D numpy array of floats
            Particle radii for projection

        ROIcentreMM : 3-component vector of floats, optional
            Particle position for ROI
            Default = Disactivated (None)

        ROIradiusMM : float, optional
            Particle radius for ROI
            Default = Disactivated (None)

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector.
            Set as numpy.inf for parallel projection
            Default = 100

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        detectorResolution : 2-component list of ints, optional
            Number of pixels rows, columns of detector
            Default = [512,512]

        projector : string, optional
            Algorithm for the projector. Options are 'C', 'numpy' or 'cupy'
            Default = 'C'

        transformationCentreMM : 3-component vector
            XYZ centre for a transformation
            Default = None

        transformationMatrix : 3x3 numpy array
            XYZ transformation matrix to apply to coordinates
            Default = None

        blur : float, optional
            sigma of blur to pass to scipy.ndimage.gaussian_filter to
            blur the radiograph at the end of everything

    Returns
    -------
        projectionMM : 2D numpy array of floats
            Radiography containing the total crossed distance through the spheres distance in mm for each beam path.
            To turn this into a radiography, the distances should be put into a calibrated Beer-Lambert law
    """

    assert len(spheresPositionMM.shape) == 2, "projectSphere.projectSphereMM(): spheresPositionMM is not 2D array"
    assert len(radiiMM.shape) == 1, "projectSphere.projectSphereMM(): radiiMM is not 1D array"
    assert (
        spheresPositionMM.shape[0] == radiiMM.shape[0]
    ), "projectSphere.projectSphereMM(): number of radii and number of sphere positions not the same"
    assert (transformationCentreMM is None) == (
        transformationMatrix is None
    ), "projectSphere.projectSphereMM(): transformationCentreMM and transformationMatrix must both be set or unset"

    # Transform coordinates if so asked
    if transformationCentreMM is not None:
        tmp = spheresPositionMM - transformationCentreMM
        for n, t in enumerate(tmp):
            tmp[n] = numpy.dot(transformationMatrix, t)
        tmp += transformationCentreMM
        spheresPositionMM = tmp

        # On the fly let's also move ROIcentreMM, no this is moved into
        # transformation options in singleSphereToDetectorPixelRange
        # if ROIcentreMM is not None:
        # ROIcentreMM = numpy.dot(transformationMatrix,
        #                         numpy.array(ROIcentreMM).ravel()  -
        #                             numpy.array(transformationCentreMM).ravel()) + transformationCentreMM

    # Special case: use this to indicate a parallel projection in the X-direction, so x-positions are ignored.
    if sourceDetectorDistMM == numpy.inf:
        if ROIcentreMM is None or ROIradiusMM is None:
            # Again refer to projectedCoords_v2.pdf
            # -z in space goes with j on the detector and
            # -y in space goes with i on the detector

            # use algorithm from tomopack
            iDetector = numpy.linspace(
                pixelSizeMM * detectorResolution[0] / 2.0,
                -pixelSizeMM * detectorResolution[0] / 2.0,
                detectorResolution[0],
            ).astype("<f4")
            jDetector = numpy.linspace(
                pixelSizeMM * detectorResolution[1] / 2.0,
                -pixelSizeMM * detectorResolution[1] / 2.0,
                detectorResolution[1],
            ).astype("<f4")

            iDetector2D, jDetector2D = numpy.meshgrid(jDetector, iDetector)

            projectionXmm = numpy.zeros(detectorResolution, dtype=("<f4"))

            for spherePositionMM, radiusMM in zip(spheresPositionMM, radiiMM):
                # This function returns the parallel projection (dims of x_detector) of particles positioned at x and y
                # print("Adding sphere at: ", spherePositionMM, 'r: ', radiusMM)
                tmp = (
                    radiusMM**2 - (spherePositionMM[1] - iDetector2D) ** 2 - (spherePositionMM[2] - jDetector2D) ** 2
                )
                mask = tmp > 0
                projectionXmm[mask] += 2 * numpy.sqrt(tmp[mask])
            return projectionXmm
        else:
            print("projectSphere.projectSphereMM(): ROI mode in parallel not yet implemented (but shoudn't be to hard)")
            return

    # Flip axes for the C++ projector after applying transformation
    spheresPositionMM = spheresPositionMM * numpy.array([1, -1, -1])

    if projector == "C":
        # sys.path.append(os.path.join(os.path.dirname(__file__), "/"))
        # from projectSphereC3 import PyInit_projectSphereC3 as project_func
        #from radioSphere.projectSphere.CProjector import project_func
        #dtype = "<f4"
        print("C projector discontinued in v2 of radioSphere")
        return

    elif projector == "numpy":
        from radioSphere.projectSphere.NumpyProjector import project as project_func
        dtype = numpy.float32

    elif projector == "cupy":
        #import cupy
        from radioSphere.projectSphere.CupyProjector import (projectAgnostic1 as project_func,)
        dtype = numpy.float32

    elif projector == "numba":
        from radioSphere.projectSphere.NumbaProjector import project as project_func
        dtype = numpy.float32

    else:
        print("projectSphere.projectSphereMM(): This projection mode not implemented")
        return

    if ROIcentreMM is None or ROIradiusMM is None:
        projectionXmm = numpy.zeros(detectorResolution, dtype=dtype)

        if displacementsMM is None:
            # This C++ function fill in the passed projectionXmm array
            project_func(
                numpy.array([sourceDetectorDistMM], dtype=dtype),
                radiiMM.astype(dtype),
                numpy.linspace(
                    -pixelSizeMM * detectorResolution[0] / 2.0,
                    pixelSizeMM * detectorResolution[0] / 2.0,
                    detectorResolution[0],
                ).astype(dtype),
                numpy.linspace(
                    -pixelSizeMM * detectorResolution[1] / 2.0,
                    pixelSizeMM * detectorResolution[1] / 2.0,
                    detectorResolution[1],
                ).astype(dtype),
                spheresPositionMM.astype(dtype),
                projectionXmm,
                numpy.array([scattering]).astype(dtype),
                numpy.array([focalSpotSize]).astype(dtype),
            )
        else:
            delta_blur = pixelSizeMM / 4.0  # increment in MM between sphere centres to evaluate projection at
            n_delta = numpy.ceil(abs(displacementsMM) / delta_blur) // 2 * 2 + 1  # round up to next odd number
            n_delta = max(
                2, int(n_delta.max())
            )  # currently just do global maximum number and project everything extra times to not have to worry
            # about some getting more projections than others

            for i in range(n_delta):
                curSpheresPositionMM = (
                    spheresPositionMM - 0.85 * displacementsMM / 2 + i / (n_delta - 1) * 0.85 * displacementsMM
                )

                project_func(
                    numpy.array([sourceDetectorDistMM], dtype=dtype),
                    radiiMM.astype(dtype),
                    numpy.linspace(
                        -pixelSizeMM * detectorResolution[0] / 2.0,
                        pixelSizeMM * detectorResolution[0] / 2.0,
                        detectorResolution[0],
                    ).astype(dtype),
                    numpy.linspace(
                        -pixelSizeMM * detectorResolution[1] / 2.0,
                        pixelSizeMM * detectorResolution[1] / 2.0,
                        detectorResolution[1],
                    ).astype(dtype),
                    curSpheresPositionMM.astype(dtype),
                    projectionXmm,
                    numpy.array([scattering]).astype(dtype),
                    numpy.array([focalSpotSize]).astype(dtype),
                )

            # projectionXmm = project_capsule(numpy.array([sourceDetectorDistMM], dtype=dtype),
            #                              radiiMM.astype(dtype),
            #                              numpy.linspace(-pixelSizeMM*detectorResolution[0]/2.,
            #                                              pixelSizeMM*detectorResolution[0]/2.,
            #                                              detectorResolution[0]).astype(dtype),
            #                              numpy.linspace(-pixelSizeMM*detectorResolution[1]/2.,
            #                                              pixelSizeMM*detectorResolution[1]/2.,
            #                                              detectorResolution[1]).astype(dtype),
            #                              spheresPositionMM.astype(dtype),
            #                              displacementsMM.astype(dtype),
            #                              projectionXmm)
            projectionXmm /= n_delta

    elif ROIcentreMM is not None and ROIradiusMM is not None:
        # Make sure there's only one sphere:
        assert (
            len(spheresPositionMM.ravel()) == 3
        ), "projectSphere.projectSphereMM(): in ROI mode I want only one sphere"

        # Get limits
        limits = singleSphereToDetectorPixelRange(
            ROIcentreMM.ravel(),
            ROIradiusMM,
            radiusMargin=0.1,
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
            transformationCentreMM=transformationCentreMM,
            transformationMatrix=transformationMatrix,
        )

        # Define (smaller) projection array to fill in
        projectionXmm = numpy.zeros((limits[0, 1] - limits[0, 0], limits[1, 1] - limits[1, 0]), dtype=("<f4"))

        if displacementsMM is None:
            # This C++ function fill in the passed projectionXmm array -- not limits after linspace
            project_func(
                numpy.array([sourceDetectorDistMM], dtype=dtype),
                radiiMM.astype(dtype),
                numpy.linspace(
                    -pixelSizeMM * detectorResolution[0] / 2.0,
                    pixelSizeMM * detectorResolution[0] / 2.0,
                    detectorResolution[0],
                ).astype(dtype)[limits[0, 0] : limits[0, 1]],
                numpy.linspace(
                    -pixelSizeMM * detectorResolution[1] / 2.0,
                    pixelSizeMM * detectorResolution[1] / 2.0,
                    detectorResolution[1],
                ).astype(dtype)[limits[1, 0] : limits[1, 1]],
                spheresPositionMM.astype(dtype),
                projectionXmm,
                numpy.array([scattering]).astype(dtype),
                numpy.array([focalSpotSize]).astype(dtype),
            )
        else:
            delta_blur = pixelSizeMM / 4.0  # increment in MM between sphere centres to evaluate projection at
            n_delta = numpy.ceil(abs(displacementsMM) / delta_blur) // 2 * 2 + 1  # round up to next odd number
            n_delta = max(
                2, int(n_delta.max())
            )  # currently just do global maximum number and project everything extra times to not have to worry
            # about some getting more projections than others

            for i in range(n_delta):
                curSpheresPositionMM = (
                    spheresPositionMM - 0.85 * displacementsMM / 2 + i / (n_delta - 1) * 0.85 * displacementsMM
                )

                # This C++ function fill in the passed projectionXmm array -- not limits after linspace
                project_func(
                    numpy.array([sourceDetectorDistMM], dtype=dtype),
                    radiiMM.astype(dtype),
                    numpy.linspace(
                        -pixelSizeMM * detectorResolution[0] / 2.0,
                        pixelSizeMM * detectorResolution[0] / 2.0,
                        detectorResolution[0],
                    ).astype(dtype)[limits[0, 0] : limits[0, 1]],
                    numpy.linspace(
                        -pixelSizeMM * detectorResolution[1] / 2.0,
                        pixelSizeMM * detectorResolution[1] / 2.0,
                        detectorResolution[1],
                    ).astype(dtype)[limits[1, 0] : limits[1, 1]],
                    curSpheresPositionMM.astype(dtype),
                    projectionXmm,
                    numpy.array([scattering]).astype(dtype),
                    numpy.array([focalSpotSize]).astype(dtype),
                )

            projectionXmm /= n_delta
            # This C++ function fill in the passed projectionXmm array
            # project_capsule_func(numpy.array([sourceDetectorDistMM], dtype=dtype),
            # radiiMM.astype(dtype),
            # numpy.linspace(-pixelSizeMM*detectorResolution[0]/2.,
            # pixelSizeMM*detectorResolution[0]/2.,
            # detectorResolution[0]).astype(dtype),
            # numpy.linspace(-pixelSizeMM*detectorResolution[1]/2.,
            # pixelSizeMM*detectorResolution[1]/2.,
            # detectorResolution[1]).astype(dtype),
            # spheresPositionMM.astype(dtype),
            # displacementsMM.astype(dtype),
            # projectionXmm)
    else:
        print("projectSphere.projectSphereMM(): If you set ROIcentreMM you must also set ROIradiusMM")

    if blur is not None:
        projectionXmm = scipy.ndimage.gaussian_filter(projectionXmm, sigma=blur)

    return projectionXmm


def computeLinearBackground(radioMM, mask=None):
    """
    This function computes a plane-fit for background greylevels to help with the correction of the background


    Parameters
    ----------
        radioMM : 2D numpy array of floats
            The image

        mask : 2D numpy array of bools, optional
            Masked zone to fit?

    Returns
    -------
        background : 2D numpy array of floats
            Same size as radioMM
    """
    x, y = numpy.meshgrid(numpy.arange(radioMM.shape[0]), numpy.arange(radioMM.shape[1]), indexing="ij")

    def plane(params, z, validPoints):
        output = params[0] * x[validPoints] + params[1] * y[validPoints] + z[validPoints] - params[2]
        return numpy.ravel(output)

    if mask is None:
        mask = numpy.abs(radioMM) < 0.05 * radiiMM[0]  # just where it is reasonable valued
    # isBackgroundMask *= numpy.abs(residualMM) > 0.1*radiiMM[0] # just where it is reasonable valued
    # plt.imshow(isBackgroundMask); plt.show()
    LSQret = scipy.optimize.least_squares(plane, [0, 0, 0], args=[radioMM, mask])

    backgroundPlane = -LSQret["x"][0] * x - LSQret["x"][1] * y + LSQret["x"][2]

    return backgroundPlane


def gl2mm(radio, calib=None):
    """
    This function takes a greylevel radiograph (I/I0) and returns
    a radiograph in mm (L), representing the path length encountered.

    Parameters
    ----------
        radio : a 2D numpy array of floats

        calib : dictionary (optional)
            This contains a calibration of greylevels to mm
            If not passed \\mu is assumed to be 1.
    """
    if calib is not None:
        print("projectSphere.gl2mm() I need to be implemented")
    return -numpy.log(radio)


def mm2gl(radioMM, calib=None):
    """
    This function takes a radiograph in mm (L) and returns
    a radiograph in greylevels (I/I0)

    Parameters
    ----------
        radioMM : a 2D numpy array of floats

        calib : dictionary (optional)
            This contains a calibration of greylevels to mm
            If not passed \\mu is assumed to be 1.
    """
    if calib is not None:
        print("projectSphere.mm2gl() I need to be implemented")
    return numpy.exp(-radioMM)


def computeMotionKernel(posPrev, posPost, displacementThreshold=1):
    """
    Helper function that calculates unique motion kernel in 2D (detector plane) based on two given positions.
    Its size is given by the maximum displacement and its direction corresponds to the direction of the
    displacement vector.

    Parameters
    ----------
        posPrev : 2D numpy array of floats
            Nx3 positions of the particles in MM (step i-1)

        posPost : 2D numpy array of floats
            Nx3 positions of the particles in MM (step i+1)

        displacementThreshold : float
            Threshold displacement in MM
            Only if displacement is bigger than this value, a kernel is calculated

    Returns
    -------
        kernel : 2D numpy array of floats
            Motion kernel
    """
    # Calculate displacement only for y-z direction (detector plane)
    dx = posPost[1:] - posPrev[1:]

    kernelR = None
    if any(y > displacementThreshold for y in abs(dx)):
        # create an empty array with size the max of the displacement
        kernelSize = int(numpy.ceil(numpy.abs(dx).max() / 2) * 2 + 1)  # round to the nearest odd number
        # kernelSize = int(numpy.ceil(numpy.abs(dxSphere).max()/2)*2 + 3) #round to the nearest odd number
        kernel = numpy.zeros((kernelSize, kernelSize))

        # fill in a horizontal step (or hat) function
        kernel[int((kernelSize - 1) / 2), :] = numpy.ones(kernelSize)

        # rotate kernel to follow the direction of the displacement vector
        direction = dx / numpy.linalg.norm(dx)
        with numpy.errstate(divide="ignore", invalid="ignore"):
            theta = numpy.rad2deg(numpy.arctan(direction[1] / direction[0]))
        kernelR = scipy.ndimage.rotate(kernel, -theta, reshape=False, order=3, mode="reflect", prefilter=False)

        # normalise and clean interpolation small values (coming from the ndimage rotation)
        kernelR /= kernelSize
        kernelR[kernelR < 0.01] = 0

        # kernelR = kernel/kernelSize

    return kernelR


def project_capsule(SDD, radiiMM, widths, heights, positionsMM, displacementsMM, proj):
    """
    Unused projector to project capsules directly. DO NOT USE THIS.
    It is faster, safer, and much more accurate to simulate motion blurring by repeated projection of spheres.
    This method gets the shape right but the attenuation value is incorrect inside the cylinder.
    """
    for sphere in range(len(positionsMM)):
        axis_length = numpy.linalg.norm(displacementsMM[sphere])
        V_sphere = 4 / 3 * numpy.pi * radiiMM[sphere] ** 3
        V_capsule = V_sphere + numpy.pi * radiiMM[sphere] ** 2 * axis_length
        path_reduction_factor = (
            V_sphere / V_capsule
        )  # a capsule has a lower attenuation because the same mass is smeared through a larger volume, so we need to
        # lower the effective path length through the material

        # define a local coordinate reference system with z along the direction of displacement,
        # and x and y normal to that
        z_unit_vector = displacementsMM[sphere] / axis_length
        y_vector = numpy.cross(
            z_unit_vector, z_unit_vector * numpy.random.rand(1, 3)
        )  # dont really care which direction y is in as long as it is normal to z
        x_vector = numpy.cross(y_vector, z_unit_vector)  # and a third normal direction
        A = numpy.vstack(
            [
                x_vector / numpy.linalg.norm(x_vector),
                y_vector / numpy.linalg.norm(y_vector),
                z_unit_vector,
            ]
        )  # rotation matrix to go from global to local coordinates
        ray_source_rotated = numpy.dot(A, -positionsMM[sphere])  # apply the rotation matrix

        for i, y in enumerate(widths):
            for j, z in enumerate(heights):

                ray_vector = numpy.array([SDD, y, z])
                rotated_vector = numpy.dot(A, ray_vector)

                path_length = _get_capsule_path_length(rotated_vector, ray_source_rotated, axis_length, radiiMM[sphere])
                proj[i, j] += path_length * path_reduction_factor

    return proj


def _get_capsule_path_length(ray_vector, ray_source, axis_length, radius):
    path_length = 0

    mag = numpy.linalg.norm(ray_vector)
    ray_unit_vector = ray_vector / mag

    # check for intersection with cylinder at ANY LOCAL z,
    # i.e. does it cross the circle defined by the capsule.
    # not a guarantee of collision with the capsule, just a collision with the infinite cylinder.
    a = ray_unit_vector[0] ** 2 + ray_unit_vector[1] ** 2
    b = 2 * ray_unit_vector[0] * ray_source[0] + 2 * ray_unit_vector[1] * ray_source[1]
    c = ray_source[0] ** 2 + ray_source[1] ** 2 - radius**2

    discriminant_squared = b**2 - 4 * a * c
    if discriminant_squared > 0:  # there must be two solutions, check them both for collisions
        l_0 = (-b + numpy.sqrt(discriminant_squared)) / 2 / a
        l_1 = (-b - numpy.sqrt(discriminant_squared)) / 2 / a
        l_2, x_0_good = _get_capsule_collision(l_0, ray_unit_vector, ray_source, radius, axis_length / 2.0, 1)
        l_3, x_1_good = _get_capsule_collision(l_1, ray_unit_vector, ray_source, radius, axis_length / 2.0, -1)

        if x_0_good and x_1_good:  # if both have collisions, we have a ray that enters and leaves the capsule
            path_length = l_2 - l_3

    return path_length


def _get_capsule_collision(length, u_hat, o, r, a, sign):
    z = o[2] + u_hat[2] * length  # z position at intercept with cylinder
    if numpy.abs(z) < a / 2:
        return [length, True]  # inside the cylindrical part

    if z > 0:
        z_offset = a / 2  # pick one sphere to check
    else:
        z_offset = -a / 2
    c = numpy.array([0, 0, z_offset])  # centre of sphere
    det = numpy.dot(u_hat, o - c) ** 2 - (numpy.linalg.norm(o - c) ** 2 - r**2)
    if det > 0:  # if the ray collides with the sphere
        length = -numpy.dot(u_hat, o - c) + sign * numpy.sqrt(det)  # pick the correct part of the sphere
        return [length, True]
    return [None, False]  # nothing found


def remove_spherical_distortion(im, SDD, W, H):
    """
    Cone beam projections recorded on flat detector panels are inherently distorted
    due to the differing path lengths from the source to the detector panel. This
    function reprojects the data onto a new grid that is formed along the imaginary
    surface of a spherical detector panel that is the same distance as the nearest
    point on the real detector panel. This will fix (somewhat) the distortion
    observed in other projections. Use this function if tomopack doesn't find
    particles near the edges of your sample.

    Parameters
    ----------
        im : 2D numpy array of floats
            The image

        SDD : float
            Source to detector distance in mm.

        W : float
            The width of the detector panel in mm

        H : float
            The height of the detector panel in mm

    Returns
    -------
        im : 2D numpy array of floats
            The undistorted image
    """

    # img - the source image
    # SDD - source to detector distance
    # W - width of the detector panel (in y direction)
    # H - height of the detector panel (in z direction)

    # u is the new horizontal coordinate that we are going to map across linearly
    # v is the vertical coordinate

    theta_u_lim = numpy.arctan2(W / 2, SDD)  # half angle across sphere that we are going to map
    theta_v_lim = numpy.arctan2(H / 2, SDD)
    theta_u = numpy.linspace(-theta_u_lim, theta_u_lim, im.shape[0])
    theta_v = numpy.linspace(-theta_v_lim, theta_v_lim, im.shape[1])

    Theta_v, Theta_u = numpy.meshgrid(theta_u, theta_v, indexing="ij")

    x_hat = numpy.cos(Theta_u) * numpy.cos(Theta_v)
    y_hat = numpy.sin(Theta_u) * numpy.cos(Theta_v)
    z_hat = numpy.sin(Theta_v)

    vec_length = SDD / x_hat  # length of the vector to hit the detector panel

    # coordinates of the new data points in the old image
    ys = y_hat * vec_length
    zs = z_hat * vec_length

    # and where those positions are on the detector panel in pixels
    ys_px = ys * im.shape[0] / W + im.shape[0] / 2.0
    zs_px = zs * im.shape[1] / H + im.shape[1] / 2.0

    return scipy.ndimage.map_coordinates(im, (zs_px, ys_px))


if __name__ == "__main__":
    # detector properties
    ny = 500
    nz = 400
    Ly = Lz = 20  # width and height of panel

    SDD = 100  # distance from source to detector
    w = numpy.linspace(-Ly / 2, Ly / 2, ny)
    h = numpy.linspace(-Lz / 2, Lz / 2, nz)
    nspheres = 10
    radiiMM = (numpy.random.rand(nspheres) + 2) / 3
    pos = 10 * numpy.random.rand(nspheres, 3) - 5  # ±5
    pos[:, 0] = 98
    # print(pos)
    disp = numpy.random.rand(nspheres, 3)
    # disp = 1e-10*numpy.ones([nspheres,3])
    # disp[:,1] = radiiMM

    # im = numpy.zeros([ny,nz])
    # project_capsule(SDD, radiiMM, w, h, pos, disp, im)
    import time

    for projector in ["C", "numpy", "cupy"]:  # ,'numba']:
        tic = time.time()
        for i in range(100):
            im = projectSphereMM(
                pos,
                radiiMM,
                sourceDetectorDistMM=SDD,
                pixelSizeMM=Ly / ny,
                detectorResolution=[ny, nz],
                projector=projector,
                blur=None,
                displacementsMM=None,
            )
        toc = time.time()
        print(f"{projector} projector: {1000*(toc-tic)}ms (lower is better)")

    tic = time.time()
    im1 = projectSphereMM(
        pos,
        radiiMM,
        sourceDetectorDistMM=SDD,
        pixelSizeMM=Ly / ny,
        detectorResolution=[ny, nz],
        projector="cupy",
        blur=None,
        displacementsMM=None,
        scattering=0.2,
    )
    toc = time.time()
    print(toc - tic)

    import matplotlib.pyplot as plt

    plt.subplot(131)
    plt.pcolormesh(w, h, im.T, shading="auto", vmin=0)
    plt.xlabel("y")
    plt.ylabel("z")
    plt.colorbar()
    plt.subplot(132)
    plt.pcolormesh(w, h, im1.T, shading="auto", vmin=0)
    plt.xlabel("y")
    plt.ylabel("z")
    plt.colorbar()
    plt.subplot(133)
    plt.pcolormesh(w, h, im1.T - im.T, shading="auto", vmin=-0.1, vmax=0.1, cmap="bwr")
    plt.xlabel("y")
    plt.ylabel("z")
    plt.colorbar()
    plt.show()
