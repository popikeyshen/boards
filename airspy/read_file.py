# airspyhf_rx -f 101.5  -r raw.iq

import numpy as np
import matplotlib.pyplot as plt

# Завантажуємо int16-потік
data = np.fromfile("raw.iq", dtype=np.int16)
iq = data[::2] + 1j * data[1::2]

# Розбиваємо на блоки
block_size = 2048
num_blocks = len(iq) // block_size
iq = iq[:num_blocks * block_size].reshape((num_blocks, block_size))

# FFT по кожному блоку
spectra = np.fft.fftshift(np.fft.fft(iq, axis=1), axes=1)
power = 20 * np.log10(np.abs(spectra) + 1e-12)

# Усереднення (накопичення)
avg_power = np.mean(power, axis=0)

# Відображення
plt.figure(figsize=(10, 4))
plt.plot(avg_power)
plt.title("Averaged FFT (Accumulated Power Spectrum)")
plt.xlabel("Frequency bin")
plt.ylabel("Power [dB]")
plt.grid()
plt.show()
