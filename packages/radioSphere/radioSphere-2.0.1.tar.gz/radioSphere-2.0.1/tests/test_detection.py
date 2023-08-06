"""
Simple tests on tomopack to make sure everything works as expected.
The layout is as per python's unittest but right it should just 
be executed, and all the `self.assertEqualTrue`s should pass.

If a new function is added it should be called at the bottom of the function

"""

import radioSphere
import numpy
import unittest
import matplotlib.pyplot as plt
import shutil


class TestDetection(unittest.TestCase):
    def tearDown(self):
        try:
            shutil.rmtree("./output")
            pass
        except OSError:
            pass

    def test_fxToPeaks(self):
        # 2D fx
        fx = numpy.zeros((200, 100))
        fx[40, 70] = 0.5
        peaks = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx, scanFixedNumber=1
        )
        self.assertTrue(numpy.allclose([0, 40, 70], peaks))

        # 3D fx
        fx = numpy.zeros((30, 200, 100))
        fx[5, 40, 70] = 0.5
        peaksa = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx, scanFixedNumber=1
        )
        peaksb = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx, massThreshold=0.4
        )
        self.assertTrue(numpy.allclose([5, 40, 70], peaksa))
        self.assertTrue(numpy.allclose([5, 40, 70], peaksb))

    def test_peaksTo3DPos(self):
        # peaks at middle of detector so real pos should be at 0 of coord system
        peaks = numpy.array([[2, 100, 50]])
        CORxPos = numpy.arange(3)
        posXYZ = radioSphere.detectSpheres.detectorPeaksTo3DCoordinates(
            peaks, CORxPos, detectorResolution=[200, 100]
        )
        self.assertTrue(numpy.allclose(posXYZ, [2, 0, 0]))

        # backwards compatibility with projectSphere
        detectorResolution = [200, 100]
        sourceDetectorDistMM = 50
        pixelSizeMM = 0.5

        peaks = [2, 20, 80]
        CORxPos = numpy.arange(3)
        posXYZ = radioSphere.detectSpheres.detectorPeaksTo3DCoordinates(
            numpy.array([peaks]),
            CORxPos,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=sourceDetectorDistMM,
        )

        p = radioSphere.projectSphere.projectSphereMM(
            posXYZ,
            numpy.ones(posXYZ.shape[0]),
            detectorResolution=[200, 100],
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
        )

        sphereCentreDetector = numpy.argwhere(p == p.max())[0]
        # 1px tol
        self.assertTrue(numpy.allclose(peaks[1:], sphereCentreDetector, atol=1))

    def test_tomopackOneSphere(self):
        COR = 50
        r = 1
        detectorResolution = [400, 600]

        # Case 1: simplest case with 1 sphere in the middle of the detector and parallel projection
        p1 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[COR, 0, 0]]),
            numpy.array([r]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=numpy.inf,
        )

        psi = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[COR, 0, 0]]),
            numpy.array([r]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=numpy.inf,
        )

        fx1 = radioSphere.detectSpheres.tomopack(p1, psi)
        peaksJI1 = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx1, scanFixedNumber=1
        )[:, 1:]

        self.assertEqual(peaksJI1[0][0], detectorResolution[0] // 2)
        self.assertEqual(peaksJI1[0][1], detectorResolution[1] // 2)

        # Case 2: 1 sphere offset from the middle of the detector and parallel projection
        p2 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[COR, -5.7, 7.4]]),
            numpy.array([r]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=numpy.inf,
        )

        fx2 = radioSphere.detectSpheres.tomopack(p2, psi)
        peaksJI2 = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx2, massThreshold=0.1
        )[:, 1:]

        spherePosDetector2 = numpy.where(p2 == p2.max())
        estimatedSpherePosDetector2 = numpy.where(fx2 == fx2.max())

        # 1px max diff
        self.assertTrue(abs(spherePosDetector2[0] - peaksJI2[0][0]) <= 1)
        self.assertTrue(abs(spherePosDetector2[1] - peaksJI2[0][1]) <= 1)

        # Case 3: A bit of zoom, simplest case with 1 sphere in the middle of the detector
        p3 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[COR, 0, 0]]),
            numpy.array([r]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=100,
        )

        psi3 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[COR, 0, 0]]),
            numpy.array([r]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=100,
        )

        fx3 = radioSphere.detectSpheres.tomopack(p3, psi3)
        peaksJI3 = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx3, scanFixedNumber=1
        )[:, 1:]

        self.assertEqual(peaksJI3[0][0], detectorResolution[0] // 2)
        self.assertEqual(peaksJI3[0][1], detectorResolution[1] // 2)

        # Case 4: A bit of zoom, 1 sphere offset from the middle
        p4 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[COR, -1.2, -2.6]]),
            numpy.array([r]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=100,
        )

        fx4 = radioSphere.detectSpheres.tomopack(p4, psi3)
        peaksJI4 = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx4, scanFixedNumber=1
        )[:, 1:]

        spherePosDetector4 = numpy.where(p4 == p4.max())
        # 1px max diff
        self.assertTrue(abs(spherePosDetector4[0][0] - peaksJI4[0][0]) <= 1)
        self.assertTrue(abs(spherePosDetector4[1][0] - peaksJI4[0][1]) <= 1)

    # Tomopack 10 random spheres
    def test_tomopack10Spheres(self):
        COR = 50
        r = 1
        detectorResolution = [100, 150]
        sourceDetectorDistMM = 100
        pixelSizeMM = 0.1
        yMin, yMax = -1.5, 1.5
        zMin, zMax = -2, 2

        pos = numpy.zeros((10, 3))
        pos[:, 0] += COR
        pos[:, 1] = numpy.linspace(yMin, yMax, 10)
        pos[:, 2] = zMin + r + (zMax - zMin - 2 * r) * numpy.array([0.56998677, 0.60194996, 0.15213411, 0.47963821, 0.35141865,
       0.75942947, 0.23605196, 0.23212684, 0.48355353, 0.88538301])
        radii = numpy.ones_like(pos[:, 0]) * r

        p = radioSphere.projectSphere.projectSphereMM(
            pos,
            radii,
            detectorResolution=detectorResolution,
            pixelSizeMM=pixelSizeMM,
            sourceDetectorDistMM=sourceDetectorDistMM,
        )

        psi = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[COR, 0, 0]]),
            numpy.array([r]),
            detectorResolution=detectorResolution,
            pixelSizeMM=pixelSizeMM,
            sourceDetectorDistMM=sourceDetectorDistMM,
        )

        fx = radioSphere.detectSpheres.tomopack(p, psi)

        # call + test helper which transforms fx guess to detector peaks
        peaksJI = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
            fx, scanFixedNumber=pos.shape[0]
        )

        # call + test helper which transforms det peaks to 3d coord
        posTomopackXYZ = radioSphere.detectSpheres.detectorPeaksTo3DCoordinates(
            peaksJI,
            numpy.ones(peaksJI.shape[0]) * COR,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=p.shape,
            sourceDetectorDistMM=sourceDetectorDistMM,
        )

        # sort tomopack guess to calculate residual directly on positions
        posTomopackXYZ = posTomopackXYZ[numpy.argsort(posTomopackXYZ[:, 1])]
        self.assertTrue(numpy.mean(numpy.linalg.norm(pos - posTomopackXYZ, axis=1) < 0.5 * r))

    def test_tomopackDivergentBeamOneSphere(self):
        r = 1
        COR = 50
        detectorResolution = [400, 600]

        # Case 1: simplest case with 1 sphere in the middle of the detector
        pos1 = numpy.array([[COR, 0, 0]])
        p1 = radioSphere.projectSphere.projectSphereMM(
            pos1, numpy.array([r]), detectorResolution=detectorResolution, sourceDetectorDistMM=100
        )

        posXYZ1a = radioSphere.detectSpheres.tomopackDivergentScanTo3DPositions(
            p1, r, CORxRef=COR, CORxNumber=5, scanFixedNumber=1, saveSeries=False, verbose=False
        )
        posXYZ1b = radioSphere.detectSpheres.tomopackDivergentScanTo3DPositions(
            p1, r, CORxRef=COR, CORxNumber=5, saveSeries=False, massThreshold=0.09
        )

        self.assertTrue(numpy.allclose(pos1, posXYZ1a[0], atol=0.5))
        self.assertTrue(numpy.allclose(pos1, posXYZ1b[0], atol=0.5))

        # Case 2: 1 sphere shifted from COR and centre of detector
        # pos2 = numpy.array(
        #     [
        #         [
        #             numpy.random.uniform(49, 51),
        #             numpy.random.uniform(3, -3),
        #             numpy.random.uniform(-3, 3),
        #         ]
        #     ]
        # )
        # pos2 = numpy.array([[47.20396842, 0, 0]])
        pos2 = numpy.array([[48.22945869, -1.63507697, 0.96052506]])
        p2 = radioSphere.projectSphere.projectSphereMM(
            pos2, numpy.array([r]), detectorResolution=detectorResolution, sourceDetectorDistMM=100
        )

        posXYZ2a = radioSphere.detectSpheres.tomopackDivergentScanTo3DPositions(
            p2,
            r,
            CORxMin=COR - 4 * r,
            CORxMax=COR + 4 * r,
            CORxNumber=100,
            scanFixedNumber=1,
            saveSeries=False,
            verbose=False,
        )
        posXYZ2b = radioSphere.detectSpheres.tomopackDivergentScanTo3DPositions(
            p2,
            r,
            CORxMin=COR - 4 * r,
            CORxMax=COR + 4 * r,
            CORxNumber=100,
            saveSeries=True,
            verbose=False,
            massThreshold=0.09,
        )

        self.assertTrue(numpy.allclose(pos2, posXYZ2a[0], atol=0.5))
        self.assertTrue(numpy.allclose(pos2, posXYZ2b[0], atol=0.5))

    def test_tomopackDivergentBeam10Spheres(self):
        r = 1
        COR = 50
        detectorResolution = [400, 600]
        pixelSizeMM = 0.1

        xMin, xMax = 40, 60
        yMin, yMax = -5, 5
        zMin, zMax = -7, 7

        pos = numpy.zeros((10, 3))
        pos[:, 0] = numpy.arange(xMin, xMax, 2 * r)
        # pos[:, 1] = yMin + r + (yMax - yMin - 2 * r) * numpy.random.rand(10)
        # pos[:, 2] = zMin + r + (zMax - zMin - 2 * r) * numpy.random.rand(10)
        pos[:, 1] = yMin + r + (yMax - yMin - 2 * r) * numpy.array([0.17644032, 0.90256817, 0.65495579, 0.56029433, 0.87741035,
       0.29646542, 0.15650145, 0.79771666, 0.96944108, 0.90927292])
        pos[:, 2] = zMin + r + (zMax - zMin - 2 * r) * numpy.array([0.56998677, 0.60194996, 0.15213411, 0.47963821, 0.35141865,
       0.75942947, 0.23605196, 0.23212684, 0.48355353, 0.88538301])
        radii = numpy.ones_like(pos[:, 0]) * r

        p = radioSphere.projectSphere.projectSphereMM(
            pos,
            radii,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=100,
        )

        posXYZa = radioSphere.detectSpheres.tomopackDivergentScanTo3DPositions(
            p,
            r,
            CORxMin=COR - 11 * r,
            CORxMax=COR + 11 * r,
            CORxNumber=50,
            scanFixedNumber=pos.shape[0],
            saveSeries=True,
            saveSeriesDirectory="./output",
        )

        posXYZb = radioSphere.detectSpheres.tomopackDivergentScanTo3DPositions(
            p,
            r,
            CORxMin=COR - 11 * r,
            CORxMax=COR + 11 * r,
            CORxNumber=50,
            fXseries="./output/fXseries.tif",
            psiXseries="./output/psiXseries.tif",
            # massThreshold=0.1,
            scanFixedNumber=pos.shape[0],
            saveSeries=False,
        )

        # sort guess based on X axis to calculate residual directly on position
        posXYZa = posXYZa[numpy.argsort(posXYZa[:, 0])]
        posXYZb = posXYZb[numpy.argsort(posXYZb[:, 0])]

        self.assertTrue(numpy.mean(numpy.linalg.norm(pos - posXYZa, axis=1)) < 1.5 * r)
        self.assertTrue(numpy.mean(numpy.linalg.norm(pos - posXYZb, axis=1)) < 1.5 * r)


if __name__ == "__main__":
    unittest.main()
