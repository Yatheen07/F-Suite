
import cv2
import numpy as np

image = cv2.imread(r'E:/F-Suite/Datasets/images/image3.jpg') # Image input
image = cv2.resize(image,(500,500))#,interpolation = cv2.INTER_AREA)
image_gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY) # GrayScale Conversion
template_image = cv2.imread(r'E:/F-Suite/leafTemplate.jpg',0) # Template input

    

w, h = template_image.shape[::-1]
     

result = cv2.matchTemplate(image_gray,template_image,cv2.TM_CCOEFF_NORMED)
     

threshold = 0.8

loc = np.where( result >= threshold) 

for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
    
cv2.imshow("Template Succesfully matched!" , image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
    
