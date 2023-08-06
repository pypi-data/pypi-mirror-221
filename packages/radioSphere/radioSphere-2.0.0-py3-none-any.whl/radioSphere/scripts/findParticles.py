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
    if os.path.exists(exp["dataFolder"] + exp["fitManyParamsPath"]):
        with open(exp["dataFolder"] + exp["fitManyParamsPath"],'r') as f: cal = json5.load(f)
    else:
        with open(exp["dataFolder"] + exp["fitSingleParamsPath"],'r') as f: cal = json5.load(f)
    
    # Load images
    I    = tifffile.imread(exp["dataFolder"] + exp["radioGL"]).astype(float)
    dark = tifffile.imread(exp["dataFolder"] + exp["darkField"]).astype(float)
    bg   = tifffile.imread(exp["dataFolder"] + exp["background"]).astype(float)
    
    radioGL = ( I - dark ) / ( bg - dark )
    radioGL = radioGL[exp["ROI"][1][0]:exp["ROI"][1][1],exp["ROI"][0][0]:exp["ROI"][0][1]]
    radioGL = scipy.ndimage.zoom(radioGL, 1./exp["binning"])
    radioGL = numpy.pad(radioGL, 10, 'linear_ramp', end_values=1) # removes artifacts from particles being close to the edge

    gl_to_mm = eval('radioSphere.calibrateAttenuation.gl_to_mm_' + exp["fit_order"])
    # mm_to_gl = eval('radioSphere.calibrateAttenuation.mm_to_gl_' + exp["fit_order"])

    radioMM = gl_to_mm(radioGL, *cal["fit_args"])

    positionsXYZmm = radioSphere.detectSpheres.tomopackDivergentScanTo3DPositions(
        radioMM,
        exp["radiusMM"],
        CORxMin=exp["X_min"],
        CORxMax=exp["X_max"],
        CORxNumber=exp["nX"],
        scanFixedNumber=exp["nSpheres"],
        sourceDetectorDistMM=exp["sourceDetectorDistMM"],
        pixelSizeMM=exp["pixelSizeMM"]*exp["binning"],
        l=exp["l"],
        # kTrustMethod='SNR',
        kTrustMethod='iterative',
        SNRCutoff=2,
        saveSeries=True,
        saveSeriesDirectory='cache',
        maxIterations=100,
        projector=exp["projector"],
        scattering=cal["scattering"]
        )
    # print(positionsXYZmm)

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
    vmin = numpy.minimum(radioMM.min(),p_f_x.min())
    vmax = numpy.maximum(radioMM.max(),p_f_x.max())
    if exp["verbose"]:
        plt.clf()
        plt.subplot(1,3,1)
        plt.title("radioMM")
        plt.imshow(radioMM, vmin=vmin, vmax=vmax)
        plt.colorbar()

        plt.subplot(1,3,2)
        plt.title("Guess at radioMM")
        plt.imshow(p_f_x, vmin=vmin, vmax=vmax)
        plt.colorbar()

        plt.subplot(1,3,3)
        plt.title("Residual from tomopack scan")
        plt.imshow(residual, vmin=-1, vmax=1, cmap='coolwarm')
        plt.colorbar()

        plt.show()
    

    numpy.savetxt(exp["dataFolder"] + exp["tomopackPath"], positionsXYZmm)

if __name__ == '__main__':
    main()
