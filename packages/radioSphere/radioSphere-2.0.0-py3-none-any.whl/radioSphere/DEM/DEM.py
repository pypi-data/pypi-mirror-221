import numpy
from scipy.spatial.distance import cdist


def DEM_step(posMMin, radiiMM, k=0.01):
    """
    Lightweight DEM with assumption of same size spheres as mechanical regularisation

    Parameters
    ----------
        posMMin : Nx3 2D numpy array of floats
            xyz positions of spheres in mm, with the origin being the middle of the detector

        radiiMM : 1D numpy array of floats
            Particle radii for projection

        k : float, optional
            Stiffness and timestep wrapped into one
            Default = 0.01

    Returns
    -------
        posMM : output positions
    """

    posMM = posMMin.copy()

    if radiiMM.min() != radiiMM.max():
        print("DEM.DEM_step(): WARINING I assume all radii are the same, taking first one")
    # k = 0.1 # stiffness and timestep wrapped into one
    nSpheres = len(posMM)
    delta = cdist(posMM, posMM) - 2 * radiiMM[0]  # assuming all radii the same
    diag = numpy.eye(nSpheres).astype("bool")

    # detect overlaps and apply DEM regularisation only for these
    while any(delta[~diag] < 0):
        for i in range(0, nSpheres):
            for j in range(i + 1, nSpheres):
                if delta[i, j] < 0:
                    # print(i,j,i+j)
                    branchVector = posMM[i] - posMM[j]
                    F = -k * delta[i, j] * branchVector
                    posMM[i] += F
                    posMM[j] -= F
        delta = cdist(posMM, posMM) - 2 * radiiMM[0]
        k += 0.01

    return posMM, k


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # locMM = np.array([[0,0,0],
    #                   [0,1.8,0],
    #                   [0,0,3],
    #                   [3,0,0]])
    locMM = np.random.rand(50, 3) * 20
    print(len(locMM))
    radiiMM = 1.0 * np.ones(len(locMM))
    for t in range(100):
        locMM = DEM_step(locMM, radiiMM)
        plt.ion()
        plt.plot(locMM[:, 0], locMM[:, 1], ".")
        # plt.show()
        plt.pause(0.01)
    # print(locMM)
