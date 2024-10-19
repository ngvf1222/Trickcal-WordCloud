import cv2
import numpy as np
word=cv2.imread('word.png')
space=cv2.imread('maxresdefault.png')
background=cv2.imread('background.jpg')
mark=(space==[0,0,0])+0
img=word+mark*background
img = np.array(img, dtype=np.uint8)
cv2.imwrite('final_result.png',img)
