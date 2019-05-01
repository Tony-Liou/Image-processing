# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:36:38 2019

@author: ltony

rotate the image 30 degrees clockwise
nearest neighbor interpolation
bilinear interpolation
"""
import cv2
import numpy as np
import math

# Read images
letter = cv2.imread("aletter.jpg")
scene = cv2.imread("scene.jpg")


def nni(img): # nearest-neighbor interpolation
    degree = 30 # clockwise 30 degrees
    theta = (degree / 180) * math.pi # radians
    csin = math.sin(theta)
    ccos = math.cos(theta)
    height, width, channels = img.shape
    #print(width, height, channels)
    length = math.ceil(height * (csin + ccos))

    tmp = np.zeros((length, length, channels), np.uint8)
    
    # offset
    nedge = (length - 1) / 2
    ox = -nedge * ccos - nedge * csin + (width - 1) / 2
    oy = nedge * csin - nedge * ccos + (height - 1) / 2
    
    for y in range(length):
        for x in range(length):            
            row = round(-x*csin + y*ccos + oy)
            col = round(x*ccos + y*csin + ox)
            if row >=0 and row < height and col >= 0 and col < width:
                tmp[y][x] = img[row][col]

    return tmp

def xvalue(x, width): # column bounding and floor the number
    if x < 0:
        x = 0
    elif x >= width:
        x -= 1
    return math.floor(x)

def yvalue(y, height): # row bounding and floor the number
    if y < 0:
        y = 0
    elif y >= height:
        y -= 1
    return math.floor(y)
    
def bi(img): # bilinear interpolation
    degree = 30 # clockwise 30 degrees
    theta = (degree / 180) * math.pi # radians
    csin = math.sin(theta)
    ccos = math.cos(theta)
    height, width, channels = img.shape
    #print(width, height, channels)
    length = math.ceil(height * (csin + ccos))

    tmp = np.zeros((length, length, channels), np.uint8)
    
    # offset
    nedge = (length - 1) / 2
    ox = -nedge * ccos - nedge * csin + (width - 1) / 2
    oy = nedge * csin - nedge * ccos + (height - 1) / 2
    
    for y in range(length):
        for x in range(length):            
            srcy = -x*csin + y*ccos + oy
            srcx = x*ccos + y*csin + ox
            if srcy >=0 and srcy < height and srcx >= 0 and srcx < width:
                u = srcx - int(srcx)
                v = srcy - int(srcy)
                tmp[y][x] = ((1 - u) * (1 - v) * img[yvalue(srcy, height)][xvalue(srcx, width)] +
                        u * (1 - v) * img[yvalue(srcy, height)][xvalue(srcx + 1, width)] +
                        (1 - u) * v * img[yvalue(srcy + 1, height)][xvalue(srcx, width)] +
                        u * v * img[yvalue(srcy + 1, height)][xvalue(srcx + 1, width)])

    return tmp
    
img = nni(letter)
cv2.imwrite('nni_letter.jpg', img)

img = nni(scene)
cv2.imwrite('nni_scene.jpg', img)

img = bi(letter)
cv2.imwrite('bi_letter.jpg', img)

img = bi(scene)
cv2.imwrite('bi_scene.jpg', img)
#cv2.imshow('res', img)
