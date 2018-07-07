import matplotlib.pyplot as plt 
import matplotlib 
import numpy as np 

def line():
	plt.plot([1,2, 3, 4])
	plt.ylabel('some numbers')
	plt.show()

def dots():
	plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
	plt.axis([0, 6, 0, 20])
	plt.show()

def sin():
	t = np.arange(0.0, 2.0, 0.01)
	s = 1+ np.sin(2*np.pi*t)
	fig, ax = plt.subplots()
	ax.plot(t, s)
	ax.grid()
	plt.show()


if __name__ == '__main__':
	line()
	dots()
	sin()