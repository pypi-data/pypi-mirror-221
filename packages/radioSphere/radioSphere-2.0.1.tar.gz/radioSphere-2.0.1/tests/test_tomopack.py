"""
Simple tests to make sure everything works as expected.
The layout is as per python's unittest but right it should just 
be executed, and all the `self.assertEqual`s should pass.

If a new function is added it should be called at the bottom of the function

This file contains tests with a single sphere
"""
#import os
#import sys

# Add root and radioSphere.projectSphere to be able to import it, this is ugly
#sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../')

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

    def test_singleSphereDetection(self):
        # First of all define a "perfect" psi
        radiusMM = 2
        psi = radioSphere.projectSphere.projectSphereMM(numpy.array([[50, 0, 0]]),
                                                        numpy.array([radiusMM]))
        #plt.imshow(psi)
        #plt.show()

        # now a noisy projection
        proj = radioSphere.projectSphere.projectSphereMM(numpy.array([[50, 0, 0]]),
                                                         numpy.array([radiusMM]),
                                                         blur=1)
        # This noise is not quite right, it should be added in I/I0 and not in log like here, but still
        proj += numpy.random.normal(size=proj.shape, scale=0.1)

        f_x = radioSphere.tomopack(proj, psi)
        self.assertTrue(f_x.shape[0] == proj.shape[0])
        self.assertTrue(f_x.shape[1] == proj.shape[1])
        

    # tomopack()
    #   Move single sphere around and make sure that detects there spheres

    # tomopackDivergentScanTo3DPositions()
    #   3-5 particles with different X positions

    # -> scanFixedNumber option do you get what you ask for?

    # indicatorFunctionToDetectorPositions needed??



if __name__ == "__main__":
    unittest.main()
