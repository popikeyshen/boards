import numpy as np
import scipy as sp

from scipy import signal

%matplotlib notebook
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

SAMPLE_RATE = 10e6

TIME_0 = 1.0 / 29.0
TIME_1 = 2.0 / 29.0

OFFSET_0 = int(SAMPLE_RATE * TIME_0)
OFFSET_1 = int(SAMPLE_RATE * (TIME_0 + TIME_1))

FILE_PATH = "/home/daulpavid/fm_ntsc_raw.bin"

sample_capture = sp.fromfile(FILE_PATH, dtype=np.complex64)
sample_capture = sample_capture[OFFSET_0:OFFSET_1]

from collections import deque

freq, power = signal.welch(sample_capture,
                           fs=SAMPLE_RATE,
                           window='hann',
                           nfft=2048,
                           return_onesided=False,
                           detrend=None)

plt.plot(freq / 1e6, 10 * np.log10(power))
plt.xlabel('Frequency [MHz]')
plt.ylabel('Power Spectral Density [dB]')
plt.grid(which='both', linestyle='--')
plt.title('FM Modulated NTSC - Periodogram')
plt.show()

