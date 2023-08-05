# <b>whoi_uwapm</b>

## <b> Introduction </b>
whoi_uwapm is a fork of arlpy's uwapm module. It removes all of the graphing features of the original uwapm, and also is updated to support the latest versions of numpy, scipy, and pandas.

## PyPI
The PyPI package contains an x86_64 binary of bellhopcuda. If you are using a different architecture, you will need to build bellhopcuda manually.

## Automated building of bellhopcuda and fortran bellhop
The build.bash script included in this repo can be used to build bellhopcuda
- Clone whoi_uwapm and navigate to it
- `./build.bash`

## Manually building bellhopcuda
- Clone whoi_uwapm
- Clone bellhopcuda
    - `git clone https://github.com/A-New-BellHope/bellhopcuda.git`
- Initialize submodules
    - `git submodule update --init --recursive`
# If using CUDA
- Install cuda toolkit:
	- https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=runfile_local
- Run cmake inside the bellhopcuda directory
	- `cmake .`
# If not using cuda
- set cmake flag for sure to off, run cmake inside the bellhopcuda directory
	- `cmake . -D BHC_ENABLE_CUDA=OFF`
# Build
- Run make inside the bellhopcuda directory
	- `make bellhopcxx`

# Install
- Move the bellhopcxx binary to the whoi_uwapm directory
    - `mv bin/bellhopcxx ../whoi_uwapm/bellhopcxx`
        - This will need to be adjusted based on where you cloned whoi_uwapm
        - If you cloned bellhopcuda inside of the whoi_uwapm directory, make sure to move it or delete it before running pip install.
    - `pip install .`

## Manually building fortran bellhop
- Clone whoi_uwapm
- Clone accoustic_toolbox
    - `git clone https://git.whoi.edu/dgiaya/acoustic_toolbox.git`
- Install gfortran
    - `sudo apt-get install gfortran -y`
- Run make inside the acoustic_toolbox directory
	- `make`

# Install
- Move the bellhopcxx binary to the whoi_uwapm directory
    - `mv Bellhop/bellhop.exe ../whoi_uwapm/bellhop`
        - This will need to be adjusted based on where you cloned whoi_uwapm
        - If you cloned accoustic_toolbox inside of the whoi_uwapm directory, make sure to move it or delete it before running pip install.
    - `pip install .`