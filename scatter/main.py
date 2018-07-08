import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.cbook as cbook

def colorfulCircles():
	np.random.seed(19680801)
	N = 50
	x = np.random.rand(N)
	y = np.random.rand(N)
	colors = np.random.rand(N)
	area = (39*np.random.rand(N))**2

	plt.scatter(x, y, s=area, c=colors, alpha=0.5)
	plt.show()

def colorfulShapes():
	np.random.seed(19680801)
	N = 50
	x = np.random.rand(N)
	y = np.random.rand(N)
	area = (39*np.random.rand(N))**2
	colors = np.sqrt(area)

	plt.scatter(x, y, s=area, c=colors, marker='^')
	
	x = np.random.rand(N)
	y = np.random.rand(N)
	area = (39*np.random.rand(N))**2
	colors = np.sqrt(area)
	plt.scatter(x, y, s=area, c=colors, marker='o')

	plt.show()

if __name__ == '__main__':
	colorfulCircles()
	colorfulShapes()