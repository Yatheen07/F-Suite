# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:09:48 2018

@author: kmy07
"""
import pyrebase
from google.cloud import vision
from google.cloud import storage
from google.cloud.vision import types

def configure_firebase():
    config = {
        "apiKey": "AIzaSyAqdCtpkbuCgjCtxrYn1z7CxYEXFeLtj0A",
        "authDomain": "imagevision-2fdbf.firebaseapp.com",
        "databaseURL": "https://imagevision-2fdbf.firebaseio.com",
        "storageBucket": "imagevision-2fdbf.appspot.com",
        }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    image = storage.child ("Images/sampleVideo").download("Downloaded_Image.png")
    return storage.child ("Images/sampleVideo").get_url(None)
    

def get_gcpVision_client():
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\kmy07\\Desktop\\Image Vision-a7e6ee31ef4b.json"
    vision_client = vision.ImageAnnotatorClient()
    return vision_client

def detect_labels(vision_client,url):
    result = vision.types.Image()
    result.source.image_uri = url
    response = vision_client.label_detection(image=result)
    labels = response.label_annotations
    print('Labels:')
    Labels_list = []
    for label in labels:
        Labels_list.append(label.description)
        print(label.description)
        
    return Labels_list
        
vision_client = get_gcpVision_client()

Labels_list = detect_labels(vision_client,configure_firebase())

