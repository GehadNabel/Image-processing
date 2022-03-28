#!/usr/bin/env python
# coding: utf-8

# In[ ]:


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "from processImage import processImage"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "img = processImage('../Large_Scaled_Forest_Lizard.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0.00291502, 0.01306423, 0.02153928, 0.01306423, 0.00291502],\n",
       "       [0.01306423, 0.05854983, 0.09653235, 0.05854983, 0.01306423],\n",
       "       [0.02153928, 0.09653235, 0.15915494, 0.09653235, 0.02153928],\n",
       "       [0.01306423, 0.05854983, 0.09653235, 0.05854983, 0.01306423],\n",
       "       [0.00291502, 0.01306423, 0.02153928, 0.01306423, 0.00291502]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import gaussian\n",
    "\n",
    "gaussian_kernal = gaussian.generateGaussian(kernal_size=5, sigma = 1)\n",
    "gaussian_kernal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from convolve import convolve2D_single_Kernal\n",
    "\n",
    "gaussian_blured_image = convolve2D_single_Kernal(img, gaussian_kernal)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import cv2\n",
    "\n",
    "cv2.imwrite('gaussian_blured_lizard.jpg', gaussian_blured_image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Edge Detection Kernel (sopel operator)\n",
    "kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])\n",
    "kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])\n",
    "from convolve import convolve2D_multi_Kernal\n",
    "\n",
    "# Convolve and Save Output\n",
    "sobel_on_guassian_blured_image = convolve2D_multi_Kernal(gaussian_blured_image, kernel_x, kernel_y, padding=1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cv2.imwrite('sobel_on_guassian_blured_image_lizard.jpg', sobel_on_guassian_blured_image)"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "304db75e9ca8a0a1d93cf838a2ff5897596f4187479e0cbadfeb76277b9159f8"
  },
  "kernelspec": {
   "display_name": "Python 3.8.10 ('venv': venv)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

