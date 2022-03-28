#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import numpy as np

def generateGaussian(kernal_size=5, sigma=1):
    gaussian_kernal = np.zeros((kernal_size, kernal_size))
    center = kernal_size / 2
    left =  - math.floor(center)
    right = math.ceil(center)
    coordinates_list = [*range(left, right)]
    coordinates_list_copy_reverse = coordinates_list.copy()
    coordinates_list_copy_reverse.reverse()


    coordinates_list.reverse()
    for i, y in enumerate(coordinates_list_copy_reverse):
        for j, x in enumerate(coordinates_list):
            sum_x2_y2 = np.square([x, y]).sum()
            exp_denominator = 2 * np.square(sigma)
            gaussian_kernal[i, j] = np.exp(-(sum_x2_y2 / (exp_denominator))) / (exp_denominator * np.pi)

    return gaussian_kernal

