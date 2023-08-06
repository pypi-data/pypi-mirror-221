"""
Library of RadioSphere spheres detection functions.
"""

import radioSphere.projectSphere
import os
import numpy
import scipy.ndimage
import scipy.signal
import scipy.stats
from scipy.spatial import distance

import matplotlib.pyplot as plt
import tifffile

import multiprocessing
from tqdm import tqdm

# Global number of processes
nProcessesDefault = multiprocessing.cpu_count()


# helper projector function operating on fx (approximation of "indicator" function)
def _PIprojector(f):
    g = f.copy()
    g[f < 0.0] = 0.0  # discard negative values
    g = numpy.round(g)  # round to the nearest integer
    return g


# Bottom of page 8 in TomoPack.pdf ---< just take peaks in a 3x3 pixel area, and weight by all of the mass in that area
_kernel = numpy.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16.0  # gaussian kernel 2D


def _filter_maxima(f, debug=False, removeNegatives=False):
    # This is making our complex result into a scalar result
    f_abs = numpy.abs(f)

    # Remove negatives -- however keeping negatives can help sharpen the result of the convolution
    if removeNegatives:
        f_abs[f < 0] = 0

    fxConvolved = scipy.ndimage.convolve(f_abs, _kernel)
    fxConvolvedMaxFiltered = scipy.ndimage.maximum_filter(fxConvolved, size=(3, 3))

    peaks = fxConvolved == fxConvolvedMaxFiltered
    masses = peaks * fxConvolved

    if debug:
        plt.subplot(2, 3, 1)
        plt.imshow(f)
        plt.title("f_x")
        plt.colorbar()

        plt.subplot(2, 3, 2)
        plt.imshow(fxConvolved)
        plt.colorbar()
        plt.title("fxConvolved")

        plt.subplot(2, 3, 3)
        plt.imshow(fxConvolvedMaxFiltered)
        plt.colorbar()
        plt.title("fxConvolvedMaxFiltered")

        plt.subplot(2, 3, 4)
        plt.imshow(peaks)
        plt.colorbar()
        plt.title("peaks")

        plt.subplot(2, 3, 5)
        plt.imshow(masses)
        plt.colorbar()
        plt.title("masses")
        plt.show()

    return masses

def getKTrustSNR(
    sourceObjectDistMM,
    radiusMM,
    detectorResolution,
    pixelSizeMM,
    sourceDetectorDistMM,
    projector="numba",
    scattering=0.0,
    iterations=100,
    SNRCutoff=2,
):

    psiMMFFT = numpy.zeros([iterations, *detectorResolution],dtype=complex)

    for i in range(iterations):
        zoomLevel = sourceDetectorDistMM/sourceObjectDistMM
        centreOfRotationMM = [
            sourceObjectDistMM,
            1 * pixelSizeMM / zoomLevel * (numpy.random.rand() - 0.5),
            1 * pixelSizeMM / zoomLevel * (numpy.random.rand() - 0.5),
        ]

        psiMM = radioSphere.projectSphere.projectSphereMM(
            numpy.array([centreOfRotationMM]),
            numpy.array([radiusMM]),
            detectorResolution=detectorResolution,
            pixelSizeMM=pixelSizeMM,
            sourceDetectorDistMM=sourceDetectorDistMM,
            projector=projector,
            scattering=scattering
        )
        psiMMFFT[i] = numpy.fft.fft2(psiMM)

    psiMMFFT_inv_median = numpy.median(1.0 / numpy.abs(psiMMFFT), axis=0)
    psiMMFFT_inv_mad = scipy.stats.median_abs_deviation(1.0 / numpy.abs(psiMMFFT), axis=0)

    psiMMFFT_SNR = psiMMFFT_inv_median / psiMMFFT_inv_mad

    # psiMMFFT_SNR = numpy.min(numpy.abs(psiMMFFT), axis=0)

    return psiMMFFT_SNR > SNRCutoff


