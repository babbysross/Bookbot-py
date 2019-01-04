import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bookshelf_test.jpg',0)

class grayscale(img):
    
    #IMREAD_GRAYSCALE = 0
    #IMREAD_COLOR = 1
    #IMREAD_UNCHANGED = -1


    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

grayscale()

##plt.imshow(img, cmap='gray', interpolation='bicubic')
##plt.plot([600,100],[80,100], 'c', linewidth=1)
##plt.show()
