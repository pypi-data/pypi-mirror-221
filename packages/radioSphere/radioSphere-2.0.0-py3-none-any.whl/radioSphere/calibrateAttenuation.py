import math
import numpy
import matplotlib.pyplot as plt
import tifffile
import radioSphere
from scipy.optimize import curve_fit, minimize
from progressbar import progressbar


def cubicFit(x, l, n, m, c):
    return l * x**3 + n * x**2 + m * x + c


def quadraticFit(x, n, m, c):
    return n * x**2 + m * x + c


def linearFit(x, m, c):
    return m * x + c


def linearFitNoIntercept(x, m):
    return m * x


# LINEAR FIT --- JUST FOR TESTING
def mm_to_gl_linear(MM, mu):
    return numpy.exp(-mu * MM)


def gl_to_mm_linear(GL, mu):
    return -numpy.log(GL) / mu


# FIT FROM STEPHANE'S PAPER https://aip.scitation.org/doi/pdf/10.1063/1.5080540
def mm_to_gl_stephane(MM, a, b, c):
    mu_eff = a + b / (MM**c)
    return numpy.exp(-mu_eff * MM)


def gl_to_mm_stephane(GL, a, b, c):
    # CANNOT INVERT THIS :(
    # return -numpy.log(GL) / mu_eff
    return None


# QUADRATIC FIT
def mm_to_gl_quadratic(MM, a, b):
    return numpy.exp(-a * MM**2 - b * MM)


def gl_to_mm_quadratic(GL, a, b):
    with numpy.errstate(invalid="ignore"):
        MM = numpy.nan_to_num(numpy.sqrt(b**2 - 4 * a * numpy.log(GL)) - b) / (2 * a)
    return MM

# REDUCED CUBIC FIT (NO QUADRATIC TERM)
def mm_to_gl_reduced_cubic(MM, a, b):
    with numpy.errstate(over="ignore",invalid="ignore"):
        return numpy.nan_to_num(numpy.exp(-a*MM**3 - b*MM))

def gl_to_mm_reduced_cubic(GL, a, b):
    # https://www.wolframalpha.com/input?i=solve+y%3Dexp%28-a*x%5E3+-+b*x%29+for+x+where+x%3E0%2C+a%3E0%2C+b%3E0%2C+0%3Cy%3C1
    with numpy.errstate(invalid="ignore"):
        MM = (2**(1/3)*(numpy.sqrt(3)*numpy.sqrt(a**3*(27*a*(numpy.log(1/GL)**2) + 4*b**3)) + 9*a**2*numpy.log(1/GL))**(2/3) - 2*3**(1/3)*a*b)/(6**(2/3)*a*(numpy.sqrt(3)*numpy.sqrt(a**3*(27*a*numpy.log(1/GL)**2 + 4*b**3)) + 9*a**2*numpy.log(1/GL))**(1/3))
    return numpy.nan_to_num(MM)

def getPathLengthThroughSphere(p, r, sdd, sod):
    """
    Get the path length of a ray passing through a sphere. Schematic diagram is provided in the supplementary
    methods section of the first (only?) radiosphere paper.

    Parameters
    ----------
        p : float
            The distance in mm along the detector panel from the centre.

        r : float
            The particle radius in mm.

        sdd : float
            The source-detector distance in mm.

        sod : float
            The source-object distance in mm.

    Returns
    -------
        L : float
            The path length through the sphere in mm. If the path lies outside the sphere, returns 0.
    """
    try:
        p = float(p)
        # print p,
        alpha = math.atan(p / sdd)
        # print alpha
        beta = math.asin(sod * math.sin(alpha) / r)
        L = 2.0 * r * math.sin(math.pi / 2.0 - beta)
        # print numpy.rad2deg(alpha), numpy.rad2deg(beta), L
        return L
    except:
        return 0.0


