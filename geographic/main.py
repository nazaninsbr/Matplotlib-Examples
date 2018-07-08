import matplotlib.pyplot as plt 
import numpy as np 


def one():
	plt.figure()
	plt.subplot(111, projection='aitoff')
	plt.grid(True)
	plt.show()

def two():
	plt.figure()
	plt.subplot(111, projection='lambert')
	plt.grid(True)
	plt.show()

def polar():
	fig = plt.figure()
	ax = fig.add_subplot(111, polar=True)
	r = np.arange(0,1,0.001)
	theta = 2 * 2*np.pi * r
	line, = ax.plot(theta, r, color='#ee8d18', lw=3)

	ind = 800
	thisr, thistheta = r[ind], theta[ind]
	ax.plot([thistheta], [thisr], 'o')
	ax.annotate('a polar annotation',
	            xy=(thistheta, thisr),  # theta, radius
	            xytext=(0.05, 0.05),    # fraction, fraction
	            textcoords='figure fraction',
	            arrowprops=dict(facecolor='black', shrink=0.05),
	            horizontalalignment='left',
	            verticalalignment='bottom',
	            )
	plt.show()


if __name__ == '__main__':
	one()
	two()
	polar()