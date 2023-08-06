import numpy
import radioSphere
from tqdm import tqdm
import matplotlib.pyplot as plt
import time

#N = 100
#n = 50
#res = [500,500]

N = 1
nParticles = 1000
res = [1000,1000]



ps = 100/res[0]

#projectors = ["numba", "C",  "cupy", "youssef"]
projectors = ["cupy", "numba"]
#projectors = ["numba"]


for pn, proj in enumerate(projectors):
    print(f"Trying {proj} projector")
    for i in tqdm(range(N+1)):
        # skip first one to allow numba to jit compile
        if i == 1: t1 = time.perf_counter()
        p = radioSphere.projectSphere.projectSphereMM(
            numpy.random.randint(-20, 20, size=(nParticles, 3))+numpy.array([50,0,0]),
            numpy.ones(nParticles)*3,
            detectorResolution=res,
            pixelSizeMM = ps,
            projector=proj
        )
    t2 = time.perf_counter()
    print(f"{proj} mean time = {(t2-t1)/N}")
    plt.subplot(1, len(projectors), pn+1)
    plt.imshow(p)
    plt.title(f"random proj with {proj}")
plt.show()