def generateFitParameters(
    calibSphereLog,
    pixelSizeMM,
    sourceDetectorDistMM,
    sourceObjectDistanceMM,
    radiusMM,
    centreYXpx,
    fitFunction=linearFit,
    outputPath=False,
    verbose=False,
):
    """
    Fit an attenuation law to a logged normalised radiograph of a single particle.

    Parameters
    ----------
        calibSphereLog : 2D numpy array of floats
            A radiograph of a single particle divided by the background intensity and then logged.

        pixelSizeMM : float
            The size of a single pixel in mm on the detector panel.

        sourceDetectorDistMM: float
            The source-detector distance in mm.

        sourceObjectDistanceMM: float
            The source-object distance in mm.

        radiusMM : float
            The particle radius in mm.

        centreYXpx : 1D numpy array of floats
             The y and x location of the centre of the particle in pixels.

        fitFunction : function handle (optional)
            The fitting function to use. By default fit a linear fitting law.
            Options are `cubicFit`, `quadraticFit`, `linearFit` and `linearFitNoIntercept`

        outputPath : string (optional)
            A path to save the fit as an `npy` file.

        verbose : bool (optional)
            Show the fit on a graph. Default is False.

    Returns
    -------
        L: float
            The path length through the sphere in mm. If the path lies outside the sphere, returns 0.
    """
    # alphaMax = math.asin(radiusMM / sourceObjectDistanceMM)
    # pmax = math.tan(alphaMax) * sourceDetectorDistMM

    # Pixel positions going -x from the middle of the sphere in MM
    pixelPoints = numpy.array(range(int(round(centreYXpx[0])))[::-1])
    pixelPointsMMdetector = pixelPoints * pixelSizeMM

    points = []
    # for pn, pMMdet in enumerate(pixelPointsMMdetector[0:130]):
    for pn, pMMdet in enumerate(pixelPointsMMdetector):
        # if pMMdet < pmax:
        L = getPathLengthThroughSphere(pMMdet, radiusMM, sourceDetectorDistMM, sourceObjectDistanceMM)
        if L > 0:
            points.append(
                [
                    L,
                    calibSphereLog[pixelPoints[-pn], int(centreYXpx[1])],
                    pixelPoints[-pn],
                ]
            )
    points = numpy.array(points)

    poptN, pcov = curve_fit(fitFunction, points[:, 1], points[:, 0])

    if outputPath:
        numpy.save(outputPath, poptN)

    if verbose:
        D = 150
        plt.subplot(121)
        plt.imshow(calibSphereLog)
        plt.colorbar()
        plt.plot(int(centreYXpx[1]) * numpy.ones_like(points[:, 2]), points[:, 2], "w--")
        plt.plot(int(centreYXpx[1]), points[0, 2], "wx")
        plt.plot(int(centreYXpx[1]), points[-1, 2], "wx")
        plt.xlim(centreYXpx[1] - D, centreYXpx[1] + D)
        plt.ylim(centreYXpx[0] - D, centreYXpx[0] + D)
        plt.subplot(122)
        plt.plot(
            points[:, 1], points[:, 0], "k.", label="Measured value"
        )  # Measured calib sphere with 130kV\nand 1.00mm Cu filter
        plt.plot(
            points[:, 1],
            fitFunction(points[:, 1], *poptN),
            "k-",
            alpha=0.5,
            label="Fit",
        )
        plt.ylabel("Path length inside\nsphere (mm)")
        # plt.ylim([0, max(points[:,0])])
        plt.xlabel(r"Log Attenuation $\ln(I/I_0)$")
        plt.legend(loc=0)

        # plt.subplots_adjust(bottom=0.21,top=0.99,right=0.99,left=0.16)
        plt.show()
        # plt.savefig('./figures/experimental-attenuationCalibration.pdf')

    return poptN


def testCalibration(
    args,
    radioGL,
    radiiMM,
    location_guess,
    detectorResolution,
    pixelSizeMM,
    sourceDetectorDistMM,
    mm_to_gl,
    projector,
    focalSpotSize,
):
    
    calibration_args = args[:-1]
    scattering = args[-1]
    
    # Update our guess of the calibration with the new positions
    radioMM_guess = radioSphere.projectSphere.projectSphereMM(
        location_guess,
        radiiMM,
        detectorResolution=detectorResolution,
        pixelSizeMM=pixelSizeMM,
        sourceDetectorDistMM=sourceDetectorDistMM,
        projector=projector,
        scattering=scattering,
        focalSpotSize=focalSpotSize,
    )

    radioGL_guess = mm_to_gl(radioMM_guess, *calibration_args)
    err = numpy.sum(numpy.square(radioGL_guess - radioGL))
    return err