def tomopack(
    radioMM,
    psiMM,
    maxIterations=50,
    l=0.5,
    projector="numba",
    scattering=0.0,
    kTrustMethod="iterative",
    epsilon=1,
    kTrustRatio=0.75,
    kTrust=None,
    verbose=False,
    graphShow=False,
):
    """
    'tomopack' FFT-based algorithm for sphere identification by Stéphane Roux.
    the FFT of psiMM as a structuring element to pick up projected spheres in radioMM
    using a parallel projection hypothesis.

    Parameters
    ----------
        radioMM : 2D numpy array of floats
            Radiography containing "distance" projections in mm
            This is typically the result of mu*log(I/I_0)

        psiMM : 2D numpy array of floats
            A (synthetic) projection in mm of a single sphere in the centre of the detector
            This is the structuring element used for FFT recognition.
            Should be same size as radioMM

        maxIterations : int, optional
            Number of iterations to run the detection for
            Default = 50

        l : float, ptional
            "Lambda" parameter which controls relaxation in the iterations
            Default = 0.5

        epsilon : float, optional
            Trust cutoff wavelengths in psi.
            If the radiograph is in mm so is this parameter

        kTrustRatio : float, optional
            Ratio of cutoff psi wavelengths. Keep this fraction of wavelengths and discard the ones with lower FFT values.
            Default = 0.75
        
        kTrustMethod : str, optional
            'scalar', 'iterative' or 'SNR'
            Default = 'iterative'

        verbose : bool, optional
            Get to know what the function is really thinking
            Default = False

        graphShow : bool, optional
            Show evolution of fx during iterations, and final one together with radio and psi
            Default = False

    Returns
    -------
        fx : 2D numpy array
            The approximation of the `indicator` function
            Same size as radioMM, with high values where we think spheres centres are
            Consider using `indicatorFunctionToDetectorPositions()` to get the IJ detector coordinates of the centres

    """
    assert len(radioMM.shape) == 2, "detectSpheres.tomopack(): radio should be a 2D array"
    assert len(psiMM.shape) == 2, "detectSpheres.tomopack(): psi should be a 2D array"
    assert len(psiMM.shape) == len(
        radioMM.shape
    ), "detectSpheres.tomopack(): psi and radioMM should be same size"

    # compute FFT of input radio
    radioMMFFT = numpy.fft.fft2(radioMM)

    # compute FFT of input psi (structuring element or shape function)
    # psiMM_FFT = numpy.fft.fft2(psiMM)
    # 2021-10-26 OS: phase shift of psi so that zero phase angle is positioned at the centre of the detector
    # avoids the HACK of shifting fx later
    psiMMFFT = numpy.fft.fft2(numpy.fft.fftshift(psiMM))

    # Naiive approach to compute fx by a direct division and deconvolution
    with numpy.errstate(divide="ignore", invalid="ignore"):
        fkNaiive = radioMMFFT / psiMMFFT
    fxNaiive = numpy.fft.ifft2(fkNaiive)

    # Prepare for iterations
    fx = numpy.zeros_like(radioMM)
    if kTrustMethod == 'SNR':
        pass # already computed
    elif kTrustMethod == "iterative":
        epsilon = 1e-5
        kTrust = numpy.abs(psiMMFFT) > epsilon
        while kTrust.sum() / kTrust.shape[0] / kTrust.shape[1] > kTrustRatio:
            epsilon *= 1.5
            kTrust = numpy.abs(psiMMFFT) > epsilon
        fxOld = epsilon * numpy.ones_like(radioMM)
    else:
        fxOld = epsilon * numpy.ones_like(radioMM)
        kTrust = numpy.abs(psiMMFFT) > epsilon

    if verbose:
        print(
            f"kTrust maintains {100*kTrust.sum()/kTrust.shape[0]/kTrust.shape[1]}% of wavenumubers"
        )

    it = 0
    # Start iterations as per Algorithm 1 in TomoPack
    #   Objective: get a good indicator function fx
    while (
        numpy.linalg.norm(fx - fxOld) > 1e-8
    ):  # NOTE: Using a different epsilon here (OS: could be an input perhaps)
        if graphShow:
            plt.clf()

        fxOld = fx.copy()
        fk = numpy.fft.fft2(fx)
        fk[kTrust] = fkNaiive[kTrust]
        # fx = numpy.fft.fftshift(numpy.fft.ifft2(fk)) # importing HACK from 1D version
        fx = numpy.fft.ifft2(fk)
        fx = fx + l * (_PIprojector(fx) - fx)

        if graphShow:
            plt.suptitle(f"Iteration Number = {it}", fontsize=10)
            plt.imshow(numpy.real(fx), vmin=0, vmax=1)
            plt.colorbar()
            plt.pause(0.001)
        it += 1

        if it > maxIterations:
            if verbose:
                print('\tNo convergence before max iterations"')
            # fx = numpy.zeros_like(fx) # NOTE: Should we return a zero indicator function?
            break

    if graphShow:
        from matplotlib.colors import LogNorm

        plt.figure(figsize=[8, 6])

        plt.subplot(321)
        plt.title(r"$p(x)$")
        plt.imshow(radioMM)
        plt.colorbar()

        plt.subplot(322)
        plt.title(r"$\psi(x)$")
        plt.imshow(psiMM, vmin=radioMM.min(), vmax=radioMM.max())
        plt.colorbar()

        plt.subplot(323)
        plt.title(r"$|\tilde{p}(k)|$")
        plt.imshow(numpy.abs(numpy.fft.fftshift(radioMMFFT)), norm=LogNorm(vmin=0.1, vmax=10**5))
        plt.colorbar()

        plt.subplot(324)
        plt.title(r"$|\tilde{\psi}(k)|$")
        plt.imshow(numpy.abs(numpy.fft.fftshift(psiMMFFT)), norm=LogNorm(vmin=0.1, vmax=10**5))
        plt.colorbar()

        plt.subplot(325)
        plt.title(r"Estimated $f(x)$")
        plt.imshow(numpy.real(fx), vmin=0, vmax=1)
        plt.colorbar()

        psiMMFFTtrusted = psiMMFFT.copy()
        psiMMFFTtrusted[~kTrust] = numpy.nan
        plt.subplot(326)
        plt.title(r"$|\tilde{\psi}(ktrust)|$")
        plt.imshow(
            numpy.abs(numpy.fft.fftshift(psiMMFFTtrusted)), norm=LogNorm(vmin=0.1, vmax=10**5)
        )
        plt.colorbar()

        plt.subplots_adjust(hspace=0.5)
        plt.show()

    return numpy.real(fx)


def indicatorFunctionToDetectorPositions(fx, scanFixedNumber=None, massThreshold=0.5, debug=False):
    """
    This function takes an indicator function fx and returns peaks on the detector.
    fx can be a 2D array, which is directly the raw output from tomopack, or a 3D array, if a series of tomopack was run.

    In both cases, the peaks returned as a (n x 3) 2D array, where the first column corresponds to the slice of the fx series that peaks were found. If a 2D input fx is passed, the first column is always 0 (zero slice in 3D).

    Parameters
    ----------
        fx : 2D or 3D numpy array of floats
            Approximation of indicator function
            For a divergent beam this should be a 3D array

        scanFixedNumber : int, optional
            The number of spheres scanned
            If None, peaks will be thresholded based on `massThreshold` (below)
            Default = None

        massThreshold : float, optional
            Threshold for accepting the result of the filtered indicator function
            Activated if `scanFixedNumber` (above) is None
            Default = 0.5

        debug : bool, optional
            Show debug graphs (especially in the maximum filtering)
            Default = False

    Returns
    -------
        peaksPOSnJI : (N x 3) 2D numpy array
            Positions of spheres centres (N) on the detector (slice, rows, coloumns (JI))
            Where slice is the CORx slice the resonance peak falls in (only makes sense for a 3D fx)

    """

    assert (
        len(fx.shape) == 2 or len(fx.shape) == 3
    ), "detectSpheres.indicatorFunctionToDetectorPositions(): Need 2D or 3D array"

    twoD = False
    if len(fx.shape) == 2:
        twoD = True
        # we're not in a divergent beam, let's filter the maxima of fx
        fx = _filter_maxima(fx, debug=debug)
        # and add a fake axis to homogenise the output
        fx = fx[numpy.newaxis, ...]

    if scanFixedNumber:
        # get the indices of all of the peaks, from highest to lowest
        sortedPeakIndices = numpy.argsort(fx, axis=None)[::-1]
        # get just the first scanFixedNumber of those and put them into a scanFixedNumber x 3 array
        peaksJI = numpy.vstack(numpy.unravel_index(sortedPeakIndices[:scanFixedNumber], fx.shape)).T
    else:
        filteredPeaks = fx > massThreshold
        if filteredPeaks.sum() == 0:
            print(
                "\ndetectSpheres.indicatorFunctionToDetectorPositions(): massThreshold too high to detect any peaks. That's probably not good..."
            )
        peaksJI = numpy.argwhere(filteredPeaks)

    return peaksJI


