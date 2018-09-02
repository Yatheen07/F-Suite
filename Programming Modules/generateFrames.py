import cv2
import numpy as np
path = r'E:/F-Suite/Datasets/'
video = cv2.VideoCapture(r'E:/F-Suite/Datasets/VID_20180727_230614.mp4')
count=1

returnn,frame = video.read()

while(returnn):
    print(path+"images/image"+str(count)+".jpg")
    cv2.imwrite(path+"images/image"+str(count)+".jpg",frame)
    returnn,frame = video.read()
    if cv2.waitKey(10) == 27:
      break
    count += 1

