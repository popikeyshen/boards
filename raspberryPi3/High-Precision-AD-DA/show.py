import numpy as np
from matplotlib import pyplot as plt


with open('signal.npy', 'rb') as f:
		data_vector = np.load(f)

plt.plot(data_vector[:,1],data_vector[:,0])
plt.show()
