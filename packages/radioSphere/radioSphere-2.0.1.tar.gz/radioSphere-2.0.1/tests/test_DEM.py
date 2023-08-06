"""
Simple tests to make sure everything works as expected.
The layout is as per python's unittest but right it should just 
be executed, and all the `self.self.assertEqualEqual`s should pass.

If a new function is added it should be called at the bottom of the function

This file contains tests with a single sphere
"""
# import os
# import sys
# Add root and projectSphere to be able to import it, this is ugly
# sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../')

import radioSphere.DEM

import numpy
import unittest
from scipy.spatial.distance import cdist


class TestOptimiser(unittest.TestCase):
    def tearDown(self):
        try:
            pass
        except OSError:
            pass

    def test_optimiserSensitivityFields_3x3x3Spheres(self):
        # Just touching should not move
        pos = numpy.array([[0.0, 0.0, 5.0], [0.0, 0.0, -5.0]])
        rad = numpy.array([5.0, 5.0])
        posNew1, _ = radioSphere.DEM.DEM_step(pos, rad)
        self.assertEqual(numpy.sum(numpy.abs(pos - posNew1)), 0)

        # Not touching should not move
        pos = numpy.array([[0.0, 0.0, 7.0], [0.0, 0.0, -7.0]])
        rad = numpy.array([5.0, 5.0])
        posNew2, _ = radioSphere.DEM.DEM_step(pos, rad)
        self.assertEqual(numpy.sum(numpy.abs(pos - posNew2)), 0)

        # Overlapping should move
        pos = numpy.array([[0.0, 0.0, 3.0], [0.0, 0.0, -3.0]])
        rad = numpy.array([5.0, 5.0])
        posNew3, _ = radioSphere.DEM.DEM_step(pos, rad, k=0.001)
        self.assertEqual(numpy.sum(numpy.abs(pos - posNew3)) > 0, True)
        delta = cdist(posNew3, posNew3) - 2 * rad[0]  # calculate new distances
        self.assertFalse(any(delta[~numpy.eye(len(rad)).astype("bool")] < 0))  # no overlaps

        # Check k influence
        self.assertAlmostEqual(numpy.mean(numpy.abs(posNew3), axis=0)[2], rad[0], places=2)
        posNew4, _ = radioSphere.DEM.DEM_step(pos, rad, k=0.1)
        self.assertAlmostEqual(
            int(numpy.mean(numpy.abs(posNew4), axis=0)[2]), int(rad[0]), places=1
        )


if __name__ == "__main__":
    unittest.main()
