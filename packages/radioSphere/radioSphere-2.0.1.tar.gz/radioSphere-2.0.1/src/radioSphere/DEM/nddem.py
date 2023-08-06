import os, glob
import numpy

# _default_NDDEM_path = '~/Dropbox/Research/Codes/DEM_ND/Samples/radioSphere'
_default_NDDEM_path = "~/code/NDDEM/Samples/radioSphere"


def write_infile(xyzMM, radiiMM, nt, dumpfolder=_default_NDDEM_path):
    if not os.path.exists(os.path.expanduser(dumpfolder)):
        os.makedirs(os.path.expanduser(dumpfolder))
        
    files = glob.glob(f"{os.path.expanduser(dumpfolder)}/*")
    for f in files:
        os.remove(f)
    with open(f"{os.path.expanduser(dumpfolder)}/in", "w") as f:
        f.write(
            f"dimensions 3 {len(xyzMM)}\nradius -1 {radiiMM[0]}\nboundary 0 PBC  {xyzMM[:,0].min()} {xyzMM[:,0].max()}\nboundary 1 PBC  {xyzMM[:,1].min()} {xyzMM[:,1].max()}\nboundary 2 PBC  {xyzMM[:,2].min()} {xyzMM[:,2].max()}\nset T {nt}\nset dt 1\nset tdump 1\nEOF"
        )


def write_dumpfile(xyzMM, radiiMM, iteration, dumpfolder=_default_NDDEM_path):
    numpy.savetxt(
        f"{os.path.expanduser(dumpfolder)}/dump-{iteration:05d}.csv",
        numpy.hstack([xyzMM, numpy.expand_dims(radiiMM, 1)]),
        delimiter=",",
        header="x0,x1,x2,R",
        comments="",
    )
