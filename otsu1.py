import cv2
import numpy as np
from matplotlib import pyplot as plt
#import necessary packages

img = cv2.imread('Image 11.JPG',0)#read image



# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_OTSU)


# plot all the images and their histograms
images = [img, 0, th2]
titles = ['Original Noisy Image','Histogram',"Otsu's Thresholding"]#Apply titles

for i in xrange(1):#Apply for loop
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()#show Image
