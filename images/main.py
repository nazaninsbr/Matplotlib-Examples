import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np 

img = mpimg.imread('./image.png')
plt.subplot(3, 3, 1)
plt.imshow(img)

lum_img = img[:, :, 0]
plt.subplot(3, 3, 2)
plt.imshow(lum_img)

plt.subplot(3, 3, 3)
plt.imshow(lum_img, cmap="hot")

plt.subplot(3, 3, 4)
plt.imshow(lum_img, clim=(0.2, 0.7))

plt.subplot(3, 3, 5)
plt.hist(lum_img.ravel(), bins=256, range=(0.0, 1.0), fc='k', ec='k')


plt.subplot(3, 3, 6)
plt.imshow(lum_img, clim=(0.7, 0.7))


plt.subplot(3, 3, 7)
plt.imshow(lum_img, cmap="hot", clim=(0.0, 0.1))


plt.subplot(3, 3, 8)
plt.imshow(lum_img, cmap="hot", clim=(0.0, 0.2))


plt.subplot(3, 3, 9)
plt.imshow(lum_img, clim=(0.0, 0.4))


plt.show()