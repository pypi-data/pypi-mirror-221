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
    
    # Load images
    I    = tifffile.imread(exp["dataFolder"] + exp["calibSphere"]).astype(float)
    dark = tifffile.imread(exp["dataFolder"] + exp["darkField"]).astype(float)
    bg   = tifffile.imread(exp["dataFolder"] + exp["background"]).astype(float)
    calibSphere = ( I - dark ) / ( bg - dark )
    calibSphere = scipy.ndimage.zoom(calibSphere, 1./exp["binning"])

    # zoomFactor = exp["sourceObjectDistanceMM"]/exp["sourceDetectorDistMM"]
    centreZYpx = numpy.unravel_index(numpy.argmin(calibSphere),calibSphere.shape)
    
    location_guess = numpy.array([[exp["sourceObjectDistanceMM"],
                                   -(centreZYpx[1] - calibSphere.shape[1]/2)*exp["pixelSizeMM"]*exp["binning"],
                                   (centreZYpx[0] - calibSphere.shape[0]/2)*exp["pixelSizeMM"]*exp["binning"]]])
    print(location_guess)

    gl_to_mm = eval('radioSphere.calibrateAttenuation.gl_to_mm_' + exp["fit_order"])
    mm_to_gl = eval('radioSphere.calibrateAttenuation.mm_to_gl_' + exp["fit_order"])
    (location_guess, calibration_args, scattering,) = radioSphere.calibrateAttenuation.getLocationAndAttenuationForSpheres(
        calibSphere,
        exp["calibration_args_guess"],
        gl_to_mm,
        mm_to_gl,
        location_guess,
        numpy.array([exp["radiusMM"]]),
        exp["sourceDetectorDistMM"],
        exp["pixelSizeMM"]*exp["binning"],
        calibSphere.shape,
        iterations=50,
        projector="cupy",
        focalSpotSize=exp["focalSpotSize"],
        verbose=exp["verbose"],
        GRAPH=True,
        perturbationMM=[1,1,1]
        # transformationCentreMM=exp["transformationCentreMM"],
        # transformationMatrix=exp["transformationMatrix"]
    )

    print("Linear attenuation law:")
    print(f"    Location: {location_guess}")
    print(f"    Calibration: {calibration_args}")
    print(f"    Scattering: {scattering}")

    with open(exp["dataFolder"] + exp["fitSingleParamsPath"], 'w') as f:
        calibration = {}
        calibration["location"] = location_guess[0].tolist()
        calibration["fit_args"] = calibration_args.tolist()
        calibration["scattering"] = scattering
        json5.dump(calibration, f, indent=2, sort_keys=True)
        # f.write(str(scattering))
    # exp["initial_particle_location_measured"] = location_guess
    # exp["calibration_args_measured"] = calibration_args
    # exp["scattering_measured"] = scattering
    

if __name__ == '__main__':
    main()
