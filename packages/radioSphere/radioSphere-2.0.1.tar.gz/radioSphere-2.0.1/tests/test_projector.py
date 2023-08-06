"""
Simple tests to make sure everything works as expected.
The layout is as per python's unittest but right it should just 
be executed, and all the `self.assertEqual`s should pass.

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


class TestOneSphere(unittest.TestCase):
    def tearDown(self):
        try:
            pass
        except OSError:
            pass

    def test_pointToDetectorPixelRange(self):
        print("\n\ntest_pointToDetectorPixelRange(): Starting up")

        sourceDetectorDistMM = 100
        pixelSizeMM = 0.1
        detectorResolution = [400, 600]

        displacementMM = 2

        print("\tMaking sure that a centred sphere is in the middle of the detector")
        posJI = radioSphere.projectSphere.pointToDetectorPixelRange(
            numpy.array([[50, 0, 0]]),
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
        )
        self.assertEqual(posJI[0], detectorResolution[0] // 2)
        self.assertEqual(posJI[1], detectorResolution[1] // 2)

        print("\tMaking sure that a sphere moving in +Y is closer to the origin of the detector")
        posJI = radioSphere.projectSphere.pointToDetectorPixelRange(
            numpy.array([[50, displacementMM, 0]]),
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
        )
        # Y is in the column direction
        self.assertEqual(posJI[0], detectorResolution[0] // 2)
        self.assertEqual(
            posJI[1],
            detectorResolution[1] // 2 - displacementMM * (sourceDetectorDistMM / 50) / 0.1,
        )

        print("\tMaking sure that a sphere moving in +Z is closer to the origin of the detector")
        posJI = radioSphere.projectSphere.pointToDetectorPixelRange(
            numpy.array([[50, 0, displacementMM]]),
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
        )
        self.assertEqual(
            posJI[0],
            detectorResolution[0] // 2 - displacementMM * (sourceDetectorDistMM / 50) / 0.1,
        )
        self.assertEqual(posJI[1], detectorResolution[1] // 2)

        print("test_pointToDetectorPixelRange(): Done")


    def test_singleSphereToDetectorPixelRange(self):
        # This is a very light test for reasonable behaviour, the real test will come within test_projectorsOneSphere
        print("\n\ntest_singleSphereToDetectorPixelRange(): Starting up")

        sourceDetectorDistMM = 100
        pixelSizeMM = 0.1
        detectorResolution = [400, 600]

        print(
            "\tMaking sure that a centred sphere has a range either side of the middle of the detector"
        )
        rangeJI = radioSphere.projectSphere.singleSphereToDetectorPixelRange(
            numpy.array([[50, 0, 0]]),
            2,
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
        )
        self.assertEqual(rangeJI[0, 0] < detectorResolution[0] // 2, True)
        self.assertEqual(rangeJI[0, 1] > detectorResolution[0] // 2, True)
        self.assertEqual(rangeJI[1, 0] < detectorResolution[1] // 2, True)
        self.assertEqual(rangeJI[1, 1] > detectorResolution[1] // 2, True)

        print("test_singleSphereToDetectorPixelRange(): Done")

    def test_projectorsOneSphere(self):
        print("\n\ntest_projectorsOneSphere(): Starting up")

        radiusMM = 2

        print("\tMaking sure we get the number of pixels we ask for on the detector, even...")
        detectorResolution = [200, 300]
        projMM1 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 0, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
        )
        self.assertEqual(detectorResolution[0] == projMM1.shape[0], True)
        self.assertEqual(detectorResolution[1] == projMM1.shape[1], True)

        print("\tMaking sure we get the number of pixels we ask for on the detector, odd...")
        detectorResolution = [99, 151]
        projMM2 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 0, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
        )
        self.assertEqual(detectorResolution[0] == projMM2.shape[0], True)
        self.assertEqual(detectorResolution[1] == projMM2.shape[1], True)
        # plt.imshow(projMM2)
        # plt.show()

        print("\tMaking sure the max projected length is 2*the imposed radius")
        detectorResolution = [512, 512]
        projMM3 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 0, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
        )
        self.assertEqual(numpy.abs(projMM3.max() - radiusMM * 2) < 0.01, True)
        self.assertEqual(projMM3.min() == 0.0, True)

        print("\tMaking sure that a little 1px blur doesn't change the image that much")
        detectorResolution = [512, 512]
        projMM3b = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 0, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            blur=1,
        )
        self.assertEqual(
            numpy.abs(projMM3 - projMM3b).sum() / detectorResolution[0] / detectorResolution[1]
            < 0.1,
            True,
        )

        print("\tMaking sure that the projections gets bigger if the sphere gets closer")
        projMM4 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[40, 0, 0]]), numpy.array([radiusMM])
        )
        self.assertEqual(numpy.sum(projMM4 > 0.1) > numpy.sum(projMM3 > 0.1), True)

        print("\tMaking sure that parallel projections remain the same under zoom")
        projMMp1 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[40, 0, 0]]), numpy.array([radiusMM]), sourceDetectorDistMM=numpy.inf
        )
        projMMp2 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[60, 0, 0]]), numpy.array([radiusMM]), sourceDetectorDistMM=numpy.inf
        )
        self.assertEqual(numpy.sum(projMMp1 - projMMp2), 0)

        print("\tMaking sure that parallel y,z == 0 sphere is in the middle of the projection")
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMMp1 > 0.1)[0]
                - detectorResolution[0] / 2
                + 0.5
            )
            < 0.1,
            True,
        )
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMMp1 > 0.1)[1]
                - detectorResolution[1] / 2
                + 0.5
            )
            < 0.1,
            True,
        )
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMMp1 > 0.1)[0]
                - detectorResolution[0] / 2
                + 0.5
            )
            < 0.1,
            True,
        )
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMMp1 > 0.1)[1]
                - detectorResolution[1] / 2
                + 0.5
            )
            < 0.1,
            True,
        )

        print("\tMaking sure that parallel y,z == 0 sphere is exactly the right size")
        radiusPx = numpy.sqrt(numpy.sum(projMMp1 > 0) / numpy.pi)
        self.assertEqual(numpy.abs(radiusPx - radiusMM / 0.1) < 0.1, True)

        print("\tMaking sure that parallel +y moves things to the left of the projection")
        projMMp3 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[40, 5, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=numpy.inf,
        )
        COM1 = scipy.ndimage.center_of_mass(projMMp1 > 0.1)
        COM3 = scipy.ndimage.center_of_mass(projMMp3 > 0.1)
        self.assertEqual(numpy.abs(COM1[0] - COM3[0]) < 0.1, True)
        self.assertEqual(COM1[1] - COM3[1] > 1, True)

        print("\tMaking sure that parallel +z moves things up in the projection")
        projMMp4 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[40, 0, 5]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            sourceDetectorDistMM=numpy.inf,
        )
        COM4 = scipy.ndimage.center_of_mass(projMMp4 > 0.1)
        self.assertEqual(numpy.abs(COM1[1] - COM4[1]) < 0.1, True)

        print("\tMaking sure that y,z == 0 sphere is in the middle of the projection")
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMM3 > 0.1)[0]
                - detectorResolution[0] / 2
                + 0.5
            )
            < 0.1,
            True,
        )
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMM3 > 0.1)[1]
                - detectorResolution[1] / 2
                + 0.5
            )
            < 0.1,
            True,
        )
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMM4 > 0.1)[0]
                - detectorResolution[0] / 2
                + 0.5
            )
            < 0.1,
            True,
        )
        self.assertEqual(
            numpy.abs(
                scipy.ndimage.center_of_mass(projMM4 > 0.1)[1]
                - detectorResolution[1] / 2
                + 0.5
            )
            < 0.1,
            True,
        )

        print("\tMaking sure that +y moves things to the left of the projection")
        projMM5 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 5, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
        )
        COM3 = scipy.ndimage.center_of_mass(projMM3 > 0.1)
        COM5 = scipy.ndimage.center_of_mass(projMM5 > 0.1)
        self.assertEqual(numpy.abs(COM3[0] - COM5[0]) < 0.1, True)
        self.assertEqual(COM3[1] - COM5[1] > 1, True)

        print("\tMaking sure that +y is centred again when we apply a 90 deg rotation")
        projMM5b = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 5, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            transformationCentreMM=[50, 0, 0],
            transformationMatrix=numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
        )
        COM3 = scipy.ndimage.center_of_mass(projMM3 > 0.1)
        COM5b = scipy.ndimage.center_of_mass(projMM5b > 0.1)
        self.assertEqual(numpy.abs(COM3[0] - COM5b[0]) < 0.1, True)
        self.assertEqual(numpy.abs(COM3[1] - COM5b[1]) < 0.1, True)

        print("\tMaking sure that +z moves things up in the projection")
        projMM6 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 0, 5]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
        )
        COM3 = scipy.ndimage.center_of_mass(projMM3 > 0.1)
        COM6 = scipy.ndimage.center_of_mass(projMM6 > 0.1)
        self.assertEqual(numpy.abs(COM3[1] - COM6[1]) < 0.1, True)

        print("\tMaking sure that ROI mode crops when centred")
        projMM7 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 0, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            ROIcentreMM=numpy.array([[50, 0, 0]]),
            ROIradiusMM=radiusMM,
        )
        self.assertEqual(projMM7.shape[0] < detectorResolution[0], True)
        self.assertEqual(projMM7.shape[1] < detectorResolution[1], True)
        # Check we got the middle
        self.assertEqual(numpy.abs(projMM7.max() - 2 * radiusMM < 0.1), True)
        # The edges should all be zero since there's a small margin
        self.assertEqual(numpy.sum(projMM7[0]), 0)
        self.assertEqual(numpy.sum(projMM7[-1]), 0)
        self.assertEqual(numpy.sum(projMM7[:, 0]), 0)
        self.assertEqual(numpy.sum(projMM7[:, -1]), 0)

        print("\tMaking sure that ROI mode crops when centred and in transformed coordinates")
        projMM7b = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 0, 0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            ROIcentreMM=numpy.array([[50, 0, 0]]),
            ROIradiusMM=radiusMM,
            transformationCentreMM=[50, 0, 0],
            transformationMatrix=numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
        )
        # plt.imshow(projMM7b)
        # plt.show()
        self.assertEqual(projMM7b.shape[0] < detectorResolution[0], True)
        self.assertEqual(projMM7b.shape[1] < detectorResolution[1], True)
        # Check we got the middle
        self.assertEqual(numpy.abs(projMM7b.max() - 2 * radiusMM < 0.1), True)
        # The edges should all be zero since there's a small margin
        self.assertEqual(numpy.sum(projMM7b[0]), 0)
        self.assertEqual(numpy.sum(projMM7b[-1]), 0)
        self.assertEqual(numpy.sum(projMM7b[:, 0]), 0)
        self.assertEqual(numpy.sum(projMM7b[:, -1]), 0)

        print("\tMaking sure that ROI mode crops when off-centre")
        projMM8 = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 1, -0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            ROIcentreMM=numpy.array([[50, 1, -0]]),
            ROIradiusMM=radiusMM,
        )
        self.assertEqual(projMM8.shape[0] < detectorResolution[0], True)
        self.assertEqual(projMM8.shape[1] < detectorResolution[1], True)
        # Check we got the middle
        self.assertEqual(numpy.abs(projMM8.max() - 2 * radiusMM) < 0.1, True)
        # The edges should all be zero since there's a small margin
        self.assertEqual(numpy.sum(projMM8[0]), 0)
        self.assertEqual(numpy.sum(projMM8[-1]), 0)
        self.assertEqual(numpy.sum(projMM8[:, 0]), 0)
        self.assertEqual(numpy.sum(projMM8[:, -1]), 0)

        print("\tMaking sure that ROI mode crops when more off-centre")
        projMM8a = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[42, 7, -0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            ROIcentreMM=numpy.array([[42, 7, -0]]),
            ROIradiusMM=radiusMM,
        )
        # plt.imshow(projMM8a)
        # plt.show()
        self.assertEqual(projMM8a.shape[0] < detectorResolution[0], True)
        self.assertEqual(projMM8a.shape[1] < detectorResolution[1], True)
        # Check we got the middle
        self.assertEqual(numpy.abs(projMM8a.max() - 2 * radiusMM) < 0.1, True)
        # The edges should all be zero since there's a small margin
        self.assertEqual(numpy.sum(projMM8a[0]), 0)
        self.assertEqual(numpy.sum(projMM8a[-1]), 0)
        self.assertEqual(numpy.sum(projMM8a[:, 0]), 0)
        self.assertEqual(numpy.sum(projMM8a[:, -1]), 0)

        print("\tMaking sure that ROI mode crops when off-centre and in transformed coordinates")
        projMM8b = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 1, -0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            ROIcentreMM=numpy.array([[50, 1, -0]]),
            ROIradiusMM=radiusMM,
            transformationCentreMM=[50, 0, 0],
            transformationMatrix=numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
        )
        # plt.imshow(projMM8b)
        # plt.show()
        self.assertEqual(projMM8b.shape[0] < detectorResolution[0], True)
        self.assertEqual(projMM8b.shape[1] < detectorResolution[1], True)
        # Check we got the middle
        self.assertEqual(numpy.abs(projMM8b.max() - 2 * radiusMM) < 0.1, True)
        # The edges should all be zero since there's a small margin
        self.assertEqual(numpy.sum(projMM8b[0]), 0)
        self.assertEqual(numpy.sum(projMM8b[-1]), 0)
        self.assertEqual(numpy.sum(projMM8b[:, 0]), 0)
        self.assertEqual(numpy.sum(projMM8b[:, -1]), 0)

        print("\tMaking sure that ROI mode crops when off-centre and in transformed coordinates")
        projMM8c = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[50, 1, -0]]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            ROIcentreMM=numpy.array([[50, 1, -0]]),
            ROIradiusMM=radiusMM,
            transformationCentreMM=[43, 0, 0],
            transformationMatrix=numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]),
        )
        # plt.imshow(projMM8c)
        # plt.show()
        self.assertEqual(projMM8c.shape[0] < detectorResolution[0], True)
        self.assertEqual(projMM8c.shape[1] < detectorResolution[1], True)
        # Check we got the middle
        self.assertEqual(numpy.abs(projMM8c.max() - 2 * radiusMM) < 0.1, True)
        # The edges should all be zero since there's a small margin
        self.assertEqual(numpy.sum(projMM8c[0]), 0)
        self.assertEqual(numpy.sum(projMM8c[-1]), 0)
        self.assertEqual(numpy.sum(projMM8c[:, 0]), 0)
        self.assertEqual(numpy.sum(projMM8c[:, -1]), 0)

        print("test_projectorsOneSphere(): Done")

    def test_computeMotionKernel(self):
        # horizontal kernel
        kernel1 = radioSphere.projectSphere.computeMotionKernel(
            numpy.array([0, 2, 0]), numpy.array([0, 5, 0])
        )
        self.assertAlmostEqual(kernel1.sum(), 1, places=4)
        # vertical kernel
        kernel2 = radioSphere.projectSphere.computeMotionKernel(
            numpy.array([0, 0, 2]), numpy.array([0, 0, 5])
        )
        self.assertAlmostEqual(kernel2.sum(), 1, places=4)
        # no kernel
        kernel3 = radioSphere.projectSphere.computeMotionKernel(
            numpy.array([0, 0, 2]), numpy.array([0, 0, 2.2])
        )
        self.assertTrue(kernel3 is None)

    # def test_projectorsThreeSpheres(self):
    # print("\n\ntest_projectorsThreeSpheres(): Starting up")
    # radiusMM = 2

    # print("\tMaking sure we get the number dots we asked for on the detector...")
    # detectorResolution = [512,512]
    # projMM1 = radioSphere.projectSphere.projectSphereMM(numpy.array([[50, 0, 0], [50, -5, 0], [50, 5, 0]]),
    # numpy.array([radiusMM, radiusMM, radiusMM]),
    # detectorResolution=detectorResolution)
    ##plt.imshow(projMM1)
    ##plt.show()
    # self.assertEqual(scipy.ndimage.label(projMM1 > 0.1)[1] == 3, True)
    # self.assertEqual(numpy.abs(projMM1.max() - radiusMM*2) < 0.01, True)
    # self.assertEqual(projMM1.min() == 0.0, True)

    # print("\tMaking sure we get the one dots when we're in a 90 deg rotated geometry")
    # detectorResolution = [512,512]
    # projMM2 = radioSphere.projectSphere.projectSphereMM(numpy.array([[50, 0, 0], [50, -5, 0], [50, 5, 0]]),
    # numpy.array([radiusMM, radiusMM, radiusMM]),
    # detectorResolution=detectorResolution,
    # transformationCentreMM=[50,0,0],
    # transformationMatrix=numpy.array([[0, -1, 0],[1, 0, 0],[0, 0, 1]]))
    ##plt.imshow(projMM2)
    ##plt.show()
    # self.assertEqual(scipy.ndimage.label(projMM2 > 0.1)[1] == 1, True)
    # print("test_projectorsThreeSpheres(): Done")


if __name__ == "__main__":
    unittest.main()