def detectorPeaksTo3DCoordinates(
    peaksJI, CORxPos, detectorResolution=[512, 512], pixelSizeMM=0.1, sourceDetectorDistMM=100
):
    """
    This function takes positions on the detector (identified peaks of the indicator function) and a set of positions in the x-ray direction (where a series of tomopack was run) and returns the corresponding XYZ coordinates

    Parameters
    ----------
        peaksJI : 2D numpy array of int
            Positions of spheres centres on the detector (rows, coloumns (JI))

        CORxPos : 1D numpy array of floats
            Positions in the x-ray direction on which a series of tomopack was run
            If not a divergent beam, this should be an array full of the same number -- COR

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        detectorResolution : 2-component list of ints, optional
            Number of pixels rows, columns of detector
            Default = [512,512]

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector.
            Set as numpy.inf for parallel projection
            Default = 100

    Returns
    -------
        posXYZmm : (N x 3) 2D numpy array
            Positions of spheres centres (N) in 3D (XYZ) in mm
            If not a divergent beam, posX is the input COR

    """

    assert len(peaksJI.shape) == 2, "detectSpheres.detectorPeaksTo3DCoordinates(): Need a 2D array"

    posXYZmm = numpy.zeros([peaksJI.shape[0], 3])

    for i in range(posXYZmm.shape[0]):
        # X -- look up which CORx slice the maximum falls in, this could be interpolated instead of rounded
        posXYZmm[i, 0] = CORxPos[int(numpy.round(peaksJI[i, 0]))]

        # detector I gives real position Y in mm
        yPosDetMM = -1 * (peaksJI[i, 2] - detectorResolution[1] / 2.0) * pixelSizeMM

        # detector J gives real position Z in mm
        zPosDetMM = -1 * (peaksJI[i, 1] - detectorResolution[0] / 2.0) * pixelSizeMM

        # And now scale down by zoom factor
        # Y
        posXYZmm[i, 1] = yPosDetMM * (posXYZmm[i, 0] / sourceDetectorDistMM)
        # Z
        posXYZmm[i, 2] = zPosDetMM * (posXYZmm[i, 0] / sourceDetectorDistMM)

    return posXYZmm


def computeFxAndPsiSeries(
    radioMM,
    radiusMM,
    CORxPositions,
    pixelSizeMM=0.1,
    sourceDetectorDistMM=100,
    blur=0.0,
    projector="numba",
    scattering=0.0,
    maxIterations=50,
    l=0.5,
    kTrustMethod="iterative",
    epsilon=1,
    kTrustRatio=0.75,
    SNRCutoff=2,
    nProcesses=nProcessesDefault,
):
    """
    This function takes in a single divergent projection and positions along the ray direction, and returns
    the corresponding indicator function (fx) and structuring element (psi) series by running (in parallel) a series of tomopack

    Parameters
    ----------
        radioMM : 2D numpy array of floats
            Radiography containing "distance" projections in mm
            This is typically the result of mu*log(I/I_0)

        radiusMM : float
            Particle radius in mm

        CORxPositions : 1D numpy array of floats
            Positions in the x-ray direction on which a series of tomopack will be run

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector.
            Set as numpy.inf for parallel projection
            Default = 100

        blur : float, optional
            Sigma of blur to pass to `scipy.ndimage.gaussian_filter` to
            blur the synthetic psi
            Default = 0

        maxIterations : int, optional
            Number of iterations to run tomopack
            Default = 50

        l : float, optional
            "Lambda" parameter which controls relaxation in tomopack iterations
            Default = 0.5

        epsilon : float, optional, or 'iterative'
            Trust cutoff wavelengths in psi
            If the radiograph is in mm so is this parameter
            Default = 'iterative' -- updating until `kTrustRatio` (below) is reached

        kTrustRatio : float, optional
            Ratio of cutoff psi wavelengths
            Default = 0.75
        
        kTrustMethod : str, optional
            'scalar', 'iterative' or 'SNR'
            Default = 'iterative'

        nProcesses : integer, optional
            Number of processes for multiprocessing
            Default = number of CPUs in the system


    Returns
    -------
        fXseries : 3D numpy array of floats
            Indicator function series along the x-ray direction
            Its shape is (len(CORxPositions), radioMM.shape[0],  radioMM.shape[1])

        psiXseries : 3D numpy array of floats
            Structuring element series along the x-ray direction
            Its shape is (len(CORxPositions), radioMM.shape[0],  radioMM.shape[1])
    """

    # Create empty arrays
    fXseries = numpy.zeros((len(CORxPositions), radioMM.shape[0], radioMM.shape[1]))
    psiXseries = numpy.zeros_like(fXseries)
    psiMMseries = numpy.zeros_like(fXseries)

    psiRefMM = radioSphere.projectSphere.projectSphereMM(
        numpy.array([[(CORxPositions.min() + CORxPositions.max()) / 2, 0.0, 0.0]]),
        numpy.array([radiusMM]),
        detectorResolution=radioMM.shape,
        pixelSizeMM=pixelSizeMM,
        sourceDetectorDistMM=sourceDetectorDistMM,
        blur=blur,
        projector=projector,
        scattering=scattering
    )

    pbar = tqdm(total=len(CORxPositions))
    finishedPos = 0

    # Loop over CORx
    # global computeOneCOR

    def computeOneCOR(pos):
        CORxPos = CORxPositions[pos]
        psiMM = radioSphere.projectSphere.projectSphereMM(
            numpy.array([[CORxPos, 0.0, 0.0]]),
            numpy.array([radiusMM]),
            detectorResolution=radioMM.shape,
            pixelSizeMM=pixelSizeMM,
            sourceDetectorDistMM=sourceDetectorDistMM,
            blur=blur,
            projector=projector,
            scattering=scattering
        )
        if kTrustMethod == 'SNR':
            kTrust = getKTrustSNR(
            CORxPos,
            radiusMM,
            radioMM.shape,
            pixelSizeMM,
            sourceDetectorDistMM,
            SNRCutoff=SNRCutoff
        )
        else:
            kTrust = None

        fX = radioSphere.detectSpheres.tomopack(
            radioMM, psiMM, maxIterations=maxIterations, l=l, kTrustMethod=kTrustMethod, kTrustRatio=kTrustRatio, epsilon=epsilon, kTrust=kTrust
        )
        psiX = radioSphere.detectSpheres.tomopack(
            psiRefMM, psiMM, maxIterations=maxIterations, l=l, kTrustMethod=kTrustMethod, kTrustRatio=kTrustRatio, epsilon=epsilon, kTrust=kTrust
        )

        return pos, fX, psiX

    for i in range(len(CORxPositions)):
        tt, fX, psiX = computeOneCOR(i)
        fXseries[i] = fX
        psiXseries[i] = psiX
        pbar.update(i)

    # Run multiprocessing
    # with multiprocessing.Pool(processes=nProcesses) as pool:
    #     for returns in pool.imap_unordered(computeOneCOR, range(len(CORxPositions))):
    #         fXseries[returns[0]] = returns[1]
    #         psiXseries[returns[0]] = returns[2]
    #         finishedPos += 1
    #         pbar.update(finishedPos)

    #     pool.close()
    #     pool.join()x
    # pbar.finish()
    pbar.close()

    return fXseries, psiXseries


