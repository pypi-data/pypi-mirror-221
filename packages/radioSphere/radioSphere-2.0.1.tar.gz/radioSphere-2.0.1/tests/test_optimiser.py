"""
Simple tests to make sure everything works as expected.
The layout is as per python's unittest but right it should just
be executed, and all the `self.self.assertEqualEqual`s should pass.

If a new function is added it should be called at the bottom of the function

This file contains tests with a single sphere
"""
# import os
# import sys

import radioSphere

import numpy
import scipy.ndimage
import matplotlib.pyplot as plt

import unittest


class TestOptimiser(unittest.TestCase):
    def tearDown(self):
        try:
            pass
        except OSError:
            pass

    def test_optimisePositionsensitivityFields_oneSphere(self):
        print("\n\ntest_optimisePositionsensitivityFields_oneSphere(): Starting up")

        pos = numpy.array([[50, 0, 0]])
        rad = 2
        projMM = radioSphere.projectSphere.projectSphereMM(pos, numpy.array([rad]))

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost starting in the right place"
        )
        posOptimised1 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM, pos + numpy.array([0.0, 0.0, 0.0]), numpy.array([rad]), iterationsMax=1
        )
        for i in range(3):
            self.assertEqual(numpy.abs(pos[0][i] - posOptimised1[0][i]) < 0.1, True)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost with a +0.5 mm miss-guess"
        )
        posOptimised2 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM, pos + numpy.array([0.5, 0.5, 0.5]), numpy.array([rad]), iterationsMax=50
        )
        for i in range(3):
            self.assertEqual(numpy.abs(pos[0][i] - posOptimised2[0][i]) < 0.1, True)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost with a +1.0 mm miss-guess"
        )
        posOptimised3 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM, pos + numpy.array([-1, -1, -1]), numpy.array([rad]), iterationsMax=50
        )
        for i in range(3):
            self.assertEqual(numpy.abs(pos[0][i] - posOptimised3[0][i]) < 0.1, True)

        print("test_optimisePositionsensitivityFields_oneSphere(): Done")

    def test_optimisePositionsensitivityFields_threeSpheres(self):
        print("\n\ntest_optimisePositionsensitivityFields_threeSpheres(): Starting up")
        pos = numpy.array([[50, 0, 0], [50, 5, 0], [50, -5, 0]])
        rad = 2
        radArray = numpy.array([rad, rad, rad])
        projMM = radioSphere.projectSphere.projectSphereMM(pos, radArray)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost starting in the right place"
        )
        posOptimised1 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM, pos, radArray, iterationsMax=3, GRAPH=False
        )
        for j in range(pos.shape[0]):
            for i in range(3):
                self.assertEqual(numpy.abs(pos[j][i] - posOptimised1[j][i]) < 0.1, True)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost with a +-0.5 mm miss-guess"
        )
        posOptimised2 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM,
            pos - numpy.array([[-0.5, 0, +0.5], [+0.5, +0.5, +0.5], [-0.5, -0.5, 0]]),
            radArray,
            iterationsMax=50,
        )
        for j in range(pos.shape[0]):
            for i in range(3):
                self.assertEqual(numpy.abs(pos[j][i] - posOptimised2[j][i]) < 0.1, True)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost with a +-0.5 mm miss-guess and that DEM option doesn't mess things up if they're not touching"
        )
        posOptimised3 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM,
            pos - numpy.array([[-0.5, 0, +0.5], [+0.5, +0.5, +0.5], [-0.5, -0.5, 0]]),
            radArray,
            iterationsMax=50,
            DEMcorr=True,
        )
        for j in range(pos.shape[0]):
            for i in range(3):
                self.assertEqual(numpy.abs(pos[j][i] - posOptimised3[j][i]) < 0.1, True)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost with a +-0.5 mm miss-guess with DEM option"
        )
        pos = numpy.array([[50, 0, 0], [50, 4, 0], [50, -4, 0]])
        projMM = radioSphere.projectSphere.projectSphereMM(pos, radArray)
        posOptimised4 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM,
            pos - numpy.array([[-0.5, 0, +0.5], [+0.5, +0.5, +0.5], [-0.5, -0.5, 0]]),
            radArray,
            iterationsMax=50,
            DEMcorr=True,
        )
        for j in range(pos.shape[0]):
            for i in range(3):
                self.assertEqual(numpy.abs(pos[j][i] - posOptimised4[j][i]) < 0.1, True)

        print("test_optimisePositionsensitivityFields_threeSpheres(): Done")

    def test_optimisePositionsensitivityFields_TwentySpheres(self):
        print("\n\ntest_optimisePositionsensitivityFields_TwentySpheres(): Starting up")

        radMM = 2
        nSphere = 20
        cylDiamMM = 5

        # Load yade-generated data
        xyzr = numpy.genfromtxt(
            "./data/yade/cylinderDiam-{:0.3f}_sphereDiam-{:0.3f}_numberSpheres-{}.txt".format(
                cylDiamMM / 1000, radMM / 1000, nSphere
            )
        )
        pos = xyzr[:, 0:3] * 1000
        radArray = xyzr[:, -1] * 1000

        # zero mean
        pos -= numpy.mean(pos, axis=0)
        # Move in x-ray direction
        pos[:, 0] += 35
        projMM = radioSphere.projectSphere.projectSphereMM(pos, radArray)
        # plt.imshow(projMM)
        # plt.show()
        slaveCentreMM = [35, 0, 0]
        slaveTransformation = numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost starting in the right place"
        )
        posOptimised1 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM, pos, radArray, iterationsMax=10
        )
        for j in range(pos.shape[0]):
            for i in range(3):
                self.assertEqual(numpy.abs(pos[j][i] - posOptimised1[j][i]) < 0.1, True)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost with an small random max +-0.001 mm miss-guess no DEM"
        )
        posOptimised2 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM,
            pos + 0.001 * numpy.random.random((len(radArray), 3)),
            radArray,
            iterationsMax=25,
            verbose=1,
            DEMcorr=False,
        )

        print("test_optimisePositionsensitivityFields_TwentySpheres(): Done")

    def _test_optimisePositionsensitivityFields_TwentySpheres_with_background(self):
        print(
            "\n\ntest_optimisePositionsensitivityFields_TwentySpheres_with_background: Starting up"
        )

        radMM = 2
        nSphere = 20
        cylDiamMM = 5
        offset = [0.01, 0.02, -0.03]

        # Load yade-generated data
        xyzr = numpy.genfromtxt(
            "./data/yade/cylinderDiam-{:0.3f}_sphereDiam-{:0.3f}_numberSpheres-{}.txt".format(
                cylDiamMM / 1000, radMM / 1000, nSphere
            )
        )
        pos = xyzr[:, 0:3] * 1000
        radArray = xyzr[:, -1] * 1000

        # zero mean
        pos -= numpy.mean(pos, axis=0)
        # Move in x-ray direction
        pos[:, 0] += 35
        projMM = radioSphere.projectSphere.projectSphereMM(pos, radArray)
        x, y = numpy.meshgrid(numpy.arange(projMM.shape[0]), numpy.arange(projMM.shape[1]))
        projMM += offset[0] * x + offset[1] * y + offset[2]
        # plt.imshow(projMM)
        # plt.show()
        slaveCentreMM = [35, 0, 0]
        slaveTransformation = numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost starting in the right place"
        )
        posOptimised1 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM, pos, radArray, iterationsMax=10
        )
        for j in range(pos.shape[0]):
            for i in range(3):
                self.assertEqual(numpy.abs(pos[j][i] - posOptimised1[j][i]) < 0.1, True)

        print(
            "\tMaking sure sensitivity field optimiser doesn't get lost with an small random max +-0.001 mm miss-guess no DEM"
        )
        posOptimised2 = radioSphere.optimisePositions.optimiseSensitivityFields(
            projMM,
            pos + 0.001 * numpy.random.random((len(radArray), 3)),
            radArray,
            iterationsMax=25,
            verbose=1,
            DEMcorr=False,
        )

        print("test_optimisePositionsensitivityFields_TwentySpheres_with_background(): Done")

    # def test_optimiseSensitivityFieldsMultiProj_ThreeSpheres(self):
    # print("\n\ntest_optimiseSensitivityFieldsMultiProj_ThreeSpheres(): Starting up")
    # rad = 2
    # radArray = numpy.array([rad, rad, rad])
    # slaveCentreMM = [50,0,0]
    # slaveTransformation = numpy.array([[0, -1, 0],[1, 0, 0],[0, 0, 1]])

    ##print("\tMaking sure bi-proj sensitivity field optimiser doesn't get lost with a +-0.1 mm random miss-guess with DEM option, aligned in x in master image")

    ##pos = numpy.array([[50, 4, 0], [50, 0, 0], [50, -4, 0]])
    ###pos = numpy.array([[54, 0, 0], [50, 0, 0], [46, 0, 0]])
    ##projMMmaster = radioSphere.projectSphere.projectSphereMM(pos,
    ##radArray)
    ##projMMslave  = radioSphere.projectSphere.projectSphereMM(pos,
    ##radArray,
    ##transformationCentreMM=slaveCentreMM,
    ##transformationMatrix=slaveTransformation)

    ##posOptimised1 = radioSphere.optimisePositions.optimiseSensitivityFieldsMultiProj(numpy.array([projMMmaster, projMMslave]),
    ##pos+numpy.random.random((len(radArray), 3)),
    ##radArray,
    ##numpy.array([[0,0,0], slaveCentreMM]),
    ##numpy.array([numpy.eye(3), slaveTransformation]),
    ##iterationsMax=50,
    ##DEMcorr=True,
    ##GRAPH=False,
    ##verbose=1)
    ##for j in range(pos.shape[0]):
    ##for i in range(3):
    ##self.assertEqual(numpy.abs(pos[j][i] - posOptimised1[j][i]) < 0.1, True)

    # print("test_optimiseSensitivityFieldsMultiProj_ThreeSpheres(): Done")

    # def test_optimiseSensitivityFieldsMultiProj_TwentySpheres(self):
    # print("\n\ntest_optimiseSensitivityFieldsMultiProj_TwentySpheres(): Starting up")

    # radMM = 2
    # nSphere = 20
    # cylDiamMM = 5

    ## Load yade-generated data
    # xyzr = numpy.genfromtxt("./data/yade/cylinderDiam-{:0.3f}_sphereDiam-{:0.3f}_numberSpheres-{}.txt".format(cylDiamMM/1000, radMM/1000, nSphere))
    # pos      = xyzr[:, 0:3]*1000
    # radArray = xyzr[:, -1]*1000

    ## zero mean
    # pos -= numpy.mean(pos, axis=0)
    ## Move in x-ray direction
    # pos[:,0] += 35
    # projMM = radioSphere.projectSphere.projectSphereMM(pos, radArray)

    ## Set up second projection
    # slaveCentreMM = [35,0,0]
    # slaveTransformation = numpy.array([[0, -1, 0],[1, 0, 0],[0, 0, 1]])

    # projMMslave = radioSphere.projectSphere.projectSphereMM(pos,
    # radArray,
    # transformationCentreMM=slaveCentreMM,
    # transformationMatrix=slaveTransformation)

    ##plt.subplot(1,2,1)
    ##plt.imshow(projMM)
    ##plt.subplot(1,2,2)
    ##plt.imshow(projMMslave)
    ##plt.show()

    # print("\tMaking sure bi-proj sensitivity field optimiser doesn't get lost starting in the right place")
    # posOptimised1 = radioSphere.optimisePositions.optimiseSensitivityFieldsMultiProj(numpy.array([projMM, projMMslave]),
    # pos,
    # radArray,
    # numpy.array([[0,0,0], slaveCentreMM]),
    # numpy.array([numpy.eye(3), slaveTransformation]),
    # iterationsMax=5,
    # DEMcorr=True,
    # GRAPH=False,
    # verbose=1)
    # for j in range(pos.shape[0]):
    # for i in range(3):
    # self.assertEqual(numpy.abs(pos[j][i] - posOptimised1[j][i]) < 0.1, True)

    # for randomNoise in [0.01, 0.1, 0.2, 0.3]:
    # print("\tMaking sure bi-proj sensitivity field optimiser doesn't get lost with an small random max +-{} mm miss-guess no DEM".format(randomNoise))

    # posOptimisedN = radioSphere.optimisePositions.optimiseSensitivityFieldsMultiProj(  numpy.array([projMM, projMMslave]),
    # pos+randomNoise*numpy.random.random((len(radArray), 3)),
    # radArray,
    # numpy.array([[0,0,0], slaveCentreMM]),
    # numpy.array([numpy.eye(3), slaveTransformation]),
    # iterationsMax=50,
    # DEMcorr=True,
    # GRAPH=False,
    # verbose=1)
    # for j in range(pos.shape[0]):
    # for i in range(3):
    # self.assertEqual(numpy.abs(pos[j][i] - posOptimisedN[j][i]) < 0.1, True)

    # print("test_optimiseSensitivityFieldsMultiProj_TwentySpheres(): Done")

    def _test_optimiseSensitivityFieldsMultiProj_ManySpheres(self):
        print("\n\ntest_optimiseSensitivityFieldsMultiProj_ManySpheres(): Starting up")

        # Lists of:
        #   - radius
        #   - nSphere
        #   - cylDimeter
        #   - [randomNoisesLimits]
        #   - xPos
        parameters = [
            # [2, 20, 5, [0, 0.01, 0.1], 35],
            # [2, 50, 7, [0, 0.01, 0.1], 35],
            # [2, 60, 7, [0, 0.01, 0.1], 50],
            [2, 75, 8, [0, 0.01, 0.1], 50]
        ]

        for radMM, nSphere, cylDiamMM, randomNoises, xPos in parameters:
            # Load yade-generated data
            xyzr = numpy.genfromtxt(
                "./data/yade/cylinderDiam-{:0.3f}_sphereDiam-{:0.3f}_numberSpheres-{}.txt".format(
                    cylDiamMM / 1000, radMM / 1000, nSphere
                )
            )
            pos = xyzr[:, 0:3] * 1000
            radArray = xyzr[:, -1] * 1000

            # zero mean
            pos -= numpy.mean(pos, axis=0)
            # Move in x-ray direction
            pos[:, 0] += xPos
            projMM = radioSphere.projectSphere.projectSphereMM(pos, radArray)

            # Set up second projection
            slaveCentreMM = [xPos, 0, 0]
            slaveTransformation = numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

            projMMslave = radioSphere.projectSphere.projectSphereMM(
                pos,
                radArray,
                transformationCentreMM=slaveCentreMM,
                transformationMatrix=slaveTransformation,
            )

            if nSphere > 20:
                plt.subplot(1, 2, 1)
                plt.imshow(projMM)
                plt.subplot(1, 2, 2)
                plt.imshow(projMMslave)
                plt.show()

            for randomNoise in randomNoises:
                print(
                    "\tMaking sure bi-proj sensitivity field optimiser converges with {} spheres and small random max +-{} mm miss-guess with DEM".format(
                        nSphere, randomNoise
                    )
                )

                posOptimisedN = radioSphere.optimisePositions._optimiseSensitivityFieldsMultiProj(
                    numpy.array([projMM, projMMslave]),
                    pos + randomNoise * numpy.random.random((len(radArray), 3)),
                    radArray,
                    numpy.array([[0, 0, 0], slaveCentreMM]),
                    numpy.array([numpy.eye(3), slaveTransformation]),
                    iterationsMax=50,
                    DEMcorr=True,
                    GRAPH=False,
                    verbose=1,
                )
                for j in range(pos.shape[0]):
                    for i in range(3):
                        self.assertEqual(numpy.abs(pos[j][i] - posOptimisedN[j][i]) < 0.1, True)

        print("test_optimiseSensitivityFieldsMultiProj_ManySpheres(): Done")

    # def test_optimisePositionsensitivityFields_3x3x3Spheres(self):
    # print("\n\ntest_optimisePositionsensitivityFields_3x3x3Spheres(): Starting up")
    # pos = numpy.array([[54, 4,  4], [54, 0,  4], [54, -4,  4],
    # [54, 4,  0], [54, 0,  0], [54, -4,  0],
    # [54, 4, -4], [54, 0, -4], [54, -4, -4],
    # [50, 4,  4], [50, 0,  4], [50, -4,  4],
    # [50, 4,  0], [50, 0,  0], [50, -4,  0],
    # [50, 4, -4], [50, 0, -4], [50, -4, -4],
    # [46, 4,  4], [46, 0,  4], [46, -4,  4],
    # [46, 4,  0], [46, 0,  0], [46, -4,  0],
    # [46, 4, -4], [46, 0, -4], [46, -4, -4]])
    # self.assertEqual(pos.shape[0], 27)
    # rad = 2
    # radArray = numpy.array([rad]*pos.shape[0])
    # projMM = radioSphere.projectSphere.projectSphereMM(pos, radArray)
    ##plt.imshow(projMM)
    ##plt.show()

    ##print("\tMaking sure sensitivity field optimiser doesn't get lost starting in the right place")
    ##posOptimised1 = radioSphere.optimisePositions.optimiseSensitivityFields(projMM, pos, radArray, iterationsMax=3)
    ##for j in range(pos.shape[0]):
    ##for i in range(3):
    ##self.assertEqual(numpy.abs(pos[j][i] - posOptimised1[j][i]) < 0.1, True)

    # print("\tMaking sure sensitivity field optimiser doesn't get lost with an small random max +-0.01 mm miss-guess + DEM")
    # posOptimised2 = radioSphere.optimisePositions.optimiseSensitivityFields(projMM, pos+0.01*numpy.random.random((27,3)), radArray, iterationsMax=50, verbose=1, DEMcorr=True)
    # for j in range(pos.shape[0]):
    # for i in range(3):
    # self.assertEqual(numpy.abs(pos[j][i] - posOptimised2[j][i]) < 0.1, True)

    # print("test_optimisePositionsensitivityFields_3x3x3Spheres(): Done")


if __name__ == "__main__":
    unittest.main()
