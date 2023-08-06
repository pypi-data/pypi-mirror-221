import numpy, scipy, tifffile
import matplotlib.pyplot as plt
import scipy.optimize

# import PySide2
# import pyqtgraph as pg

# from functions import *
import time

numpy.set_printoptions(suppress=True)


def optimiseSensitivityFields(
    radioMM,
    xyzGuessesMM,
    radiiMM,
    iterationsMax=20,
    minDeltaMM=0.01,
    perturbationMM=None,
    displacementsMM=None,
    sourceDetectorDistMM=100,
    pixelSizeMM=0.1,
    detectorResolution=[512, 512],
    verbose=0,
    DEMcorr=False,
    DEMparameter=0.01,
    limitsX=None,
    regularisation=False,
    regularisationThreshold=numpy.inf,
    weightX=1.0,
    GRAPH=False,
    NDDEM_output=False,
    blur=None,
    motionKernel=None,
    showConvergence=False,
    optimiseGL=False,
    optimiseGLcalib=None,
    outDir=None,
    projector="numba",
    focalSpotSize=0,
    scattering=0,
):
    """
    This function takes in a reference projection (radioMM) in mm and sphere positions
    and moves them around to minimise the residual as far as possible.
    The technique used is the calculation of a sensitivity field in x, y, z with a perturbation of the
    synthetic radiograph.
    This is done locally in a ROI around each particle, which avoids doing the projection for all pixels.

    Parameters
    ----------
        radioMM : 2D numpy array of floats
            Projection of distance crossed in spheres in MM

        xyzGuessesMM : 2D numpy array of floats
            Nx3 guesses for the positions of the particles in MM

        radiiMM : 1D numpy array of floats
            Particle radii for projection

        iterationsMax : int, optional
            Number of iterations to perform
            Default = 20

        minDeltaMM : float, optional
            If step size gets below this value, stop
            Default = 0.01

        perturbationMM : either a single float or a 3-component list of floats, optional
            Size of the perturbation step to compute the sensitivity field
            Default = mean particle radius * numpy.array([SOD^2/(2*SDD), 0.5, 0.5])

        displacementsMM : 2D numpy array of floats, optional
            Nx3 displacement vectors to account for blur
            Default = None

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector
            Default = 100

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        detectorResolution : 2-component list of ints, optional
            Number of pixels height, width of detector
            Default = [512,512]

        verbose : int, optional
            Print noisly? 0 = quiet except warning, 1=iterations, 2=everything
            Default = 1

        DEMcorr : bool, optional
            Perform a soft DEM correction between all iterations?
            Default = False

        DEMparameter : float, optional
            If DEMcorr is activated
            Stiffness and timestep wrapped into one
            Default = 0.01

        limitsX : two-component list of floats, optional
            Minimum and maximum zoom position in the direction of the X-ray beam
            Default = None, no limits

        regularisation : bool, optional
            Perform a harsh "regularisation" in time in the direction of the X-ray beam
            Default = False

        regularisationThreshold : float, optional
            Threshold (MM) in distance between current X-position and input guess
            If this is exceeded, the X-position is forced back to the input one
            Default = numpy.inf

        weightX : float, optional
            Extra weighting factor applied in the direction of the X-ray beam
            It is applied inside the least_squares minimisation damping down X oscillations
            Default = 1.

        NDDEM_output : bool, optional
            Save every iteration so that it can be viewed using NDDEM - sorry Eddy

        blur : dictionary of floats, optional
            Dictionary containing a unique sigma for each sphere
            to pass to `scipy.ndimage.gaussian_filter()` to blur the synthetic radiographs
            Default = None

        motionKernel : dictionary of floats,, optional
            Dictionary containing a unique motion kernel (2d array of floats) for each sphere
            to convolve the synthetic radiographs
            Default = None

        showConvergence : bool, optional
            show a graph of the system converging with iterations
            Default = False

        optimiseGL : bool, optional
            Perform optimisation on image in greylevels rather than mm?
            Default = False

        optimiseGLcalib : dictionary, optional
            Calibration to apply for converting mm to greylevels and back
            Default = None


    Returns
    -------
        xzyMM : Corrected positions array
    """
    import radioSphere.projectSphere

    # This is the function that will be optimised to match synthetic residuals to the real measured ones
    # ...it's the heart of the approach
    # attempt to find weights a, b, c for the x, y, z sensitivity fields with leastsquares
    def optimiseMe(weights, residualToMatch, sensXYZ):
        # print("optimiseMe(): weights = ", weights)
        output = residualToMatch - weightX * weights[0] * sensXYZ[0] - weights[1] * sensXYZ[1] - weights[2] * sensXYZ[2]
        # return numpy.ravel(output[output != 0])
        return numpy.ravel(output)

    if optimiseGL:
        radio = radioSphere.mm2gl(radioMM, calib=optimiseGLcalib)
    else:
        radio = radioMM

    if GRAPH:
        # from PyQt5 import QtGui
        # app = QtGui.QApplication([])
        # w = QtGui.QWidget()
        plt.subplot(1, 1, 1)
        plt.axis([radioMM.shape[1], 0, radioMM.shape[0], 0])
        plt.ion()
        ##plt.show()
        ##plt.subplot(1,1,1)
        # imv = pg.ImageView()
        ##imv.show()
        # layout = QtGui.QGridLayout()
        # w.setLayout(layout)
        # layout.addWidget(imv, 0, 0)
        # w.show()
        # app.exec_()
        # pg.GraphicsWindow()
        # pw = pg.image(radioMM)
        pass

    if NDDEM_output:
        from radioSphere.DEM.nddem import write_infile

        write_infile(xyzGuessesMM, radiiMM, iterationsMax)

    assert (
        len(radiiMM) == xyzGuessesMM.shape[0]
    ), "optimiseSensitivityFields(): number of radii and sphere positions not the same"

    sourceObjectDistanceMM = numpy.mean(numpy.sqrt(numpy.sum(xyzGuessesMM**2, axis=1)))

    # perturbXscaling = 4
    # perturbXscaling = sourceObjectDistanceMM**2/radiiMM[0]/sourceDetectorDistMM
    perturbXscaling = sourceObjectDistanceMM / radiiMM[0]

    if perturbationMM is None:
        # Pixel size in middle of sample
        pixelSizeMMatCOR = pixelSizeMM * (numpy.mean(xyzGuessesMM[:, 0]) / sourceDetectorDistMM)

        # Perturb 1px in detector and 4 in the x-direction (this should be function of beam angle)
        perturbationMM = (perturbXscaling * pixelSizeMMatCOR, pixelSizeMMatCOR, pixelSizeMMatCOR)
        if verbose > 0:
            print(
                f"optimiseSensitivityFields(): using a perturbation of (which is 1 px in detector plane and larger in X):\n\tX: {perturbationMM[0]:0.3f}mm Y: {perturbationMM[1]:0.3f}mm Z: {perturbationMM[2]:0.3f}mm"
            )
    elif isinstance(perturbationMM, float):
        perturbationMM = (perturbXscaling * perturbationMM, perturbationMM, perturbationMM)
        if verbose > 0:
            print(
                f"optimiseSensitivityFields(): using a perturbation of:\n\tX: {perturbationMM[0]:0.3f}mm Y: {perturbationMM[1]:0.3f}mm Z: {perturbationMM[2]:0.3f}mm"
            )

    # OS 24/03/22:
    # define limitsX
    if limitsX:
        minZoom = max(limitsX)
        maxZoom = min(limitsX)
        limitsX = True

    # initialise variables
    iterations = 0
    xyzMM = xyzGuessesMM.copy().astype("<f4")
    xyzMMprev = xyzGuessesMM.copy().astype("<f4")
    if verbose > 1:
        print("Initial pos:\n", xyzMM)

    # step = numpy.array([numpy.inf, numpy.inf, numpy.inf])
    dX = numpy.inf
    # outputForFigure = []
    while iterations < iterationsMax and dX > minDeltaMM:
        if verbose > 0:
            print("\tIt:", iterations, end="")
        # if verbose > 1: print("\tperturbationMM:\t", perturbationMM)

        # Generate radio with current guess of position (xyzMM)
        guessedRadioMM = radioSphere.projectSphere.projectSphereMM(
            xyzMM,
            radiiMM,
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
            displacementsMM=displacementsMM,
            projector=projector,
            focalSpotSize=focalSpotSize,
            scattering=scattering
            # blur=blur
        )

        if optimiseGL:
            guessedRadio = radioSphere.mm2gl(guessedRadioMM, calib=optimiseGLcalib)
        else:
            guessedRadio = guessedRadioMM

        # update residual
        residual = radio - guessedRadio

        ## create an empty mask that stores locations with particles in the ROI
        # if removeBackground: isBackgroundMask = numpy.ones_like(radioMM,dtype=bool)
        ## Could easily parallelise here, these are all independent corrections
        limits = [[] for _ in range(len(radiiMM))]
        displacementFactor = numpy.ones((len(radiiMM)))
        for sphere in range(len(radiiMM)):
            # if verbose > 2: print("\tSphere {} of {}".format(sphere+1, len(radiiMM)))
            # Compute sensitivity fields for this perturbationMM -- this is the current virtual radiograph
            #   Perturbed by a given perturbationMM in x, y, z independently

            # OS 30/05/22:
            # we need to enlarge our ROI to account for the displacement
            factor = 1
            if isinstance(displacementsMM, numpy.ndarray):
                # set factor as a function of sphere radius
                factor = max(1.0, max(abs(displacementsMM[sphere])) / (radiiMM[sphere] / 1.0))

            # Compute sensitivity field only for this particle, this is debatable, so generate its reference projection
            # Since we're going to try to do this locally, let's pre-compute the limits on the detector
            limits[sphere] = radioSphere.projectSphere.singleSphereToDetectorPixelRange(
                xyzMM[sphere],
                radiiMM[sphere] * 1.2 * factor,
                radiusMargin=0.1,
                sourceDetectorDistMM=sourceDetectorDistMM,
                pixelSizeMM=pixelSizeMM,
                detectorResolution=detectorResolution,
            )

            displacementFactor[sphere] = factor

            # if removeBackground: isBackgroundMask[limits[sphere][0,0]:limits[sphere][0,1], limits[sphere][1,0]:limits[sphere][1,1]] = False

        for sphere in range(len(radiiMM)):
            if verbose > 2:
                print("\tSphere {} of {}".format(sphere + 1, len(radiiMM)))

            # OS 30/05/22:
            # pass sphere disp in projection function
            displacementMMSphere = None
            if isinstance(displacementsMM, numpy.ndarray):
                displacementMMSphere = displacementsMM[sphere]

            # Compute local reference projection for this sphere with ROI activated around the sphere
            sphereRefProjectionMM = radioSphere.projectSphere.projectSphereMM(
                numpy.array([xyzMM[sphere]]),
                numpy.array([radiiMM[sphere]]),
                sourceDetectorDistMM=sourceDetectorDistMM,
                pixelSizeMM=pixelSizeMM,
                detectorResolution=detectorResolution,
                ROIcentreMM=xyzMM[sphere].copy(),
                ROIradiusMM=radiiMM[sphere] * 1.2 * displacementFactor[sphere],
                projector=projector,
                displacementsMM=displacementMMSphere,
                focalSpotSize=focalSpotSize,
                scattering=scattering
                # blur=blur
            )

            # crop ROI for each sphere
            radioCropSphere = radio[
                limits[sphere][0, 0] : limits[sphere][0, 1],
                limits[sphere][1, 0] : limits[sphere][1, 1],
            ]
            guessedRadioCropSphere = guessedRadio[
                limits[sphere][0, 0] : limits[sphere][0, 1],
                limits[sphere][1, 0] : limits[sphere][1, 1],
            ]

            # apply kernel to each ROI
            if motionKernel:
                if motionKernel[sphere] is not None:
                    guessedRadioCropSphere = scipy.ndimage.convolve(guessedRadioCropSphere, motionKernel[sphere])
                    sphereRefProjectionMM = scipy.ndimage.convolve(sphereRefProjectionMM, motionKernel[sphere])

            if blur:
                if blur[sphere] is not None:
                    guessedRadioCropSphere = scipy.ndimage.gaussian_filter(guessedRadioCropSphere, sigma=blur[sphere])
                    sphereRefProjectionMM = scipy.ndimage.gaussian_filter(sphereRefProjectionMM, sigma=blur[sphere])

            residualCropSphere = radioCropSphere - guessedRadioCropSphere

            if optimiseGL:
                sphereRefProjection = radioSphere.mm2gl(sphereRefProjectionMM, calib=optimiseGLcalib)
            else:
                sphereRefProjection = sphereRefProjectionMM

            # Pre-allocate sens field, since it's local it should be the same shape as sphereRefProjectionMM
            sensXYZ = numpy.zeros((3, sphereRefProjection.shape[0], sphereRefProjection.shape[1]), dtype=float)

            # if GRAPH and iterations%10==0:
            if GRAPH:
                # plt.clf()
                plt.subplot(1, 4, 1)
                # plt.ion()
                if optimiseGL:
                    plt.title(f"Current Residual (GL) iteration={iterations}")
                    plt.imshow(
                        residual,
                        cmap="coolwarm",
                        vmin=radioSphere.mm2gl(-0.1),
                        vmax=radioSphere.mm2gl(0.1),
                    )
                else:
                    plt.title(f"Current Residual (mm) LUT: [-0.1, 0.1] iteration={iterations}")
                    plt.imshow(residual, cmap="coolwarm", vmin=-radiiMM[sphere], vmax=radiiMM[sphere])
                plt.pause(0.01)

            # For each direction in X, Y, Z
            for i in range(3):
                # Perturb just one direction
                tmp = xyzMM[sphere].copy()
                tmp[i] += perturbationMM[i]
                # Here the ROI parameters are the same as the undisturbed sphere to guarantee the same size
                #   projection being returned
                perturbedProjectionMM = radioSphere.projectSphere.projectSphereMM(
                    numpy.array([tmp]),
                    numpy.array([radiiMM[sphere]]),
                    sourceDetectorDistMM=sourceDetectorDistMM,
                    pixelSizeMM=pixelSizeMM,
                    detectorResolution=detectorResolution,
                    ROIcentreMM=xyzMM[sphere].copy(),
                    ROIradiusMM=radiiMM[sphere] * 1.2 * displacementFactor[sphere],
                    displacementsMM=displacementMMSphere,
                    projector=projector,
                    focalSpotSize=focalSpotSize,
                    scattering=scattering
                    # blur=blur)
                )
                # apply kernel to each ROI
                if motionKernel:
                    if motionKernel[sphere] is not None:
                        perturbedProjectionMM = scipy.ndimage.convolve(perturbedProjectionMM, motionKernel[sphere])

                if blur:
                    if blur[sphere] is not None:
                        perturbedProjectionMM = scipy.ndimage.gaussian_filter(perturbedProjectionMM, sigma=blur[sphere])

                if optimiseGL:
                    perturbedProjection = radioSphere.mm2gl(perturbedProjectionMM, calib=optimiseGLcalib)
                else:
                    perturbedProjection = perturbedProjectionMM

                sensXYZ[i] = sphereRefProjection - perturbedProjection

                if GRAPH:
                    plt.subplot(1, 4, 2 + i)
                    if optimiseGL:
                        plt.title(
                            f"Sens{'XYZ'[i]} (GL) LUT: [{radioSphere.mm2gl(-2)}, {radioSphere.mm2gl(2)}]\nSphere = {sphere}, Perturbation {perturbationMM[i]} mm"
                        )
                        plt.imshow(
                            sensXYZ[i],
                            cmap="coolwarm",
                            vmin=radioSphere.mm2gl(-2),
                            vmax=radioSphere.mm2gl(2),
                        )
                    else:
                        plt.title(
                            f"Sens{'XYZ'[i]} (mm) LUT: [-2, 2]\nSphere = {sphere}, Perturbation {perturbationMM[i]} mm"
                        )
                        plt.imshow(sensXYZ[i], cmap="coolwarm", vmin=-2, vmax=2)
            # for making sensivitiy single particle figure in paper uncomment the next line
            # numpy.save('cache/sensXYZ.npy', sensXYZ)

            if GRAPH:
                plt.pause(1e-6)
                # plt.show()

            # Reset step which will be filled with the step in XZY combining weighted combination of sensitivity fields
            #   N.B. not to be confused with perturbationMM, which for now is not changed during iterations
            # step = numpy.zeros(3)

            LSQret = scipy.optimize.least_squares(
                optimiseMe,
                [1.0, 1.0, 1.0],
                args=[residualCropSphere, sensXYZ],
                verbose=False,
                method="lm",
                diff_step=1,
            )
            if LSQret["success"] == True:
                # print('LSQ Success!')
                # print(LSQret['x'])
                # OS 25/10/21:
                # update spheres position
                xyzMM[sphere] -= LSQret["x"] * perturbationMM
                # OS 24/03/22:
                # check if current position falls inside the limits, if not force it back
                if limitsX:
                    if xyzMM[sphere, 0] > minZoom:
                        # print("\nHit MIN zoom!")
                        xyzMM[sphere, 0] = minZoom
                    if xyzMM[sphere, 0] < maxZoom:
                        # print("\nHit MAX zoom!")
                        xyzMM[sphere, 0] = maxZoom
            else:
                print("LSQ failed to converge")

            if verbose > 1:
                # print("\t\tstep:\t",step)
                print("\t\tpos:\t", xyzMM[sphere])

        ### End optimisation iterations

        #### Now a soothing  DEM step can be applied to the current updated XYZ positions
        # if DEMcorr:
        # import radioSphere.DEM
        # xyzMMnew, k = radioSphere.DEM.DEM_step(xyzMM, radiiMM, k=0.1)
        ##if verbose > 0: print("   DEM changed positions by: ", numpy.linalg.norm(xyzMM-xyzMMnew), end='')
        # xyzMM = xyzMMnew

        if DEMcorr:
            # OS 24/03/22:
            # check for overlaps and apply DEM cor
            from scipy.spatial.distance import cdist

            nSpheres = len(xyzMM)
            delta = cdist(xyzMM, xyzMM) - 2 * radiiMM[0]
            diag = numpy.eye(nSpheres).astype("bool")

            if any(delta[~diag] < 0):
                import radioSphere.DEM

                xyzMMDEM, k = radioSphere.DEM.DEM_step(xyzMM, radiiMM, k=DEMparameter)
                if verbose > 1:
                    print("   DEM changed positions by: ", numpy.linalg.norm(xyzMM - xyzMMDEM), end="")
                xyzMM = xyzMMDEM

        # OS 30/05/22:
        # harsh regularisation in time?
        if regularisation:
            distX = numpy.abs(xyzMM[:, 0] - xyzGuessesMM[:, 0])
            for pos in range(distX.shape[0]):
                if distX[pos] > regularisationThreshold:
                    xyzMM[pos, 0] = xyzGuessesMM[pos, 0]

        # OS 25/10/21
        # define dX as the norm of the displacement step, that's debatable
        dX = numpy.linalg.norm(xyzMM - xyzMMprev)
        # print(numpy.mean(numpy.mean(numpy.abs(xyzMM-xyzMMprev), axis=1)))

        # outputForFigure.append([numpy.linalg.norm(step),numpy.sqrt(numpy.sum(residualMM.flatten()**2))])
        # if verbose > 0: print("   |deltaMM|: ", numpy.linalg.norm(xyzMM-xyzMMprev), end='')
        if verbose > 0:
            print(f"  LSQ: {LSQret['x']} | |dMM|: {dX:0.5f}", end="\r")

        xyzMMprev = xyzMM.copy()

        if NDDEM_output:
            from radioSphere.DEM.nddem import write_dumpfile

            write_dumpfile(xyzMM, radiiMM, iterations)

        if showConvergence:
            # plt.figure(2)
            plt.ion()
            plt.semilogy(iterations, numpy.sqrt(numpy.sum(residual.flatten() ** 2)), "k.")
            plt.xlabel("Iterations")
            if optimiseGL:
                plt.ylabel("Sum of squared residuals (GL^2)")
            else:
                plt.ylabel("Sum of squared residuals (mm^2)")
            plt.pause(2)
            plt.show()

        iterations += 1

    # numpy.savetxt('./cache/optimiserSensitivityField.csv',outputForFigure,delimiter=',',header='DisplacementNorm,SquaredResidual')

    if verbose > 0:
        if dX <= minDeltaMM:
            # Check that we exited based on displacement
            print("\n\toptimiseSensitivityFields(): Got below {} in {} iterations".format(minDeltaMM, iterations))
        else:
            # Check that we exited based on displacement
            print("\n\toptimiseSensitivityFields(): hit max iterations ({})".format(iterations))

    plt.ioff()

    return xyzMM