def tomopackDivergentScanTo3DPositions(
    radioMM,
    radiusMM,
    CORxRef=None,
    CORxMin=None,
    CORxMax=None,
    CORxNumber=100,
    fXseries=None,
    psiXseries=None,
    pixelSizeMM=0.1,
    sourceDetectorDistMM=100,
    blur=0.0,
    maxIterations=50,
    l=0.5,
    kTrustMethod="iterative",
    kTrustRatio=0.75,
    SNRCutoff=2,
    epsilon=1,
    scanFixedNumber=None,
    massThreshold=0.5,
    projector="numba",
    scattering=0.0,
    saveSeries=True,
    saveSeriesDirectory=None,
    nProcesses=nProcessesDefault,
    verbose=True,
):
    """
    This function takes in a single divergent projection, and will run tomopack
    generating different psis by varying their position as Centre Of Rotation (COR) in the x-direction,
    from CORxMin to CORxMax in CORxNumber steps.

    The resulting series of indicator functions is analysed and a 3D position guess for
    all identified spheres is returned.

    Parameters
    ----------
        radioMM : 2D numpy array of floats
            Radiography containing "distance" projections in mm
            This is typically the result of mu*log(I/I_0)

        radiusMM : float
            Particle radius in mm

        fXseries: 3D numpy array of floats, optional
            Indicator function series along the x-ray direction
            Default = None

        psiXseries: 3D numpy array of floats, optional
            Structuring element series along the x-ray direction
            Default = None

        pixelSizeMM : float, optional
            Pixel size on detector in mm
            Default = 0.1

        sourceDetectorDistMM : float, optional
            Distance between x-ray source and middle of detector
            Default = 100

        blur : float, optional
            Sigma of blur to pass to `scipy.ndimage.gaussian_filter` to
            blur the synthetic psi
            Default = 0

        maxIterations : int, optional
            Number of iterations to run tomopack
            Default = 50

        l : float, optional
            "Lambda" parameter which controls relaxation in tomopack iterations
            Default = 0.5
        
        kTrustMethod : str, optional
            'scalar', 'iterative' or 'SNR'
            Default = 'iterative'

        epsilon : float, optional, or 'iterative'
            Trust cutoff wavelengths in psi for tomopack
            If the radiograph is in mm so is this parameter

        kTrustRatio : float, optional
            Ratio of cutoff psi wavelengths for tomopack. Used if `epsilon` is `iterative` only.
            Default = 0.75
        
        SNRCutoff : float, optional
            Signal-to-noise ratoiop that determines kTrust if `epsilon` is `SNR` only.
            Default = 2
        
        scanFixedNumber : int, optional
            The number of spheres scanned
            If None peaks will be thresholded based on `massThreshold` (below)
            Default = None

        massThreshold : float, optional
            Threshold for accepting the result of the filtered indicator function
            Activated if `scanFixedNumber` (above) is None
            Default = 0.5

        saveSeries : boolean, optional
            Save indicator function, psi and filtered series as tif files
            Default = True

        saveSeriesDirectory : str, optional
            Directory to save the computed series
            Default = None

        nProcesses : integer, optional
            Number of processes for multiprocessing
            Default = number of CPUs in the system

        verbose : boolean, optional
            Print what the function is doing?
            Default = True

    Returns
    -------
        positionsXYZmm : 2D numpy array
            Positions of spheres centres in 3D (in mm)
    """
    assert (
        len(radioMM.shape) == 2
    ), "\ndetectSpheres.tomopackDivergentScanTo3DPositions(): Projection should be 2D array"
    assert (
        CORxMin or CORxRef
    ), "\ndetectSpheres.tomopackDivergentScanTo3DPositions(): Need either position limits along the ray beam or the reference COR"

    #############################################################################
    # Create positions array along ray beam to run series of tomopack
    #############################################################################
    if not CORxMin:
        CORxMin = CORxRef - 3 * radiusMM
    if not CORxMax:
        CORxMax = CORxRef + 3 * radiusMM

    # CORxPositions = numpy.linspace(CORxMin, CORxMax, CORxNumber)
    CORxPositions = numpy.geomspace(CORxMin, CORxMax, CORxNumber)
    meanDeltaCORx = numpy.mean(numpy.diff(CORxPositions))

    if saveSeries:
        try:
            if saveSeriesDirectory:
                if verbose:
                    print(f"\nOutput directory: \n\t{saveSeriesDirectory}")
                os.makedirs(saveSeriesDirectory)
            else:
                if verbose:
                    print(f"\nOutput directory: \n\t{os.getcwd()}")
                saveSeriesDirectory = os.getcwd()
        except OSError:
            if not os.path.isdir(saveSeriesDirectory):
                raise

    #############################################################################
    # Load or compute fx and psi series
    #############################################################################
    loadedSeries = False
    if fXseries and psiXseries:
        if os.path.isfile(fXseries) and os.path.isfile(psiXseries):
            if verbose:
                print("\nLoading previous indicator functions and psi series... ", end="")
            fXseries = tifffile.imread(fXseries)
            psiXseries = tifffile.imread(psiXseries)
            if (fXseries.shape == psiXseries.shape) and (fXseries.shape[1:] == radioMM.shape):
                if fXseries.shape[0] == len(CORxPositions):
                    if verbose:
                        print("done.")
                    loadedSeries = True
            else:
                if verbose:
                    print("\nInput series had wrong dimensions. They will be recomputed")

    if not loadedSeries:
        if verbose:
            print(
                f"\nNo input fx and psi series found. Computing them now using {nProcesses} cores"
            )
        fXseries, psiXseries = computeFxAndPsiSeries(
            radioMM,
            radiusMM,
            CORxPositions,
            pixelSizeMM=pixelSizeMM,
            projector=projector,
            scattering=scattering,
            sourceDetectorDistMM=sourceDetectorDistMM,
            blur=blur,
            maxIterations=maxIterations,
            l=l,
            kTrustMethod=kTrustMethod,
            epsilon=epsilon,
            kTrustRatio=kTrustRatio,
            SNRCutoff=SNRCutoff,
            nProcesses=nProcesses,
        )

        if saveSeries:
            tifffile.imwrite(saveSeriesDirectory + "/fXseries.tif", fXseries.astype("<f4"))
            tifffile.imwrite(saveSeriesDirectory + "/psiXseries.tif", psiXseries.astype("<f4"))

    #############################################################################
    # Clean resonance peaks of fx series
    # by a convolution with a SE extracted from the psi series
    #############################################################################
    # if verbose: print("\nConvolving fx with psi series...", end="")
    ##Lx  = 20 # TODO: SCALING IN X DIRECTION SHOULD BE A FUNCTION OF THE CONE ANGLE
    ##Lyz =  2 # TODO: THIS SHOULD BE A FUNCTION OF THE PIXELS PER RADIUS
    zoomLevel = sourceDetectorDistMM / ((CORxMin + CORxMax) / 2)
    Lx = int(numpy.ceil(5.0 * radiusMM / meanDeltaCORx))
    Lyz = int(numpy.floor(0.1 * radiusMM / pixelSizeMM * zoomLevel))

    X_middle_loc = numpy.argmin(numpy.abs(CORxPositions - (CORxMax + CORxMin)/2.)) # geometric progression doesn't have mean value at the middle

    # BM 2022-08-10: Now works for both even and odd image sizes!
    struct = psiXseries[
        X_middle_loc - Lx : X_middle_loc + Lx + 1,
        # (psiXseries.shape[0]) // 2 - Lx : (psiXseries.shape[0]) // 2 + Lx + 1,
        (psiXseries.shape[1]) // 2 - Lyz + ((psiXseries.shape[1]) % 2): (psiXseries.shape[1]) // 2 + Lyz + 1 + ((psiXseries.shape[1]) % 2),
        (psiXseries.shape[2]) // 2 - Lyz + ((psiXseries.shape[2]) % 2): (psiXseries.shape[2]) // 2 + Lyz + 1 + ((psiXseries.shape[2]) % 2),
    ]

    ## OS 2021-11-19: Let's do a fourier convolution which should be way faster
    ##fXconvolvedSeries = scipy.ndimage.convolve(fXseries,struct/struct.sum())
    fXconvolvedSeries = scipy.signal.convolve(fXseries, struct / struct.sum(), mode="same")
    if verbose:
        print(" done.")

    if saveSeries:
        tifffile.imwrite(saveSeriesDirectory + "/psiXseries-convolutionSE.tif", struct.astype("<f4"))
        tifffile.imwrite(
            saveSeriesDirectory + "/fXconvolvedSeries.tif", fXconvolvedSeries.astype("<f4")
        )

    # fXconvolvedSeries = fXseries.copy()
    ##############################################################################
    # Filter maxima of cleaned fx series
    ##############################################################################
    if verbose:
        print("\nFiltering maxima...", end="")
    # Look in a volume of +/- half a radius in all directions for the highest value
    # (+/- 1 radius keeps overlapping and causing issues, half a radius doesn't overlap particles, but still contains one clean peak)
    fXconvolvedMaximumFiltered = scipy.ndimage.maximum_filter(
        fXconvolvedSeries,
        size=(
            int(numpy.ceil(1.5 * radiusMM / meanDeltaCORx)),
            int(numpy.floor(radiusMM / pixelSizeMM * zoomLevel)),
            int(numpy.floor(radiusMM / pixelSizeMM * zoomLevel)),
        ),
    )

    allPeaks = fXconvolvedSeries == fXconvolvedMaximumFiltered
    masses = allPeaks * fXconvolvedSeries
    if verbose:
        print(" done.")

    if saveSeries:
        tifffile.imwrite(saveSeriesDirectory + "/masses.tif", masses.astype("<f4"))
        tifffile.imwrite(saveSeriesDirectory + "/peaks.tif", allPeaks.astype("<f4"))
        tifffile.imwrite(
            saveSeriesDirectory + "/fXconvolvedSeriesMaxFiltered.tif",
            fXconvolvedMaximumFiltered.astype("<f4"),
        )

    ##############################################################################
    # Find filtered peaks on the detector
    ##############################################################################
    if verbose:
        print("\nConverting filtered peaks to detector positions...", end="")
    peaksCORxPOSnJI = radioSphere.detectSpheres.indicatorFunctionToDetectorPositions(
        masses, scanFixedNumber=scanFixedNumber, massThreshold=massThreshold
    )
    if verbose:
        print(" done.")

    ##############################################################################
    # Converting peaksJI to XYZmm
    ##############################################################################
    if verbose:
        print("\nConverting detector peaks to 3D positions...", end="")
    positionsXYZmm = radioSphere.detectSpheres.detectorPeaksTo3DCoordinates(
        peaksCORxPOSnJI,
        CORxPositions,
        detectorResolution=radioMM.shape,
        pixelSizeMM=pixelSizeMM,
        sourceDetectorDistMM=sourceDetectorDistMM,
    )
    if verbose:
        print(" done.")

    print(
        f"\ntomopackDivergentScanTo3DPositions(): Returning {positionsXYZmm.shape[0]} 3D positions.\n"
    )
    return positionsXYZmm


