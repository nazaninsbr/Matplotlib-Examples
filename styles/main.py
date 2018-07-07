import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
import math

styles = plt.style.available 
dataX = np.random.randn(50) 
dataY = np.random.randn(50) 


for i in range(len(styles)):
	plt.subplot(math.sqrt(len(styles)), math.sqrt(len(styles)), i+1)
	plt.style.use(styles[i])
	plt.scatter(dataX, dataY)

plt.show()
