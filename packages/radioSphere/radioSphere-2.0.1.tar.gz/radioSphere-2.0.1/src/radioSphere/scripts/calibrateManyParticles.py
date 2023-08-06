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
    radioGL = numpy.pad(radioGL, 10, 'linear_ramp', end_values=1) # removes artifacts from 

    positionsXYZmm = numpy.loadtxt(exp["dataFolder"] + exp["tomopackPath"])
    calibration_args_guess = [*cal["fit_args"], cal["scattering"]]
    # calibration_args_guess = exp["calibration_args_guess"]

    gl_to_mm = eval('radioSphere.calibrateAttenuation.gl_to_mm_' + exp["fit_order"])
    mm_to_gl = eval('radioSphere.calibrateAttenuation.mm_to_gl_' + exp["fit_order"])

    calibration_args, scattering = radioSphere.calibrateAttenuation.optimiseAttenuation(
        radioGL,
        calibration_args_guess,
        gl_to_mm,
        mm_to_gl,
        positionsXYZmm,
        numpy.array([exp["radiusMM"]]*exp["nSpheres"]),
        exp["sourceDetectorDistMM"],
        exp["pixelSizeMM"]*exp["binning"],
        radioGL.shape,
        iterations=50,
        projector="cupy",
        focalSpotSize=exp["focalSpotSize"],
        verbose=exp["verbose"],
        GRAPH=True,
        # transformationCentreMM=exp["transformationCentreMM"],
        # transformationMatrix=exp["transformationMatrix"]
    )

    print("Updated attenuation law:")
    # print(f"    Location: {location_guess}")
    print(f"    Calibration: {calibration_args}")
    print(f"    Scattering: {scattering}")

    with open(exp["dataFolder"] + exp["fitManyParamsPath"], 'w') as f:
        calibration = {}
        calibration["fit_args"] = calibration_args.tolist()
        calibration["scattering"] = scattering
        json5.dump(calibration, f, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