def removeParticle(
    positionsXYZmm,
    residual,
    radioMM,
    radiiMM,
    pixelSizeDetectorMM,
    zoomLevel,
    sourceObjectDistMM,
    projector,
    scattering,
    verbose,
    GRAPH,
):
    if verbose:
        print("Removing a particle")
    # find the location of the highest peak on the detector panel. This is presumably the centroid.
    residualMMPeakIndices = numpy.unravel_index(numpy.argmax(residual, axis=None), residual.shape)
    if verbose:
        print(f"residualMMPeakIndices: {residualMMPeakIndices}")

    # define unit vector between source and peak location
    yPosDetMM = -1 * (residualMMPeakIndices[1] - radioMM.shape[1] / 2.0) * pixelSizeDetectorMM
    zPosDetMM = -1 * (residualMMPeakIndices[0] - radioMM.shape[0] / 2.0) * pixelSizeDetectorMM
    magnitude = numpy.sqrt(
        zoomLevel**2 * sourceObjectDistMM**2 + yPosDetMM**2 + zPosDetMM**2
    )
    s = numpy.array(
        [zoomLevel * sourceObjectDistMM / magnitude, yPosDetMM / magnitude, zPosDetMM / magnitude]
    )
    if verbose:
        print(f"s: {s}")

    # find distance of every particle from the line defined by this unit vector
    distances = numpy.linalg.norm(numpy.cross(positionsXYZmm, s), axis=1)
    if verbose:
        print(f"distances: {distances}")

    # remove the particle closest to the line
    closestParticleIndex = numpy.argmin(distances)
    positionsXYZmm = numpy.delete(positionsXYZmm, closestParticleIndex, axis=0)

    p_f_x = radioSphere.projectSphere.projectSphereMM(
        positionsXYZmm,
        radiiMM[0] * numpy.ones(len(positionsXYZmm)),
        sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
        pixelSizeMM=pixelSizeDetectorMM,
        detectorResolution=radioMM.shape,
        projector=projector,
        scattering=scattering
    )
    residual = p_f_x - radioMM

    if GRAPH:
        plt.imshow(residual)
        plt.show()

    return positionsXYZmm, residual


