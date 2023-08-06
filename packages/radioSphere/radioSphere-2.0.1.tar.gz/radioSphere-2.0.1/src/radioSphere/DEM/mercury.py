import numpy
import tifffile
import sys, os

# sys.path.append(os.path.join(os.path.dirname(__file__), "projectSphereC.cython"))
import radioSphere.projectSphere
import csv


def getParticlesFromMercury(mercuryFileName, timeStepDEM):
    with open(mercuryFileName) as f:
        frame = 0
        reader = csv.reader(f, delimiter=" ")
        for i, line in enumerate(reader):
            if i == 0:
                num_particles = int(line[0])
                loc = numpy.zeros([num_particles, 3], dtype="<f4")
                radii = numpy.zeros([num_particles], dtype="<f4")
            elif i % (num_particles + 1) == 0:
                frame += 1
                # print('Made ' + str(frame).zfill(3) + ' frames', end='\r')
                if frame > timeStepDEM:
                    break
            elif frame == timeStepDEM:
                pt = i % (num_particles + 1) - 1
                loc[pt, 0] = numpy.double(line[0])  # x
                loc[pt, 1] = numpy.double(line[1])  # y
                loc[pt, 2] = numpy.double(line[2])  # z
                radii[pt] = numpy.double(line[6])  # radius
    return loc, radii


def generateSampledRadiographFromMercuryData(
    mercuryFileName,
    timeStepDEM,
    halfConeBeamAngleDegrees,
    pixelSizeMM,
    detectorResolution,
    samplingThicknessXMM=None,
    samplingTransverseDistanceMM=None,
    samplingFraction=None,
    zoomLevel=2.0,
    saveImage=False,
    GRAPH=False,
):
    # Load data
    spheres, radii = getParticlesFromMercury(mercuryFileName, timeStepDEM)
    spheresMM = spheres * 1000
    radiiMM = radii * 1000

    if samplingThicknessXMM is not None:
        # just sample in the middle samplingThicknessXMM in the X direction
        sampled = (spheresMM[:, 0] > -samplingThicknessXMM / 2.0) * (
            spheresMM[:, 0] < samplingThicknessXMM / 2.0
        )
    if samplingFraction is not None:
        # sampling_parameter is volume fraction of solids (i.e. fraction of spheres in packing)
        sampled = numpy.random.choice(len(spheresMM), int(samplingFraction * len(spheresMM)))
    spheresMM = spheresMM[sampled, :]
    radiiMM = radiiMM[sampled]

    if samplingTransverseDistanceMM is not None:
        sampled = (
            numpy.sqrt(spheresMM[:, 1] ** 2 + spheresMM[:, 2] ** 2) < samplingTransverseDistanceMM
        )
        spheresMM = spheresMM[sampled, :]
        radiiMM = radiiMM[sampled]

    sourceObjectDistMM = radiiMM[0] / numpy.tan(numpy.radians(halfConeBeamAngleDegrees))
    # spheresMM[:,0] -= spheresMM[:,0].mean()
    spheresMM[:, 0] += sourceObjectDistMM  # move to sample location

    pixelsPerDiameterZoomed = radiiMM * 2 / (pixelSizeMM / zoomLevel)
    sourceDetectorDistMM = zoomLevel * sourceObjectDistMM

    radioMM = radioSphere.projectSphere.projectSphereMM(
        spheresMM,
        radiiMM,
        detectorResolution=detectorResolution,
        pixelSizeMM=pixelSizeMM,
        sourceDetectorDistMM=sourceDetectorDistMM,
    )

    if GRAPH:
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

        # Functions from @Mateen Ulhaq and @karlo
        def set_axes_equal(ax: plt.Axes):
            limits = numpy.array(
                [
                    ax.get_xlim3d(),
                    ax.get_ylim3d(),
                    ax.get_zlim3d(),
                ]
            )
            origin = numpy.mean(limits, axis=1)
            radius = 0.5 * numpy.max(numpy.abs(limits[:, 1] - limits[:, 0]))
            _set_axes_radius(ax, origin, radius)

        def _set_axes_radius(ax, origin, radius):
            x, y, z = origin
            ax.set_xlim3d([x - radius, x + radius])
            ax.set_ylim3d([y - radius, y + radius])
            ax.set_zlim3d([z - radius, z + radius])

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(spheresMM[:, 0], spheresMM[:, 1], spheresMM[:, 2], marker="o", s=200)
        ax.set_box_aspect([1, 1, 1])  # IMPORTANT - this is the new, key line
        # ax.set_proj_type('ortho') # OPTIONAL - default is perspective (shown in image above)
        set_axes_equal(ax)  # IMPORTANT - this is also required        plt.show()
        plt.show()

    if saveImage:
        # print('saving')
        foldername = (
            "data/DEM_projected/half-cone-beam-angle-"
            + str(halfConeBeamAngleDegrees)
            + "/resolution-"
            + str(pixelsPerDiameterZoomed)
            + "/thickness-"
            + str(numberOfParticleLayers)
            + "/"
        )
        if not os.path.exists(foldername):
            os.makedirs(foldername)
        tifffile.imwrite(foldername + str(tstep).zfill(4) + ".tiff", radioXmm)

    return radioMM, spheresMM, radiiMM, sourceObjectDistMM


if __name__ == "__main__":
    fname = "./data/lees_edwards_nu_0.6_R_1_M_1.data"
    # Constant system parameters
    particleDiameterMM = 1  # Set in DEM
    pixelSizeMM = 0.1
    detectorResolution = [512, 512]
    maximumAspectRatio = 1.5

    for tstep in range(1):
        for halfConeBeamAngleDegrees in [1, 2, 3, 5, 10]:
            for numberOfParticleLayers in [0.01, 0.5, 1, 2, 5, 7, 10]:
                generate_radiograph_from_DEM(
                    fname,
                    tstep,
                    halfConeBeamAngleDegrees,
                    numberOfParticleLayers,
                    particleDiameterMM,
                    pixelSizeMM,
                    detectorResolution,
                    samplingMode="layers",
                )
