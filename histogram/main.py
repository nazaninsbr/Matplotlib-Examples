import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)


mu = 100 #mean_of_distribution
sigma = 15 #deriviation_of_distribution
x = mu + sigma * np.random.randn(437)

num_bins = 50


fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=1)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')

fig.tight_layout()
plt.show()