def addParticle(*args, **kwargs):
    # return addParticleRaster(*args, **kwargs)
    return addParticleSensitivity(*args, **kwargs)


def addParticleRaster(
    positionsXYZmm,
    residual,
    radioMM,
    radiiMM,
    pixelSizeDetectorMM,
    zoomLevel,
    sourceObjectDistMM,
    CORxMin,
    CORxMax,
    CORxNumber,
    projector,
    scattering,
    verbose,
    GRAPH,
):
    if verbose:
        print("Adding a particle")
    # find the location of the highest peak on the detector panel. This is presumably the centroid.
    residualMMPeakIndices = numpy.unravel_index(numpy.argmin(residual, axis=None), residual.shape)
    if verbose:
        print(f"residualMMPeakIndices: {residualMMPeakIndices}")

    # define unit vector between source and peak location
    yPosDetMM = -1 * (residualMMPeakIndices[1] - radioMM.shape[1] / 2.0) * pixelSizeDetectorMM
    zPosDetMM = -1 * (residualMMPeakIndices[0] - radioMM.shape[0] / 2.0) * pixelSizeDetectorMM
    magnitude = numpy.sqrt(
        zoomLevel**2 * sourceObjectDistMM**2 + yPosDetMM**2 + zPosDetMM**2
    )
    s = numpy.array(
        [zoomLevel * sourceObjectDistMM / magnitude, yPosDetMM / magnitude, zPosDetMM / magnitude]
    )
    if verbose:
        print(f"s: {s}")

    # trying to find an optimal solution by doing a raster scan and looking for minimal residual
    x_test = numpy.linspace(CORxMin, CORxMax, CORxNumber)
    best_index = 0
    best_residual = numpy.inf
    ref_projection = radioSphere.projectSphere.projectSphereMM(
        positionsXYZmm,
        radiiMM[0] * numpy.ones(len(positionsXYZmm)),
        sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
        pixelSizeMM=pixelSizeDetectorMM,
        detectorResolution=radioMM.shape,
        projector=projector,
        scattering=scattering
    )

    limits = radioSphere.projectSphere.singleSphereToDetectorPixelRange(
        s * x_test[0],
        radiiMM[0],
        radiusMargin=0.1,
        sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
        pixelSizeMM=pixelSizeDetectorMM,
        detectorResolution=radioMM.shape,
    )

    ref_projection_crop = ref_projection[limits[0, 0] : limits[0, 1], limits[1, 0] : limits[1, 1]]
    radioMM_crop = radioMM[limits[0, 0] : limits[0, 1], limits[1, 0] : limits[1, 1]]
    for i, x in enumerate(x_test):
        single_particle_projection = radioSphere.projectSphere.projectSphereMM(
            numpy.expand_dims(s * x, axis=0),
            numpy.expand_dims(radiiMM[0], axis=0),
            sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
            pixelSizeMM=pixelSizeDetectorMM,
            detectorResolution=radioMM.shape,
            ROIcentreMM=s * x_test[0],
            ROIradiusMM=radiiMM[0],
            projector=projector,
            scattering=scattering
        )

        residual = ref_projection_crop + single_particle_projection - radioMM_crop
        # print(i, (residual**2).sum(), best_residual, best_index)

        if (residual**2).sum() < best_residual:
            best_index = i
            best_residual = (residual**2).sum()

        # plt.ion()
        # plt.title(i)
        # plt.imshow(residual)
        # plt.pause(0.001)
    bestPositionXYZmm = s * x_test[best_index]

    print(f"Best location at {best_index}-th x value: {x_test[best_index]}")

    optimise = True
    if optimise:
        import radiosphere.optimsePositions

        bestPositionXYZmm = radioSphere.optimisePositions.optimiseSensitivityFields(
            radioMM,
            numpy.expand_dims(bestPositionXYZmm, axis=0),  # try the middle of the sample
            numpy.expand_dims(radiiMM[0], axis=0),
            perturbationMM=(0.01, 0.01, 0.01),
            # perturbationMM=(0.5, 0.25, 0.25),
            # perturbationMM=(1, 0.5, 0.5),
            # perturbationMM=(3, 1, 1),
            minDeltaMM=0.0001,
            iterationsMax=500,
            sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
            pixelSizeMM=pixelSizeDetectorMM,
            detectorResolution=radioMM.shape,
            verbose=False,
            # GRAPH=True,
            # NDDEM_output=True
        )

    positionsXYZmm = numpy.vstack([positionsXYZmm, bestPositionXYZmm])
    p_f_x = radioSphere.projectSphere.projectSphereMM(
        positionsXYZmm,
        radiiMM[0] * numpy.ones(len(positionsXYZmm)),
        sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
        pixelSizeMM=pixelSizeDetectorMM,
        detectorResolution=radioMM.shape,
        projector=projector,
        scattering=scattering
    )
    residual = p_f_x - radioMM

    if GRAPH:
        plt.imshow(residual)
        plt.show()

    return positionsXYZmm, residual


def addParticleSensitivity(
    positionsXYZmm,
    residual,
    radioMM,
    radiiMM,
    pixelSizeDetectorMM,
    zoomLevel,
    sourceObjectDistMM,
    CORxMin,
    CORxMax,
    CORxNumber,
    projector,
    scattering,
    verbose,
    GRAPH,
):
    if verbose:
        print("Adding a particle")
    # find the location of the highest peak on the detector panel. This is presumably the centroid.
    residualMMPeakIndices = numpy.unravel_index(numpy.argmin(residual, axis=None), residual.shape)
    if verbose:
        print(f"residualMMPeakIndices: {residualMMPeakIndices}")

    # define unit vector between source and peak location
    yPosDetMM = -1 * (residualMMPeakIndices[1] - radioMM.shape[1] / 2.0) * pixelSizeDetectorMM
    zPosDetMM = -1 * (residualMMPeakIndices[0] - radioMM.shape[0] / 2.0) * pixelSizeDetectorMM
    magnitude = numpy.sqrt(
        zoomLevel**2 * sourceObjectDistMM**2 + yPosDetMM**2 + zPosDetMM**2
    )
    s = numpy.array(
        [zoomLevel * sourceObjectDistMM / magnitude, yPosDetMM / magnitude, zPosDetMM / magnitude]
    )
    if verbose:
        print(f"s: {s}")

    # trying to find an optimal solution by doing a raster scan and looking for minimal residual
    positionXYZmmOpt = radioSphere.optimisePositions.optimiseSensitivityFields(
        radioMM,
        numpy.expand_dims(s * sourceObjectDistMM, axis=0),  # try the middle of the sample
        numpy.expand_dims(radiiMM[0], axis=0),
        perturbationMM=(0.001, 0.001, 0.001),
        minDeltaMM=0.0001,
        iterationsMax=500,
        sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
        pixelSizeMM=pixelSizeDetectorMM,
        detectorResolution=radioMM.shape,
        verbose=False,
        NDDEM_output=True,
    )

    positionsXYZmm = numpy.vstack([positionsXYZmm, positionXYZmmOpt])
    p_f_x = radioSphere.projectSphere.projectSphereMM(
        positionsXYZmm,
        radiiMM[0] * numpy.ones(len(positionsXYZmm)),
        sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
        pixelSizeMM=pixelSizeDetectorMM,
        detectorResolution=radioMM.shape,
        projector=projector,
        scattering=scattering
    )
    residual = p_f_x - radioMM

    if GRAPH:
        plt.imshow(residual)
        plt.show()

    return positionsXYZmm, residual


