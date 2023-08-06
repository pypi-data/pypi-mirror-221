import sys

if "cupy" in sys.modules:
    import cupy as xp
else:
    import numpy as xp

import scipy.ndimage


def projectAgnostic0(sourceDetectorDistMM, radiiMM, detHorizPosMM, detVertPosMM, spheres, projectionXmm, scattering):
    dtype = xp.float32
    sourceDetectorDistMM = sourceDetectorDistMM.astype(dtype)
    detVertPosMM = detVertPosMM.astype(dtype)
    detHorizPosMM = detHorizPosMM.astype(dtype)
    radiiMM = radiiMM.astype(dtype)
    spheres = spheres.astype(dtype)
    # projectionXmm = projectionXmm.astype(dtype)

    radiiMMSquare = radiiMM**2  # radius of particles squared
    Z, Y = xp.meshgrid(
        detHorizPosMM, detVertPosMM, indexing="ij"
    )  # 2D arrays of X and Y values at every detector pixel
    lines = xp.empty(
        [len(detHorizPosMM), len(detVertPosMM), 3]
    )  # vector from origin to each pixel on the detector panel
    lines[:, :, 0] = sourceDetectorDistMM
    lines[:, :, 1] = Y
    lines[:, :, 2] = Z
    magnitude = xp.sqrt(xp.sum(lines**2, axis=2))  # magnitude of each vector
    for i in range(3):
        lines[:, :, i] /= magnitude  # make unit vectors
    with xp.errstate(invalid="ignore"):
        for i, sphere in enumerate(spheres):
            c = xp.sum(sphere**2)  # norm squared of the distance from the origin to the centre of the sphere
            length = 2.0 * xp.sqrt(xp.dot(lines, sphere) ** 2 - c + radiiMMSquare[i])
            # print(length)
            length[xp.isnan(length)] = 0.0
            projectionXmm += length
    # return projectionXmm


def projectAgnostic1(
    sourceDetectorDistMM,
    radiiMM,
    detHorizPosMM,
    detVertPosMM,
    spheres,
    projectionXmm,
    scattering=0,
    focalSpotSize=0,
    step=1000,
):
    dtype = xp.float32
    sourceDetectorDistMM = sourceDetectorDistMM.astype(dtype)
    detVertPosMM = detVertPosMM.astype(dtype)
    detHorizPosMM = detHorizPosMM.astype(dtype)
    radiiMM = radiiMM.astype(dtype)
    spheres = spheres.astype(dtype)
    # projectionXmm = projectionXmm.astype(dtype)

    radiiMMSquare = radiiMM**2  # radius of particles squared
    Z, Y = xp.meshgrid(
        detHorizPosMM, detVertPosMM, indexing="ij"
    )  # 2D arrays of X and Y values at every detector pixel
    lines = xp.empty(
        [len(detHorizPosMM), len(detVertPosMM), 3]
    )  # vector from origin to each pixel on the detector panel
    magnitude = xp.sqrt(Y**2 + Z**2 + sourceDetectorDistMM**2)  # magnitude of each vector
    lines[:, :, 0] = sourceDetectorDistMM / magnitude
    lines[:, :, 1] = Y / magnitude
    lines[:, :, 2] = Z / magnitude

    dY = detHorizPosMM[1] - detHorizPosMM[0]
    dZ = detVertPosMM[1] - detVertPosMM[0]
    cs = xp.sum(spheres**2, axis=1)

    with xp.errstate(invalid="ignore"):
        for i, sphere in enumerate(spheres):

            # c = cp.sum(sphere**2) # norm squared of the distance from the origin to the centre of the sphere
            length = 2.0 * xp.sqrt(
                (lines[:, :, 0] * sphere[0] + lines[:, :, 1] * sphere[1] + lines[:, :, 2] * sphere[2]) ** 2
                - cs[i]
                + radiiMMSquare[i]
            )
            # print(length)
            length[xp.isnan(length)] = 0.0

            if scattering > 0:
                reduced_length = (1 - scattering) * length

                # now work out which pixels need to be scattered
                incident = xp.argwhere(length > 0)
                # print(f'{len(incident)//step} scattering events to process')
                # print(incident)
                scattered_length = xp.zeros_like(length)
                for j in incident[::step]:  # skip many incident pixels to speed things up a bit
                    scattered_length += (
                        scattering
                        * length[j[0], j[1]]
                        / (
                            4
                            * xp.pi
                            * ((sourceDetectorDistMM - sphere[0]) ** 2 + (sphere[1] - Y) ** 2 + (sphere[2] - Z) ** 2)
                        )
                        * dY
                        * dZ
                        * step
                        * step
                    )  # NOTE: SHOULD BE IN I, NOT MM!!!!

                # print(f'    scattered: {xp.sum(scattered_length)}')
                # print(f'not scattered: {xp.sum(reduced_length)}')
                # print(f'ratio: {xp.sum(scattered_length)/xp.sum(length)}')
                length = scattered_length + reduced_length

            if focalSpotSize > 0:
                penumbra_widthMM = focalSpotSize[0] * (sourceDetectorDistMM[0] - sphere[0]) / sphere[0]
                penumbra_widthPX = penumbra_widthMM / dY  # mm / (mm/px)
                # print(penumbra_widthPX)
                length = scipy.ndimage.gaussian_filter(length, sigma=penumbra_widthPX)
            projectionXmm += length
    # return projectionXmm


