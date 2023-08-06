import os
import sys
import numpy
import matplotlib.pyplot as plt
import radioSphere
from tqdm import tqdm, trange
from scipy.spatial.transform import Rotation as R


def generate_shelled_particle(majorRadiusMM, sizeRatio, areaFillingFraction=0.5, verbose=True, fillMode="simple"):
    """
    Use a brute force method to place spheres of one size (majorRadius * sizeRatio) around a sphere of another size (majorRadius). Keep adding particles until a certain fraction of the surface area (ish) is filled. Return the positions and radii of all of the spheres.
    """
    cacheName = f"{majorRadiusMM}_{sizeRatio}_{areaFillingFraction}"

    if os.path.exists("cache/pos_" + cacheName + ".npy"):
        pos = numpy.load("cache/pos_" + cacheName + ".npy")
        radii = numpy.load("cache/radii_" + cacheName + ".npy")
    else:
        # derived quantities
        minorRadiusMM = majorRadiusMM * sizeRatio

        # store location and radii, starting with major particle at the origin
        pos = [[0, 0, 0]]
        radii = [majorRadiusMM]

        if sizeRatio > 0:  # do not add any shell particles if sizeRatio is zero
            if fillMode == "simple":
                # simple version - just calculate surface area of sphere passing through small sphere centres and fill a certain fraction of that
                nShellParticles = int(
                    areaFillingFraction
                    * (4 * numpy.pi * (majorRadiusMM + minorRadiusMM) ** 2)
                    / (numpy.pi * minorRadiusMM**2)
                )
            elif fillMode == "Rogers":
                # from https://www.cambridge.org/core/journals/mathematika/article/covering-a-sphere-with-spheres/36A4272740F04D37381C8E83CF5A6AC0
                # using last equation, in their notation:
                # R is big sphere radius
                # small sphere radius is 1
                n = 3  # the dimension
                e = 2.718281  # euler's number
                nShellParticles = 4 * e * n * numpy.sqrt(n) / numpy.log(n) * (n * numpy.log(n) + n)
                sys.exit("NOT IMPLEMENTED YET")

            for i in trange(nShellParticles, leave=False):
                overlapping = True
                j = 0

                while overlapping:
                    x = 2 * (numpy.random.rand(3) - 0.5)  # a randomly generated vector
                    x /= numpy.linalg.norm(x)  # now a randomly generated unit vector
                    x *= majorRadiusMM + minorRadiusMM  # and now with the correct length

                    overlapping = False
                    for p in pos[1:]:
                        if numpy.linalg.norm(x - p) < 2 * minorRadiusMM:
                            overlapping = True
                            break

                    j += 1
                    if verbose:
                        print(i, j, nShellParticles)

                    if j > 1e4:
                        x = None
                        break  # give up

                if x is not None:
                    pos.append(x)
                    radii.append(minorRadiusMM)

        numpy.save("cache/pos_" + cacheName + ".npy", pos)
        numpy.save("cache/radii_" + cacheName + ".npy", radii)
    return pos, radii