def cleanDivergentScan(
    positionsXYZmm,
    radioMM,
    radiiMM,
    zoomLevel,
    sourceObjectDistMM,
    pixelSizeDetectorMM,
    CORxMin,
    CORxMax,
    CORxNumber,
    projector="numba",
    scattering=0.0,
    verbose=False,
    GRAPH=False,
):
    p_f_x = radioSphere.projectSphere.projectSphereMM(
        positionsXYZmm,
        radiiMM[0] * numpy.ones(len(positionsXYZmm)),
        sourceDetectorDistMM=zoomLevel * sourceObjectDistMM,
        pixelSizeMM=pixelSizeDetectorMM,
        detectorResolution=radioMM.shape,
        projector=projector,
        scattering=scattering
    )

    residual = p_f_x - radioMM
    print(f"Maximum |residual| {numpy.abs(residual).max()}")
    # Found an extra particle that shouldn't be there
    removed = 0
    added = 0
    # remove any overlaps
    while residual.max() > 0.9:
        positionsXYZmm, residual = removeParticle(
            positionsXYZmm,
            residual,
            radioMM,
            radiiMM,
            pixelSizeDetectorMM,
            zoomLevel,
            sourceObjectDistMM,
            projector=projector,
            scattering=scattering,
            verbose=verbose,
            GRAPH=GRAPH,
        )
        removed += 1
    while residual.min() < -0.9:
        positionsXYZmm, residual = addParticle(
            positionsXYZmm,
            residual,
            radioMM,
            radiiMM,
            pixelSizeDetectorMM,
            zoomLevel,
            sourceObjectDistMM,
            CORxMin,
            CORxMax,
            CORxNumber,
            projector=projector,
            scattering=scattering,
            verbose=verbose,
            GRAPH=GRAPH,
        )
        added += 1
    # now we clean up the cleaning up to make sure we have the right number of particles
    while added > removed:
        positionsXYZmm, residual = removeParticle(
            positionsXYZmm,
            residual,
            radioMM,
            radiiMM,
            pixelSizeDetectorMM,
            zoomLevel,
            sourceObjectDistMM,
            projector=projector,
            scattering=scattering,
            verbose=verbose,
            GRAPH=GRAPH,
        )
        removed += 1
    while removed > added:
        positionsXYZmm, residual = addParticle(
            positionsXYZmm,
            residual,
            radioMM,
            radiiMM,
            pixelSizeDetectorMM,
            zoomLevel,
            sourceObjectDistMM,
            CORxMin,
            CORxMax,
            CORxNumber,
            projector=projector,
            scattering=scattering,
            verbose=verbose,
            GRAPH=GRAPH,
        )
        added += 1

    print(f"Removed {removed} particles and added {added}.")
    return positionsXYZmm


def calculateErrors(posXYZa, posXYZb, radiiMM, verbose=True):
    distances = distance.cdist(posXYZa, posXYZb)
    distance_threshold = radiiMM[0]

    # an empty column in the distance matrix is a lost particle
    number_lost = numpy.sum((numpy.sum(distances <= distance_threshold, axis=0) == 0))
    if number_lost > 0:
        print(f"detectSpheres.calculateErrors(): number_lost = {number_lost}")

    # get errors
    min_errors = numpy.min(distances, axis=0)  # best match for each column
    min_valid_errors = min_errors[min_errors < distance_threshold]  # just where we found a particle

    err_mean = numpy.mean(min_valid_errors)
    err_std = numpy.std(min_valid_errors)

    return err_mean, err_std, number_lost


