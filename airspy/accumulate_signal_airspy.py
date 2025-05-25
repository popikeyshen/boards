# not tested
import SoapySDR
from SoapySDR import *  # SOAPY_SDR_ constants
import time
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# --- Параметри ---
frequency = 433e6          # Центр
sample_rate = 2.5e6        # Частота дискретизації
num_samples = 4096         # Блок семплів
avg_blocks = 1000          # Скільки накопичувати
target_freq_offset = 100e3 # Частота сигналу відносно центру, яку витягуємо (100 кГц)

# --- Підключення до AirSpy ---
#results = SoapySDR.Device.enumerate("driver=airspy")
results = SoapySDR.Device.enumerate("driver=airspyhf")

if len(results) == 0:
    raise RuntimeError("AirSpy не знайдено")

sdr = SoapySDR.Device(results[0])

sdr.setSampleRate(SOAPY_SDR_RX, 0, sample_rate)
sdr.setFrequency(SOAPY_SDR_RX, 0, frequency)
sdr.setGain(SOAPY_SDR_RX, 0, 20)

# --- Створення потоку ---
rxStream = sdr.setupStream(SOAPY_SDR_RX, SOAPY_SDR_CF32)
sdr.activateStream(rxStream)

# --- Масив для накопичення ---
accumulated = np.zeros(num_samples, dtype=np.complex64)

# --- Зміщення сигналу в нульову частоту ---
def frequency_shift(signal, freq_offset, sample_rate):
    t = np.arange(len(signal)) / sample_rate
    return signal * np.exp(-1j * 2 * np.pi * freq_offset * t)

# --- Основний цикл накопичення ---
for i in range(avg_blocks):
    buff = np.empty(num_samples, dtype=np.complex64)
    sr = sdr.readStream(rxStream, [buff], len(buff))
    if sr.ret > 0:
        shifted = frequency_shift(buff, target_freq_offset, sample_rate)
        phase_aligned = hilbert(np.real(shifted))  # вирівнювання фази
        accumulated += phase_aligned
    else:
        print("Помилка зчитування блоку", i)

sdr.deactivateStream(rxStream)
sdr.closeStream(rxStream)

# --- Візуалізація ---
plt.figure()
plt.plot(np.abs(accumulated))
plt.title(f'Накопичений сигнал ({avg_blocks} блоків)')
plt.xlabel("Семпли")
plt.ylabel("Амплітуда")
plt.grid()
plt.show()
