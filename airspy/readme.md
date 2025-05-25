sudo apt install libairspyhf-dev airspyhf
airspyhf_info

airspyhf_rx -f 3  -r raw.iq
python3 read_file.py

git clone https://github.com/pothosware/SoapySDR
cd SoapySDR/
ls
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
SoapySDRUtil --info


sudo apt install libairspyhf-dev
git clone  https://github.com/pothosware/SoapyAirspyHF
mkdir build && cd build
cmake ..
make
sudo make install
sudo ldconfig


SoapySDRUtil --info
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################

Lib Version: v0.8.1-g640ac414
API Version: v0.8.200
ABI Version: v0.8-3
Install root: /usr/local
Search path:  /usr/local/lib/SoapySDR/modules0.8-3
Module found: /usr/local/lib/SoapySDR/modules0.8-3/libairspyhfSupport.so (0.2.0-a2fd6cf)
Available factories... airspyhf
Available converters...
 -  CF32 -> [CF32, CS16, CS8, CU16, CU8]
 -  CS16 -> [CF32, CS16, CS8, CU16, CU8]
 -  CS32 -> [CS32]



SoapySDRUtil --find
######################################################
##     Soapy SDR -- the SDR abstraction library     ##
######################################################

Found device 0
  driver = airspyhf
  label = AirSpy HF+ [dc52e85dcdcd35ba]
  serial = dc52e85dcdcd35ba

