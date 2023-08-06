import os
import sys
import json5
import numpy
import radioSphere
import tifffile
import scipy.ndimage
import matplotlib
import matplotlib.pyplot as plt



def main():
    params_file = sys.argv[1]

    # Plotting stuff
    plt.style.use(os.path.join(radioSphere.__path__[0], 'radioSphere.mplstyle'))
    matplotlib.rcParams['figure.figsize'] = [10,6]

    # Load experimental logfile with all necessary parameters
    with open(params_file,'r') as f: exp = json5.load(f)
    with open(exp["dataFolder"] + exp["fitParamsPath"],'r') as f: cal = json5.load(f)
    positionsXYZmm = numpy.loadtxt(exp["dataFolder"] + exp["tomopackPath"])

    # Load images
    I    = tifffile.imread(exp["dataFolder"] + exp["radioGL"]).astype(float)
    dark = tifffile.imread(exp["dataFolder"] + exp["darkField"]).astype(float)
    bg   = tifffile.imread(exp["dataFolder"] + exp["background"]).astype(float)

    radioGL = ( I - dark ) / ( bg - dark )
    radioGL = radioGL[exp["ROI"][1][0]:exp["ROI"][1][1],exp["ROI"][0][0]:exp["ROI"][0][1]]
    radioGL = scipy.ndimage.zoom(radioGL, 1./exp["binning"])
    radioGL = numpy.pad(radioGL, 10, 'linear_ramp', end_values=1) # removes artifacts from particles being close to the edge

    radioMM = radioSphere.calibrateAttenuation.gl_to_mm_linear(radioGL, *cal["fit_args"])

    # Now generate a radiograph using the recovered positions
    p_f_x = radioSphere.projectSphere.projectSphereMM(
        positionsXYZmm,
        exp["radiusMM"]*numpy.ones(len(positionsXYZmm)),
        sourceDetectorDistMM=exp["sourceDetectorDistMM"],
        pixelSizeMM=exp["pixelSizeMM"]*exp["binning"],
        detectorResolution=radioMM.shape,
        projector=exp["projector"],
        scattering=cal["scattering"]
        )

    # Calculate the current residual (difference between what we wanted and what we got)
    residual = p_f_x - radioMM

    positionsXYZmmOpt = radioSphere.optimisePositions.optimiseSensitivityFields(
    radioMM,
    positionsXYZmm,
    exp["radiusMM"]*numpy.ones(len(positionsXYZmm)),
    # perturbationMM=perturbationMM,
    # minDeltaMM=0.001,
    iterationsMax=2500,
    sourceDetectorDistMM=exp["sourceDetectorDistMM"],
    pixelSizeMM=exp["pixelSizeMM"]*exp["binning"],
    detectorResolution=radioMM.shape,
    verbose=exp["verbose"],
    DEMcorr=False,
    GRAPH=False,
    projector=exp["projector"],
    scattering=cal["scattering"]
    )

    # Make guess at radiograph from optimised positions
    p_f_x_Opt = radioSphere.projectSphere.projectSphereMM(
        positionsXYZmmOpt,
        exp["radiusMM"]*numpy.ones(len(positionsXYZmmOpt)),
        sourceDetectorDistMM=exp["sourceDetectorDistMM"],
        pixelSizeMM=exp["pixelSizeMM"]*exp["binning"],
        detectorResolution=radioMM.shape,
        projector=exp["projector"],
        scattering=cal["scattering"]
        )

    # Calculate updated residual
    residualOpt = p_f_x_Opt - radioMM

    if exp["verbose"]:
        plt.clf()
        plt.subplot(2,2,1)
        plt.title("radioMM")
        plt.imshow(radioMM)
        plt.colorbar()

        plt.subplot(2,2,2)
        plt.title("Residual from tomopack $\psi$ scan 3D guess")
        plt.imshow(residual, vmin=-1, vmax=1, cmap='coolwarm')
        plt.colorbar()

        plt.subplot(2,2,3)
        plt.title("Residual after optimisation")
        plt.imshow(residualOpt, vmin=-1, vmax=1, cmap='coolwarm')
        plt.colorbar()

        plt.subplot(2,2,4)
        plt.title(r"Residual after optimisation ($\frac{1}{50}$ LUT range)")
        plt.imshow(residualOpt, vmin=-0.02, vmax=0.02, cmap='coolwarm')
        plt.colorbar()
        plt.show()
        

        

if __name__ == '__main__':
    main()
