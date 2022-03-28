#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2

# Grayscale Image
def processImage(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    return image

def convolve2D_multi_Kernal(image, kernel_x, kernel_y, padding=0, strides=1):
    # Cross Correlation
    kernel_x = np.flipud(np.fliplr(kernel_x))
    kernel_y = np.flipud(np.fliplr(kernel_y))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape, yKernShape = kernel_x.shape
    xImgShape, yImgShape = image.shape


    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))
    theta = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((xImgShape + padding*2, yImgShape + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
    else:
        imagePadded = image

    # Iterate through image
    for i in range(xImgShape):
        # Exit Convolution
        if i > xImgShape - xKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if i % strides == 0:
            for j in range(yImgShape):
                # Go to next row once kernel is out of bounds
                if j > yImgShape - yKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if j % strides == 0:
                        Gx = (kernel_x * imagePadded[i: i + xKernShape, j: j + yKernShape]).sum()
                        Gy = (kernel_y * imagePadded[i: i + xKernShape, j: j + yKernShape]).sum()
                        theta[i, j] = np.arctan(Gy / Gx)
                        Gx_square = np.square(Gx)
                        Gy_square = np.square(Gy)
                        G_sum_square = np.array([Gx_square, Gy_square]).sum()
                        G_root_sum_square = np.sqrt(G_sum_square)
                        output[i, j] = G_root_sum_square
                except:
                    break

    return output, theta

def convolve2D_single_Kernal(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))


    # Gather Shapes of Kernel + Image + Padding
    xKernShape, yKernShape = kernel.shape
    xImgShape, yImgShape = image.shape


    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((xImgShape + padding*2, yImgShape + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
    else:
        imagePadded = image

    # Iterate through image
    for i in range(xImgShape):
        # Exit Convolution
        if i > xImgShape - xKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if i % strides == 0:
            for j in range(yImgShape):
                # Go to next row once kernel is out of bounds
                if j > yImgShape - yKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if j % strides == 0:
                        G = (kernel * imagePadded[i: i + xKernShape, j: j + yKernShape]).sum()
                        output[i, j] = G
                except:
                    break

    return output