if __name__ == "__main__":
    # control parameters
    majorRadiusMM = 1.0
    sizeRatios = numpy.logspace(0, -2, 11)
    relativeResolutions = numpy.logspace(0, 2, 11)
    areaFillingFraction = 0.5
    numRepeats = 100
    # chis = numpy.linspace(0,2,11)
    chis = [0]

    proj_fig = plt.figure(1, figsize=[len(relativeResolutions), len(sizeRatios)])
    proj_fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    fx_fig = plt.figure(2, figsize=[len(relativeResolutions), len(sizeRatios)])
    fx_fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    summary_fig = plt.figure(3)
    

    peakIndicatorFunctions = numpy.zeros([len(sizeRatios), len(relativeResolutions), numRepeats])

    for chi in tqdm(chis):
        plt.figure(summary_fig)
        plt.clf()
        sum_ax = summary_fig.add_subplot()
        sum_ax.set_xlabel("Resolution (px/radius)")
        sum_ax.set_xscale("log")
        sum_ax.set_yscale("log")
        sum_ax.set_ylabel("Size ratio (-)")

        for i, sizeRatio in enumerate(tqdm(sizeRatios, leave=False)):
            pos, radii = generate_shelled_particle(majorRadiusMM, sizeRatio, areaFillingFraction, verbose=False)
            minorRadiusMM = majorRadiusMM * sizeRatio
            # effectiveRadiusMM = majorRadiusMM + 2 * minorRadiusMM
            # effectiveRadiusMM = majorRadiusMM + minorRadiusMM # somehow accounting for only partial filling of the outer layer?
            effectiveRadiusMM = majorRadiusMM + chi * minorRadiusMM # somehow accounting for only partial filling of the outer layer?

            for j, relativeResolution in enumerate(tqdm(relativeResolutions, leave=False)):
                pixelSizeMM = majorRadiusMM / relativeResolution

                detectorResolution = [
                    int((2 * (majorRadiusMM + 2*minorRadiusMM)) / pixelSizeMM) + 1,
                    int((2 * (majorRadiusMM + 2*minorRadiusMM)) / pixelSizeMM) + 1,
                    # int((3 * effectiveRadiusMM) / pixelSizeMM),
                    # int((3 * effectiveRadiusMM) / pixelSizeMM),
                ]

                psi = radioSphere.projectSphere.projectSphereMM(
                    numpy.array([pos[0]]),
                    numpy.array([effectiveRadiusMM]),
                    sourceDetectorDistMM=numpy.inf,
                    pixelSizeMM=pixelSizeMM,
                    detectorResolution=detectorResolution,
                )

                for k in tqdm(range(numRepeats), leave=False):

                    r = R.from_euler(
                        "zyx",
                        [360 * numpy.random.rand(), 360 * numpy.random.rand(), 360 * numpy.random.rand()],
                        degrees=True,
                    )

                    rotated_pos = r.apply(pos)

                    # project all particles
                    projectionMM = radioSphere.projectSphere.projectSphereMM(
                        numpy.array(rotated_pos),
                        numpy.array(radii),
                        sourceDetectorDistMM=numpy.inf,
                        pixelSizeMM=pixelSizeMM,
                        detectorResolution=detectorResolution,
                    )

                    # now apply radiosphere in a parallel geometry and look for peak value in the centre of the particle
                    fx = radioSphere.detectSpheres.tomopack(
                        projectionMM,
                        psi,
                        maxIterations=50,
                        l=0.5,
                        projector="C",
                        scattering=0.0,
                        kTrustMethod="iterative",
                        epsilon=1,
                        kTrustRatio=0.75,
                        kTrust=None,
                        verbose=False,
                        graphShow=False,
                    )

                    peakIndicatorFunctions[i, j, k] = fx.max()

                ax = proj_fig.add_subplot(len(sizeRatios), len(relativeResolutions), i * len(relativeResolutions) + j + 1)
                ax.imshow(projectionMM)
                ax.set_xticks([])
                ax.set_yticks([])

                ax = fx_fig.add_subplot(len(sizeRatios), len(relativeResolutions), i * len(relativeResolutions) + j + 1)
                ax.imshow(fx, vmin=0, vmax=1)
                ax.set_xticks([])
                ax.set_yticks([])

                meanPeakIndicatorFunction = numpy.mean(peakIndicatorFunctions, axis=2)
                s = sum_ax.pcolormesh(relativeResolutions, sizeRatios, meanPeakIndicatorFunction, shading="nearest")

            if i == len(sizeRatios) - 1:
                cb = summary_fig.colorbar(s)
                cb.set_label("Mean peak indicator function (-)")

        if not os.path.exists("im/"): os.mkdir('im')

        proj_fig.savefig(f"im/proj_{chi:0.2f}.png", dpi=100)
        fx_fig.savefig(f"im/fx_{chi:0.2f}.png", dpi=100)
        summary_fig.savefig(f"im/summary_{chi:0.2f}.png")
