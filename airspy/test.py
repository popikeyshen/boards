import SoapySDR
from SoapySDR import *
import numpy as np

results = SoapySDR.Device.enumerate("driver=airspyhf")
sdr = SoapySDR.Device(results[0])
sdr.setSampleRate(SOAPY_SDR_RX, 0, 768000)
sdr.setFrequency(SOAPY_SDR_RX, 0, 14.2e6)
sdr.setGain(SOAPY_SDR_RX, 0, 16)

rxStream = sdr.setupStream(SOAPY_SDR_RX, SOAPY_SDR_CF32)
sdr.activateStream(rxStream)

buff = np.array([0]*4096, np.complex64)
sr = sdr.readStream(rxStream, [buff], len(buff))
print("Прочитано:", sr.ret, "семплів")

sdr.deactivateStream(rxStream)
sdr.closeStream(rxStream)
