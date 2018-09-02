# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 01:51:50 2018

@author: yatheen!
"""

import cv2

videoPath = r'D:\\Pictures\\videos\\video1509089841.mp4'
video = cv2.VideoCapture(videoPath)

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def getFile_size(file_path):
    import os
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

def analyzeVideo(path):
    from moviepy.video.io.VideoFileClip import VideoFileClip
    video = VideoFileClip(path)
    return video.duration,video.aspect_ratio,video.filename,video.fps

def getMetaData(path,video):
    meta_data = dict()
    meta_data.clear()
    meta_data["Duration"],meta_data["Aspect Ratio"],meta_data["Filename"],meta_data["FPS"] = analyzeVideo(path)
    
    meta_data["#frames"] = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    meta_data["Extension"] = meta_data["Filename"].split(".")[-1]
    meta_data["Size"] = getFile_size(path)
    return meta_data


meta_data = getMetaData(videoPath,video)