def getLocationAndAttenuationForSpheres(
    radioGL,
    args,
    gl_to_mm,
    mm_to_gl,
    location_guess,
    radiiMM,
    sourceDetectorDistMM,
    pixelSizeMM,
    detectorResolution,
    projector="numpy",
    iterations=10,
    perturbationMM=None,
    focalSpotSize=0,
    verbose=True,
    GRAPH=False
):
    calibration_args = numpy.array(args[:-1])
    scattering = args[-1]

    for i in progressbar(range(iterations)):

        # Update our calibration curve
        bounds = [[0,numpy.inf]]*len(args)
        res = minimize(
            testCalibration,
            args,
            args=(
                radioGL,
                radiiMM,
                location_guess,
                detectorResolution,
                pixelSizeMM,
                sourceDetectorDistMM,
                mm_to_gl,
                projector,
                focalSpotSize,
            ),
            bounds=bounds
        )

        l = 0.5
        calibration_args = l*res.x[:-1] + (1-l)*calibration_args
        scattering = l*res.x[-1] + (1-l)*scattering

        # Update our guess of the particle location
        radioMM_guess = gl_to_mm(radioGL, *calibration_args)

        new_location = radioSphere.optimisePositions.optimiseSensitivityFields(
            radioMM_guess,
            location_guess,
            radiiMM,
            # minDeltaMM=0.00001,
            iterationsMax=5,
            GRAPH=False,
            perturbationMM=perturbationMM,
            projector=projector,
            sourceDetectorDistMM=sourceDetectorDistMM,
            pixelSizeMM=pixelSizeMM,
            detectorResolution=detectorResolution,
            focalSpotSize=focalSpotSize,
            scattering=0.0,
            verbose=verbose,
            DEMcorr=False,
        )
        location_guess = l*new_location + (1-l)*location_guess

        if GRAPH:
            radioMM_guess = radioSphere.projectSphere.projectSphereMM(
                location_guess,
                radiiMM,
                detectorResolution=detectorResolution,
                pixelSizeMM=pixelSizeMM,
                sourceDetectorDistMM=sourceDetectorDistMM,
                projector=projector,
                scattering=scattering,
                focalSpotSize=focalSpotSize,
            )

            radioGL_guess = mm_to_gl(radioMM_guess, *calibration_args)
            err = numpy.square(radioGL_guess - radioGL)

            lim = numpy.max(numpy.sqrt(err))  # *0.9
            plt.ion()
            plt.clf()
            plt.subplot(231)
            plt.title("ground truth GL")
            plt.imshow(radioGL)
            plt.colorbar()
            plt.subplot(232)
            plt.title("guessed GL")
            plt.imshow(radioGL_guess, vmin=numpy.min(radioGL), vmax=numpy.max(radioGL))
            plt.colorbar()
            plt.subplot(233)
            plt.title("Residual")
            plt.imshow(radioGL - radioGL_guess, cmap="bwr", vmin=-lim, vmax=lim)
            plt.colorbar()
            plt.subplot(234)
            plt.plot(radioGL.flatten(), radioGL_guess.flatten(), "k.")
            plt.xlabel("ground truth GL")
            plt.ylabel("guessed GL")
            plt.subplot(235)
            plt.hist(err.flatten(), bins=20, log=True)
            plt.xlabel("Error value")
            plt.ylabel("Count")
            plt.subplots_adjust(wspace=0.5)
            plt.pause(1e-6)    
    return location_guess, calibration_args, scattering

