# -*- coding: utf-8 -*-
"""pixels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XxtIQzSRehzMfmyxWLRZI2XxBDgz1WrX
"""

import cv2
from PIL import Image
from google.colab.patches import cv2_imshow
import numpy as np
from matplotlib import pyplot as plt

img=Image.open('sample.jpg')
img1=cv2.imread("sample.jpg",1)
cv2_imshow(img1)
img

sh=img1.shape
sh

r=[]
g=[]
b=[]

for i in range(sh[0]):
  t1=[]
  t2=[]
  t3=[]
  for j in range(sh[1]):
    t1.append(img1[i][j][0]) 
    t2.append(img1[i][j][1])
    t3.append(img1[i][j][2])
  b.append(t1)
  g.append(t2)
  r.append(t3)

#r,g,b will have the rgb values of sample.jpg
