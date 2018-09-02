# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 12:10:40 2018

@author: kmy07
"""

import cv2
from PIL import Image
from statistics import median,mean

videoPath = r'D:\\Pictures\\videos\\video558464737.mp4'

def getMedianValue(image):
    return median(image.histogram())

def handleVideo(path,frame_index):
    counter = 0
    pixel_values = []
    video = cv2.VideoCapture(path)
    while(True):
        returnedValue , frame = video.read()
        if not returnedValue:
            break
        counter+=1
        if frame_index == -1:
            image = Image.fromarray(frame)
            pixel_values.append(getMedianValue(image))
        elif counter == frame_index:
            image = Image.fromarray(frame)
            image.save(r'D:\\Pictures\\videos\\result.png')
            return True,pixel_values
    
    video.release()
    cv2.destroyAllWindows()
    return False,pixel_values 



status,pixel_values = handleVideo(videoPath,-1)
frame_index = pixel_values.index(median(pixel_values))

status,junk = handleVideo(videoPath,frame_index)
if(status):
    print("Resultant Image Saved!")
else:
    print("Error in Key Frame Generation")

    
    