def psiSeriesScanTo3DPositions(
    radio,  # not (necessarily) MM
    psiXseries,  # Obviously in the same units as radio above, please
    radiusMM,  # can be removed?
    CORxPositions=None,
    massThreshold=0.12,
    scanPersistenceThresholdRadii=None,
    scanFixedNumber=None,
    scanPersistenceThreshold=7,
    maxIterations=50,
    sourceDetectorDistMM=100,
    pixelSizeMM=0.1,
    l=0.2,
    kTrustRatio=0.7,
    useCache=True,
    numCores=1,
    blur=0.0,
    cacheFile="fXseries.tif",
    verbose=False,
):

    # it is our objective to fill in fx series
    fXseries = numpy.zeros_like(psiXseries)

    if CORxPositions is None:
        print("xPositions is not passed, just putting 1, 2, 3...")
        CORxPositions = numpy.arange(psiXseries.shape[0])

    for posN, CORxPos in enumerate(CORxPositions):
        ### "Structuring Element"
        print(
            "\t{}/{} CORxPos = {:0.2f} mm".format(posN + 1, len(CORxPositions), CORxPos), end="\r"
        )
        fXseries[posN] = radioSphere.detectSpheres.tomopack(
            radio,
            psiXseries[posN],
            GRAPH=0,
            maxIterations=maxIterations,
            l=l,
            kTrustRatio=kTrustRatio,
        )
    tifffile.imwrite(cacheFile, fXseries.astype("float"))
    print(f"saved {cacheFile}")
    # loadedCache = False

    # if useCache:
    # cachePsiFile = cacheFile[:-4] + '_psi.tif'
    # if os.path.isfile(cacheFile) and os.path.isfile(cachePsiFile):
    # print("Loading previous indicator functions... ", end="")
    # fXseries = tifffile.imread(cacheFile)
    # psiXseries = tifffile.imread(cachePsiFile)
    # if ( fXseries.shape[0] == CORxNumber ) and ( fXseries.shape[1] == radioMM.shape[0] ) and ( fXseries.shape[2] == radioMM.shape[1] ):
    # print("done.")
    # loadedCache = True
    # else:
    # print("cached file had wrong dimensions. Generating new cache file.")
    # else:
    # print('No cached indicator functions found. Generating them now to cache.')
    # if not loadedCache:
    # fXseries = numpy.zeros((len(CORxPositions), radioMM.shape[0], radioMM.shape[1]))
    # psiXseries = numpy.zeros_like(fXseries)

    # psiRefMM = radioSphere.projectSphere.projectSphereMM(numpy.array([[(CORxMax+CORxMin)/2., 0., 0.]]),
    # numpy.array([radiusMM]),
    # detectorResolution=radioMM.shape,
    # pixelSizeMM=pixelSizeMM,
    # sourceDetectorDistMM=sourceDetectorDistMM,
    # blur=blur)

    # for posN, CORxPos in enumerate(CORxPositions):
    #### "Structuring Element"
    # print("\t{}/{} CORxPos = {:0.2f}mm".format(posN+1, len(CORxPositions), CORxPos), end='\r')
    # psiMM = radioSphere.projectSphere.projectSphereMM(numpy.array([[CORxPos, 0., 0.]]),
    # numpy.array([radiusMM]),
    # detectorResolution=radioMM.shape,
    # pixelSizeMM=pixelSizeMM,
    # sourceDetectorDistMM=sourceDetectorDistMM,
    # blur=blur)

    # fXseries[posN] = radioSphere.detectSpheres.tomopack(radioMM, psiMM, GRAPH=0, maxIterations=maxIterations, l=l, kTrustRatio=kTrustRatio)
    # psiXseries[posN] = radioSphere.detectSpheres.tomopack(psiRefMM, psiMM, GRAPH=0, maxIterations=maxIterations, l=l, kTrustRatio=kTrustRatio)

    # if useCache and not loadedCache:
    # print("Saving indicator functions for next time... ", end="")
    # tifffile.imwrite(cacheFile, fXseries.astype('<f4'))
    # tifffile.imwrite(cachePsiFile, psiXseries.astype('<f4'))
    # print("done.")

    # L_x  = 20 # TODO: SCALING IN X DIRECTION SHOULD BE A FUNCTION OF THE CONE ANGLE
    # L_yz =  2 # TODO: THIS SHOULD BE A FUNCTION OF THE PIXELS PER RADIUS

    # struct = psiXseries[(psiXseries.shape[0])//2 -  L_x:(psiXseries.shape[0])//2 + L_x  + 1,
    # (psiXseries.shape[1])//2 - L_yz:(psiXseries.shape[1])//2 + L_yz + 1,
    # (psiXseries.shape[2])//2 - L_yz:(psiXseries.shape[2])//2 + L_yz + 1]

    # fXconvolvedSeries = scipy.ndimage.convolve(fXseries,struct/struct.sum())
    ##if useCache and not loadedCache:
    ##tifffile.imwrite(f'{cacheFile[:-4]}_struct.tif', struct.astype('<f4'))
    ##tifffile.imwrite(f'{cacheFile[:-4]}_fXconvolvedSeries.tif', fXconvolvedSeries.astype('<f4'))

    # binaryPeaks = fXconvolvedSeries > massThreshold

    zoomLevel = sourceDetectorDistMM / ((CORxPositions[0] + CORxPositions[-1]) / 2)
    CORxDelta = numpy.abs(CORxPositions[0] - CORxPositions[1])
    # Look in a volume of +/- half a radius in all directions for the highest value (+/- 1 radius keeps overlapping and causing issues, half a radius doesn't overlap particles, but still contains one clean peak)
    fXseriesMaximumFiltered = scipy.ndimage.maximum_filter(
        fXseries,
        size=(
            3 * int(numpy.floor(radiusMM / CORxDelta)),
            int(numpy.floor(radiusMM / pixelSizeMM * zoomLevel)),
            int(numpy.floor(radiusMM / pixelSizeMM * zoomLevel)),
        ),
    )
    allPeaks = fXseries == fXseriesMaximumFiltered
    masses = allPeaks * fXseries

    if verbose:
        tifffile.imwrite(cacheFile[:-4] + "_masses.tif", masses.astype("<f4"))
        tifffile.imwrite(cacheFile[:-4] + "_peaks.tif", allPeaks.astype("<f4"))
        tifffile.imwrite(cacheFile[:-4] + "_fXseries.tif", fXseries.astype("<f4"))
        tifffile.imwrite(
            cacheFile[:-4] + "_fXseriesMaximumFiltered.tif", fXseriesMaximumFiltered.astype("<f4")
        )

    if scanFixedNumber:
        # get the indices of all of the peaks, from highest to lowest
        sortedPeakIndices = numpy.argsort(masses, axis=None)[::-1]
        # print(sortedPeakIndices.shape)
        # get just the first scanFixedNumber of those and put them into a scanFixedNumber x 3 array
        peaksCORxPOSnJI = numpy.vstack(
            numpy.unravel_index(sortedPeakIndices[:scanFixedNumber], masses.shape)
        ).T
        # print(peaksCORxPOSnJI.shape)
    else:
        filteredPeaks = masses > massThreshold
        peaksCORxPOSnJI = numpy.argwhere(filteredPeaks)

        if verbose:
            tifffile.imwrite(cacheFile[:-4] + "_filteredPeaks.tif", filteredPeaks.astype("<f4"))
    # print(peaksCORxPOSnJI)

    ###############################################################
    ### Now we have guesses for all particle according to detector
    ###   (IJ) and position along the X-scanning direction
    ### We're going to convert that to spatial XYZ
    ###############################################################
    print("\nConverting tomopack x-scan to 3D positions\n")
    ## Convert to XYZ in space and mm
    positionsXYZmm = numpy.zeros([peaksCORxPOSnJI.shape[0], 3])

    for i in range(positionsXYZmm.shape[0]):
        # X -- look up which CORx slice the maximum falls in, this could be interpolated instead of rounded
        positionsXYZmm[i, 0] = CORxPositions[int(numpy.round(peaksCORxPOSnJI[i, 0]))]

        # detector I gives real position Y in mm
        yPosDetMM = -1 * (peaksCORxPOSnJI[i, 2] - radio.shape[1] / 2.0) * pixelSizeMM

        # detector J gives real position Z in mm
        zPosDetMM = -1 * (peaksCORxPOSnJI[i, 1] - radio.shape[0] / 2.0) * pixelSizeMM

        # And now scale down by zoom factor
        # Y
        positionsXYZmm[i, 1] = yPosDetMM * (positionsXYZmm[i, 0] / sourceDetectorDistMM)
        # Z
        positionsXYZmm[i, 2] = zPosDetMM * (positionsXYZmm[i, 0] / sourceDetectorDistMM)

    print(
        f"\ntomopackDivergentScanTo3DPositions(): I'm returning {positionsXYZmm.shape[0]} 3D positions.\n"
    )
    return positionsXYZmm
