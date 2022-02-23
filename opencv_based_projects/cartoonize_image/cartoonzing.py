import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread("cat.png")

# Convert to gray scale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

# Median filter
img_blur = cv2.medianBlur(img_gray, 7)

#Use adaptive thresholding to create an edge mask
img_edge = cv2.adaptiveThreshold(img_blur, 255,
   cv2.ADAPTIVE_THRESH_MEAN_C,
   cv2.THRESH_BINARY,
   blockSize=3,
   C=2)
 # Apply mask
#img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)

dst = np.zeros(img_gray.shape)


# Add the thick boundary lines to the image using 'AND' operator
dst = cv2.bitwise_and( img_rgb, cv2.cvtColor(img_rgb, cv2.COLOR_RGB2YCrCb), mask =img_edge)
#dst = cv2.bitwise_and( img_rgb, img_rgb, mask =img_edge)

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.imshow(img_rgb)
plt.title('original image')
plt.axis('off')

ax2 = fig.add_subplot(1,2,2)
ax2.imshow(dst)
plt.title('cartoonize image')
plt.axis('off')

plt.savefig("test.png", bbox_inches='tight')
plt.show()