if __name__ == "__main__":
    import CProjector
    import matplotlib.pyplot as plt
    import time
    import numpy as np

    sourceDetectorDistMM = np.array([100], dtype="<f4")
    N = 20
    W = H = 1000
    spheres = 15 * (np.random.rand(N, 3) - 0.5)
    spheres[:, 0] += 90

    projectionXmm = np.zeros([W, H], dtype="<f4")
    detVertPosMM = np.linspace(-10, 10, H, dtype="<f4")
    detHorizPosMM = np.linspace(-10, 10, W, dtype="<f4")
    spheres = spheres.astype("<f4")
    radiiMM = np.ones([N], dtype="<f4")
    tic = time.time()
    print(spheres)
    CProjector.project_func(sourceDetectorDistMM, radiiMM, detVertPosMM, detHorizPosMM, spheres, projectionXmm)
    toc = time.time()
    print("c++ version took " + str(toc - tic) + "s for " + str(N) + " particles")

    for i in range(2):
        if i == 0:
            if "cupy" in sys.modules:
                import cupy as xp
            else:
                print("cupy not installed, skipping")
                continue
        elif i == 1:
            import numpy as xp

        out0 = out1 = xp.zeros([W, H])
        tic = time.time()
        projectAgnostic0(sourceDetectorDistMM, radiiMM, detHorizPosMM, detVertPosMM, spheres, out0)
        toc = time.time()
        projectAgnostic1(sourceDetectorDistMM, radiiMM, detHorizPosMM, detVertPosMM, spheres, out1)
        tac = time.time()
        print(str(i) + "th version took " + str(toc - tic) + "s for method 0 for " + str(N) + " particles")
        print(str(i) + "th version took " + str(tac - toc) + "s for method 1 for " + str(N) + " particles")
        if i == 0:
            out0 = xp.asnumpy(out0)
            out1 = xp.asnumpy(out1)
        print(
            "Errors were "
            + str(np.mean(np.abs(out0 - projectionXmm)))
            + " and "
            + str(np.mean(np.abs(out1 - projectionXmm)))
        )

    GRAPH = True
    if GRAPH:
        plt.subplot(221)
        plt.pcolormesh(detHorizPosMM, detVertPosMM, projectionXmm, shading="auto")
        plt.colorbar()
        plt.subplot(223)
        plt.pcolormesh(detHorizPosMM, detVertPosMM, out0, shading="auto")
        plt.colorbar()
        plt.subplot(224)
        plt.pcolormesh(detHorizPosMM, detVertPosMM, out1, shading="auto")
        plt.colorbar()
        plt.show()
    #

    # out2 = cp.zeros([W,H],dtype='<f4')
    # # sourceDetectorDistMM = sourceDetectorDistMM
    # spheres = cp.array(spheres,dtype='<f4')
    # detVertPosMM = cp.array(detVertPosMM,dtype='<f4')
    # detHorizPosMM = cp.array(detHorizPosMM,dtype='<f4')
    # tic = time.time()
    # out2 = projectCupy(sourceDetectorDistMM, radius, detVertPosMM, detHorizPosMM, spheres, out2)
    # toc = time.time()
    # print('Cupy version took ' + str(toc - tic) + 's for ' + str(N) + ' particles')
    #
    # # But did we calculate the right values??
    # # print(out0)
    # # print(projectionXmm)
    # # print(out2)
    # # print(np.mean(np.abs(out0-projectionXmm)))
    # print(np.mean(np.abs(cp.asnumpy(out2)-projectionXmm)))
