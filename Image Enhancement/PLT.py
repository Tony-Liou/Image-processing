# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:19:56 2019

@author: ltony

Image enhancement: Power Law Transformation

"""

import cv2
import numpy as np

# Read images

bright = cv2.imread("bright.png")
dark = cv2.imread("dark.png")
gray = cv2.imread("gray.png")
normal = cv2.imread("normal.png")

# Power law transformation: Gamma = 2 or 0.5

bright = bright/255.0
PLT_bright1 = cv2.pow(bright, 2)
PLT_bright2 = cv2.pow(bright, 0.5)

dark = dark/255.0
PLT_dark1 = cv2.pow(dark, 2)
PLT_dark2 = cv2.pow(dark, 0.5)

gray = gray/255.0
PLT_gray1 = cv2.pow(gray, 2)
PLT_gray2 = cv2.pow(gray, 0.5)

normal = normal/255.0
PLT_normal1 = cv2.pow(normal, 2)
PLT_normal2 = cv2.pow(normal, 0.5)

# Write images

cv2.imwrite("bright_gamma2.png", PLT_bright1*255)
cv2.imwrite("bright_gamma0.5.png", PLT_bright2*255)

cv2.imwrite("dark_gamma2.png", PLT_dark1*255)
cv2.imwrite("dark_gamma0.5.png", PLT_dark2*255)

cv2.imwrite("gray_gamma2.png", PLT_gray1*255)
cv2.imwrite("gray_gamma0.5.png", PLT_gray2*255)

cv2.imwrite("normal_gamma2.png", PLT_normal1*255)
cv2.imwrite("normal_gamma0.5.png", PLT_normal2*255)
'''
cv2.imshow('Bright', bright)
cv2.waitKey()
'''