def _optimiseSensitivityFieldsMultiProj(
    radioMM,
    xyzGuessesMM,
    radiiMM,
    transformationCentresMM,
    transformationMatrices,
    iterationsMax=20,
    minDeltaMM=0.01,
    perturbationMM=numpy.array([0.5, 0.5, 0.5]),
    sourceDetectorDistMM=100,
    pixelSizeMM=0.1,
    detectorResolution=[512, 512],
    solver="leastsquares",
    verbose=0,
    DEMcorr=False,
    GRAPH=False,
):
    """
    This function takes in a series of reference projection (radioMM) in mm and sphere positions
    and moves them around to minimise the residual as far as possible.
    The technique used is the calculation of a sensitivity field in x, y, z with a perturbation of the
    synthetic radiograph.
    This is done locally in a ROI around each particle, which avoids doing the projection for all pixels.

    Parameters
    ----------
        radioMM : 3D numpy array of floats
            N Projections of distance crossed in spheres in MM, where N is the number of different views

        xyzGuessesMM : 2D numpy array of floats
            Nx3 guesses for the positions of the particles in MM

        radiiMM : 1D numpy array of floats
            Particle radii for projection

        transformationCentresMM : Nx3 numpy array
            A tranformation centre (XYZ) for each projection

        transformationMatrices : Nx3x3 numpy array
            A 3x3 transformation matrix (XYZ) for each projection

        iterationsMax : int, optional
            Number of iterations to perform
            Default = 20

        minDeltaMM : float, optional
            If step size gets below this value, stop
            Default = 0.01

        perturbationMM : 3-component list of floats, optional
            Size of the perturbation step to compute the sensitivity field
            Default = (2.0, 0.5, 0.5)

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector
            Default = 100

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        detectorResolution : 2-component list of ints, optional
            Number of pixels height, width of detector
            Default = [512,512]

        projector : string, optional
            #Algorithm for the projector
            #Default = 'numba'

        solver : string, optional
            Way in which the sensitivity fields
            are combined to minimise residual.
            Options = 'homemade', 'leastsquares'
            Default = 'leastsquares'

        verbose : int, optional
            Print noisly? 0 = quiet except warning, 1=iterations, 2=everything
            Default = 1

        DEMcorr : bool, optional
            Perform a soft DEM correction between all iterations?
            Default = False

    Returns
    -------
        xzyMM : Corrected positions array
    """
    import radioSphere.projectSphere

    assert (
        len(radiiMM) == xyzGuessesMM.shape[0]
    ), "optimiseSensitivityFieldsMultiProj(): number of radii and sphere positions not the same"
    assert radioMM.shape[0] == transformationCentresMM.shape[0]
    assert radioMM.shape[0] == transformationMatrices.shape[0]
    if numpy.all(numpy.array(transformationCentresMM[0]) != numpy.array([0.0, 0.0, 0.0])):
        print(
            "optimiseSensitivityFieldsMultiProj(): master transformation centre is not zero, do you know what you're doing?"
        )
    if numpy.all(numpy.array(transformationMatrices[0]) != numpy.eye(3)):
        print(
            "optimiseSensitivityFieldsMultiProj(): master transformation matrix is not identity, do you know what you're doing?"
        )

    nProj = radioMM.shape[0]

    if verbose > 1:
        print("optimiseSensitivityFieldsMultiProj(): Number of projections = ", nProj)

    # initialise variables
    iterations = 0
    xyzMM = xyzGuessesMM.copy().astype("<f4")
    xyzMMprev = xyzGuessesMM.copy().astype("<f4")
    if verbose > 1:
        print("Initial pos:\n", xyzMM)

    step = numpy.array([numpy.inf, numpy.inf, numpy.inf])

    while iterations < iterationsMax and numpy.linalg.norm(step * perturbationMM) > minDeltaMM:
        if verbose > 0:
            print("\tIteration Number", iterations, end="")
        if verbose > 1:
            print("\tperturbationMM:\t", perturbationMM)
        if verbose > 1:
            print("\txyzMM:\t", xyzMM)

        # Generate radio stack with current guess of position (xyzMM)
        guessedRadioMM = numpy.zeros_like(radioMM)
        for n in range(nProj):
            guessedRadioMM[n] = radioSphere.projectSphere.projectSphereMM(
                xyzMM,
                radiiMM,
                sourceDetectorDistMM=sourceDetectorDistMM,
                pixelSizeMM=pixelSizeMM,
                detectorResolution=detectorResolution,
                transformationCentreMM=transformationCentresMM[n],
                transformationMatrix=transformationMatrices[n],
            )

        # update residual
        residualMM = radioMM - guessedRadioMM

        if GRAPH:
            for n in range(nProj):
                plt.subplot(nProj, 5, n * 5 + 1)
                plt.title("Proj {} Ref Projection (mm) LUT: [-2, 2]".format(n))
                plt.imshow(radioMM[n])

                plt.subplot(nProj, 5, n * 5 + 2)
                plt.title("Proj {} Current Residual (mm) LUT: [-2, 2]".format(n))
                plt.imshow(residualMM[n], cmap="coolwarm", vmin=-2, vmax=2)

        # Could easily parallelise here, these are all independent corrections
        for sphere in range(len(radiiMM)):

            if verbose > 1:
                print("\tSphere {} of {}".format(sphere + 1, len(radiiMM)))
            # Compute sensitivity fields for this perturbationMM -- this is the current virtual radiograph
            #   Perturbed by a given perturbationMM in x, y, z independently

            # This better be a list, since (due to different zooms) the ROIs might be different sizes for the different projections
            sensXYZall = []
            # This is a list of ROI residuals built here in order not to need to export limits and to avoid
            #   passing whole residual to the optimisation function below
            residualMMroi = []
            for n in range(nProj):
                # Compute sensitivity field only for this particle, this is debatable, so generate its reference projection
                # Since we're going to try to do this locally, let's pre-compute the limits on the detector
                limits = radioSphere.projectSphere.singleSphereToDetectorPixelRange(
                    xyzMM[sphere],
                    radiiMM[sphere] * 1.2,
                    radiusMargin=0.1,
                    sourceDetectorDistMM=sourceDetectorDistMM,
                    pixelSizeMM=pixelSizeMM,
                    detectorResolution=detectorResolution,
                    transformationCentreMM=transformationCentresMM[n],
                    transformationMatrix=transformationMatrices[n],
                )

                # Compute local reference projection for this sphere with ROI activated around the sphere
                sphereRefProjectionMM = radioSphere.projectSphere.projectSphereMM(
                    numpy.array([xyzMM[sphere]]),
                    numpy.array([radiiMM[sphere]]),
                    sourceDetectorDistMM=sourceDetectorDistMM,
                    pixelSizeMM=pixelSizeMM,
                    detectorResolution=detectorResolution,
                    ROIcentreMM=xyzMM[sphere].copy(),
                    ROIradiusMM=radiiMM[sphere] * 1.2,
                    transformationCentreMM=transformationCentresMM[n],
                    transformationMatrix=transformationMatrices[n],
                )

                # Pre-allocate sens field, since it's local it should be the same shape as sphereRefProjectionMM
                sensXYZ = numpy.zeros((3, sphereRefProjectionMM.shape[0], sphereRefProjectionMM.shape[1]), dtype=float)

                # For each direction in X, Y, Z
                for i in range(3):
                    # Perturb just one direction
                    tmp = xyzMM[sphere].copy()
                    tmp[i] += perturbationMM[i]
                    # Here the ROI parameters are the same as the undisturbed sphere to guarantee the same size
                    #   projection being returned
                    perturbedProjectionMM = radioSphere.projectSphere.projectSphereMM(
                        numpy.array([tmp]),
                        numpy.array([radiiMM[sphere]]),
                        sourceDetectorDistMM=sourceDetectorDistMM,
                        pixelSizeMM=pixelSizeMM,
                        detectorResolution=detectorResolution,
                        ROIcentreMM=xyzMM[sphere].copy(),
                        ROIradiusMM=radiiMM[sphere] * 1.2,
                        transformationCentreMM=transformationCentresMM[n],
                        transformationMatrix=transformationMatrices[n],
                    )
                    sensXYZ[i] = sphereRefProjectionMM - perturbedProjectionMM

                # Append sens field and residual ROI to lists for optimisation
                sensXYZall.append(sensXYZ)
                residualMMroi.append(residualMM[n, limits[0, 0] : limits[0, 1], limits[1, 0] : limits[1, 1]])

            if GRAPH:
                for n in range(nProj):
                    for i in range(3):
                        plt.subplot(nProj, 5, n * 5 + 3 + i)
                        plt.title(
                            "Proj {} Sens{} (mm) LUT: [-2, 2]\nSphere = {}, Perturbation {} mm".format(
                                n, "XYZ"[i], sphere, perturbationMM[i]
                            )
                        )
                        plt.imshow(sensXYZall[n][i], cmap="coolwarm", vmin=-2, vmax=2)
                plt.show()

            # Reset step which will be filled with the step in XZY combining weighted combination of sensitivity fields
            #   N.B. not to be confused with perturbationMM, which for now is not changed during iterations
            step = numpy.zeros(3)
            if solver == "homemade":
                # mask = numpy.where(numpy.abs(residualMM) > 0.01)
                # for i in range(3):
                # tmp = residualMM / sensXYZ[i]

                # step[i] = -1.0 * numpy.mean(tmp[mask][numpy.isfinite(tmp[mask])])
                # xyzMM[sphere][i] += step[i] * perturbationMM[i]
                # if GRAPH:
                # plt.subplot(2,4,4+i+2)
                # plt.imshow(tmp, cmap='coolwarm', vmin=-5, vmax=5)
                # plt.title("Step = {}".format(step[i]))
                # if verbose: print("step:\t",step)
                # if verbose: print("pos:\t",xyzMM[sphere])
                pass

            elif solver == "leastsquares":
                # attempt to find weights a, b, c for the x, y, z sensitivity fields with leastsquares
                import scipy.optimize

                def optimiseMe(weights, residualMMroi, sensXYZall):
                    # print("optimiseMe(): weights = ", weights)
                    assert len(residualMMroi) == len(sensXYZall)

                    # Add a series of 1D errors for each radio
                    output = []
                    for n in range(len(residualMMroi)):
                        output = numpy.hstack(
                            [
                                output,
                                numpy.ravel(
                                    residualMMroi[n]
                                    - weights[0] * sensXYZall[n][0]
                                    - weights[1] * sensXYZall[n][1]
                                    - weights[2] * sensXYZall[n][2]
                                ),
                            ]
                        )
                    return output

                LSQret = scipy.optimize.least_squares(
                    optimiseMe,
                    [
                        1.0,
                        1.0,
                        1.0,
                    ],  # this is step, i.e., the *weights* for the different perturbations, they are not in MM
                    args=[residualMMroi, sensXYZall],
                    verbose=False,
                    method="lm",
                    diff_step=1.0,
                )
                if LSQret["success"] == True:
                    # print('LSQ Success!')
                    step = LSQret["x"]
                    for i in range(3):
                        xyzMM[sphere][i] -= step[i] * perturbationMM[i]
                else:
                    print("LSQ failed to converge")

                if verbose > 1:
                    print("\t\tstep:\t", step)
                    print("\t\tpos:\t", xyzMM[sphere])

            else:
                print("optimiseSensitivityFieldsMultiProj(): Don't know this solver")
                return

        ### Now a soothing  DEM step can be applied to the current updated XYZ positions
        if DEMcorr:
            import radioSphere.DEM

            xyzMMnew = radioSphere.DEM.DEM_step(xyzMM, radiiMM)
            if verbose > 0:
                print(
                    "   DEM changed positions by: {:0.3f}mm".format(numpy.linalg.norm(xyzMM - xyzMMnew)),
                    end="",
                )
            xyzMM = xyzMMnew

        if GRAPH:
            plt.show()

        # if verbose > 0: print("   |deltaMM|: ", numpy.linalg.norm(xyzMM-xyzMMprev))
        if verbose > 0:
            print("   |deltaMM|: {:0.3f}".format(numpy.linalg.norm(step * perturbationMM)))

        xyzMMprev = xyzMM.copy()

        iterations += 1

    if verbose > 0:
        if numpy.linalg.norm(step * perturbationMM) <= minDeltaMM:
            # Check that we exited based on displacement
            print(
                "\toptimiseSensitivityFieldsMultiProj(): Got below {} in {} iterations".format(minDeltaMM, iterations)
            )
        else:
            # Check that we exited based on displacement
            print("\toptimiseSensitivityFieldsMultiProj(): hit max iterations ({})".format(iterations))

    return xyzMM
