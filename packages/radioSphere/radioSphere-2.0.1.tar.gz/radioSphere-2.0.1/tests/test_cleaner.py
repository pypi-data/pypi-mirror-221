#!/usr/bin/env python
# coding: utf-8
import os, sys
import radioSphere.detectSpheres
import radioSphere.projectSphere
from radioSphere.DEM.nddem import write_infile, write_dumpfile
import matplotlib.pyplot as plt
from scipy.spatial import distance
import numpy
import tifffile

# plt.style.use('./tools/radioSphere.mplstyle')

zoomLevel = 10
sourceObjectDistMM = 20.0
pixelSizeDetectorMM = 0.1
detectorResolution = [512, 512]
radiusMM = 0.5

CORxMin = -2.0 + sourceObjectDistMM
CORxMax = 2.0 + sourceObjectDistMM
CORxNumber = 40

positionsXYZmmTrue = numpy.array(
    [
        [-1, -1, -1],
        [0, -1, -1],
        [1, -1, -1],
        [-1, 0, -1],
        [0, 0, -1],
        [1, 0, -1],
        [-1, 1, -1],
        [0, 1, -1],
        [1, 1, -1],
        [-1, -1, 0],
        [0, -1, 0],
        [1, -1, 0],
        [-1, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
        [-1, 1, 0],
        [0, 1, 0],
        [1, 1, 0],
        [-1, -1, 1],
        [0, -1, 1],
        [1, -1, 1],
        [-1, 0, 1],
        [0, 0, 1],
        [1, 0, 1],
        [-1, 1, 1],
        [0, 1, 1],
        [1, 1, 1],
    ],
    dtype=float,
)

positionsXYZmmTrue[:, 0] += sourceObjectDistMM
radiiMM = radiusMM * numpy.ones(len(positionsXYZmmTrue))


radioMM = radioSphere.projectSphere.projectSphereMM(
    positionsXYZmmTrue,
    radiiMM,
    sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
    pixelSizeMM=pixelSizeDetectorMM,
    detectorResolution=detectorResolution,
)

plt.subplot(231)
plt.title("True radio")
plt.imshow(radioMM)
plt.colorbar()


# Shuffle positions
SEED = 0
rng = numpy.random.default_rng()  # SEED)
positionsXYZmmFalse = positionsXYZmmTrue.copy()
rng.shuffle(positionsXYZmmFalse, axis=0)

# Add perturbations
positionsXYZmmFalse += 0.05 * (numpy.random.rand(positionsXYZmmFalse.shape[0], 3) - 0.5)
positionsXYZmmFalse[0] -= [0, 1, 0]
positionsXYZmmFalse[1] -= [0, 1, 0]
positionsXYZmmFalse[2] -= [0, 1, 0]

p_f_x = radioSphere.projectSphere.projectSphereMM(
    positionsXYZmmFalse,
    radiusMM * numpy.ones(len(positionsXYZmmFalse)),
    sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
    pixelSizeMM=pixelSizeDetectorMM,
    detectorResolution=radioMM.shape,
)

plt.subplot(232)
plt.title("Measured radio")
plt.imshow(p_f_x)
plt.colorbar()


plt.subplot(233)
plt.title("Initial residual")
plt.imshow(p_f_x - radioMM, vmin=-2, vmax=2, cmap="bwr")
plt.colorbar()

positionsXYZmmClean = radioSphere.detectSpheres.cleanDivergentScan(
    positionsXYZmmFalse,
    radioMM,
    radiiMM,
    zoomLevel,
    sourceObjectDistMM,
    pixelSizeDetectorMM,
    CORxMin,
    CORxMax,
    CORxNumber,
    verbose=False,
    GRAPH=False,
)

p_f_x_clean = radioSphere.projectSphere.projectSphereMM(
    positionsXYZmmClean,
    radiusMM * numpy.ones(len(positionsXYZmmClean)),
    sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
    pixelSizeMM=pixelSizeDetectorMM,
    detectorResolution=radioMM.shape,
)

residual_clean = p_f_x_clean - radioMM

plt.subplot(223)
plt.title("Cleaned radio")
plt.imshow(p_f_x_clean)
plt.subplot(224)
plt.title("Cleaned residual")
plt.imshow(residual_clean, vmin=-1, vmax=1, cmap="bwr")
plt.colorbar()

m, s, l = radioSphere.detectSpheres.calculateErrors(
    positionsXYZmmFalse, positionsXYZmmTrue, radiiMM
)
print(m, s, l)
m, s, l = radioSphere.detectSpheres.calculateErrors(
    positionsXYZmmClean, positionsXYZmmTrue, radiiMM
)
print(m, s, l)

dumpfolder = "~/code/NDDEM/Samples/radioSphere/"
# write_infile(positionsXYZmmTrue,radiiMM,3,dumpfolder=dumpfolder)
# write_dumpfile(positionsXYZmmTrue,radiiMM,0,dumpfolder=dumpfolder)
# write_dumpfile(positionsXYZmmFalse,radiiMM,1,dumpfolder=dumpfolder)
# write_dumpfile(positionsXYZmmClean,radiiMM,2,dumpfolder=dumpfolder)


# plt.show()
