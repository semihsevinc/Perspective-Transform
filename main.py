import cv2
import random
import numpy as np
import mapper
import matplotlib.pyplot as plt
from PIL import Image


path = 'source.jpeg'
scale = 0.5
circles = []
counter = 0
counter2 = 0
point1= []
point2= []
point3= []
point4= []
myPoints = []
myColor= []

img = cv2.imread(path,)
im = Image.open(path)
width, height = im.size

def mousePoints(event,x,y,flags,params):
    global counter,point1,point2,point3,point4,counter2,circles,myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter==0:
            point1=int(x),int(y)
            counter +=1
            myColor = (0,0,255)
        elif counter ==1:
            point2=int(x),int(y)
            counter += 1
        elif counter==2:
            point3 = int(x), int(y)
            counter += 1
        elif counter==3:
            point4 = int(x), int(y)

            myPoints.append([point1,point2,point3,point4])
            pts1 = np.float32([point1, point2, point3, point4])
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

            M = cv2.getPerspectiveTransform(pts1, pts2) #transform matrix

            dst = cv2.warpPerspective(img, M, (width, height))

            plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Orijinal Görüntü')
            plt.subplot(122), plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)), plt.title('Kuş Bakışı Görüntü')
            cv2.imwrite('pers.png', dst)
            plt.show()

            counter += 1
            counter=0
        circles.append([x,y,myColor])
        counter2 += 1

while True:
    # To Display points
    for x,y,color in circles:
        cv2.circle(img,(x,y),5,myColor,cv2.FILLED)
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(myPoints)
        break