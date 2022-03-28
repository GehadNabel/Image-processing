#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2

# Grayscale Image
def processImage(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    return image