def optimiseAttenuation(
    radioGL,
    args,
    gl_to_mm,
    mm_to_gl,
    location_guess,
    radiiMM,
    sourceDetectorDistMM,
    pixelSizeMM,
    detectorResolution,
    projector="numpy",
    iterations=10,
    focalSpotSize=0,
    verbose=True,
    GRAPH=False,
):

    bounds = [[0,numpy.inf]]*len(args)
    res = minimize(
        testCalibration,
        args,
        args=(
            radioGL,
            radiiMM,
            location_guess,
            detectorResolution,
            pixelSizeMM,
            sourceDetectorDistMM,
            mm_to_gl,
            projector,
            focalSpotSize,
        ),
        bounds=bounds
    )
    calibration_args = res.x[:-1]
    scattering = res.x[-1]
    if GRAPH:
        radioMM_guess = radioSphere.projectSphere.projectSphereMM(
            location_guess,
            radiiMM,
            detectorResolution=detectorResolution,
            pixelSizeMM=pixelSizeMM,
            sourceDetectorDistMM=sourceDetectorDistMM,
            projector=projector,
            scattering=scattering,
            focalSpotSize=focalSpotSize,
        )

        radioGL_guess = mm_to_gl(radioMM_guess, *calibration_args)
        err = numpy.square(radioGL_guess - radioGL)

        lim = numpy.max(numpy.sqrt(err))  # *0.9

        plt.clf()
        plt.subplot(231)
        plt.title("ground truth GL")
        plt.imshow(radioGL)
        plt.colorbar()
        plt.subplot(232)
        plt.title("guessed GL")
        plt.imshow(radioGL_guess, vmin=numpy.min(radioGL), vmax=numpy.max(radioGL))
        plt.colorbar()
        plt.subplot(233)
        plt.title("Residual")
        plt.imshow(radioGL - radioGL_guess, cmap="bwr", vmin=-lim, vmax=lim)
        plt.colorbar()
        plt.subplot(234)
        plt.plot(radioGL.flatten(), radioGL_guess.flatten(), "k.")
        plt.xlabel("ground truth GL")
        plt.ylabel("guessed GL")
        plt.subplot(235)
        plt.hist(err.flatten(), bins=20, log=True)
        plt.xlabel("Error value")
        plt.ylabel("Count")
        plt.subplots_adjust(wspace=0.5)
        # plt.pause(1e-6)
        plt.show()    
    
    return calibration_args, scattering

if __name__ == "__main__":
    plt.style.use("./radioSphere/radioSphere.mplstyle")

    calibSpherePath = "./data/2021-02-09-EddyBillesNanoBis/7mm-AVG64.tif"
    backgroundPath = "./data/2021-02-09-EddyBillesNanoBis/I0-AVG64.tif"
    outputPath = "./cache/fit-log-linear.npy"

    # Load images
    calibSphere = tifffile.imread(calibSpherePath).astype(float) / tifffile.imread(backgroundPath).astype(float)
    calibSphereLog = numpy.log(calibSphere)

    # Projection geometry stuff
    binning = 4
    pixelSizeMM = 0.127 * float(binning)
    sourceDetectorDistMM = 242.597  # from XAct
    focalSpotSize = 0.05  # 50 microns? total guess

    radiusMM = 7 / 2
    sourceObjectDistanceMM = sourceDetectorDistMM * (
        radiusMM / 71 / pixelSizeMM
    )  # 71 pixels across diameter, so 51um/px, pixels 0.508 mm
    # uncertain parameter, this wiggles it
    sourceObjectDistanceMM += 0.5
    # print("SOD = ", sourceObjectDistanceMM)
    centreYXpx = numpy.array([229, 183])

    poptN = generateFitParameters(
        calibSphereLog,
        pixelSizeMM,
        sourceDetectorDistMM,
        sourceObjectDistanceMM,
        radiusMM,
        centreYXpx,
        outputPath=outputPath,
        verbose=False,
    )

    print("Eye fitting method:")
    print(f"    X Location: {sourceObjectDistanceMM}")
    print(f"    Calibration: {poptN}")

    # Our best guess from eye fitting for the location and calibration params
    location_guess = numpy.array([[sourceObjectDistanceMM, 0, 0]])
    # FOR LINEAR MODEL
    args = [
        1e-2,
        1e-2,
    ]  # calibration AND scattering AND focalSpotSize in one list. last value is scattering

    (location_guess, calibration_args, scattering,) = getLocationAndAttenuationForSingleSphere(
        calibSphere,
        args,
        gl_to_mm_linear,
        mm_to_gl_linear,
        location_guess,
        radiusMM,
        sourceDetectorDistMM,
        pixelSizeMM,
        calibSphere.shape,
        iterations=20,
        projector="cupy",
        focalSpotSize=focalSpotSize,
        verbose=True,
    )

    print("Linear attenuation law:")
    print(f"    Location: {location_guess}")
    print(f"    Calibration: {calibration_args}")
    print(f"    Scattering: {scattering}")
    