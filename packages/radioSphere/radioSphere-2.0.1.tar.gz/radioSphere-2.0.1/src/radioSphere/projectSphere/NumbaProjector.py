import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import numba as nb
# from radioSphere.projectSphere.NumpyProjector import project as project_func

@nb.jit(nopython=True, cache=True, parallel=True, fastmath=True)
def project(sourceDetectorDistMM, radiiMM, xx, yy, spheresPositionMM, p, scattering, focalSpotSize):
    r'''
    Function for forward radon transform of spheres (3D, cone beam) for one given angle

    Parameters
    ----------
        sourceDetectorDistMM : float
            Distance between source and detector in mm
        radiiMM : array
            Radii of spheres in mm
        xx : array
            x coordinates of pixels in mm
        yy : array
            y coordinates of pixels in mm
        spheresPositionMM : array
            Positions of spheres in mm
        p : array
            Projection data
        scattering : float
            Scattering coefficient
        focalSpotSize : float
            Focal spot size in mm

    Returns
    -------
        proj : array
            Projection data
    '''
    sdd = sourceDetectorDistMM
    #size of the projection data
    size = xx.shape[0], yy.shape[0]
    N,M = size

    #cartesian coordinates of pixels
    pixels_cart_coords = np.zeros((2,N,M))
    for i in nb.prange(N):
        pixels_cart_coords[0, i, :] = yy
    for j in nb.prange(M):
        pixels_cart_coords[1, :, j] = xx

    rays_vectors = np.zeros((3, N, M))
    # unit vectors of rays from source to pixels
    rays_vectors[0:2, :, :] = pixels_cart_coords
    rays_vectors[2] = sdd
    norms = np.sqrt(rays_vectors[0]**2 + rays_vectors[1]**2 + rays_vectors[2]**2)
    rays_vectors[0] /= norms; rays_vectors[1] /= norms; rays_vectors[2] /= norms #fastidious but necessary with parallel
    sphere = np.zeros(3)

    #loop over each sphere, /!\ no parallel here, because simultaneous pixel-writing causes problems
    for k in range(spheresPositionMM.shape[0]):

        #sphere position in cartesian coordinates
        sphere[0] = spheresPositionMM[k][1]
        sphere[1] = spheresPositionMM[k][2]
        sphere[2] = spheresPositionMM[k][0]
        sphere_radius = radiiMM[k]

        #loop over each pixel (N,M)
        for i in nb.prange(N):
            for j in nb.prange(M):
                ray = rays_vectors[:,i,j]
                #solve quadratic equation for line-sphere intersection
                a = ray[0]**2 + ray[1]**2 + ray[2]**2
                b = 2*(ray[0]*(-sphere[0]) + ray[1]*(-sphere[1]) + ray[2]*(-sphere[2]))
                c = (-sphere[0])**2 + (-sphere[1])**2 + (-sphere[2])**2 - sphere_radius**2
                delta = b**2 - 4*a*c
                if delta >= 0:
                    t1 = (-b + sqrt(delta))/(2*a)
                    t2 = (-b - sqrt(delta))/(2*a)
                    #if the ray intersects the sphere, add the length of the ray inside the sphere to the projection data
                    p[i,j] += np.abs(t1 - t2)
