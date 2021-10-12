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
img = cv2.imread(path)
im = Image.open(path)
width, height = im.size
# img = cv2.resize(img, (0, 0),2,scale , scale)# boyut değiştirme


def mousePoints(event,x,y,flags,params):
    global counter,point1,point2,point3,point4,counter2,circles,myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter==0:
            point1=int(x),int(y)
            counter +=1
            myColor = (random.randint(0,2)*200,random.randint(0,2)*200,random.randint(0,2)*200 )## mouse'u tıklandığı yerde oluşacak olan circlenin rengi
        elif counter ==1:
            point2=int(x),int(y)
            counter += 1
            #myColor = (random.randint(0, 2) * 200, random.randint(0, 2) * 200, random.randint(0, 2) * 200)
        elif counter==2:
            point3 = int(x), int(y)
            counter += 1
            #myColor = (random.randint(0, 2) * 200, random.randint(0, 2) * 200, random.randint(0, 2) * 200)
        elif counter==3:
            point4 = int(x), int(y)
            #myColor = (random.randint(0, 2) * 200, random.randint(0, 2) * 200, random.randint(0, 2) * 200)
            myPoints.append([point1,point2,point3,point4])
            print(myPoints)
            print(point1)
            print(point2)
            print(point3)
            print(point4)

            pts1 = np.float32([point1, point2, point3, point4])
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

            M = cv2.getPerspectiveTransform(pts1, pts2) #dönüşüm matrisi

            dst = cv2.warpPerspective(img, M, (width, height))

            plt.subplot(121), plt.imshow(img), plt.title('Input')
            plt.subplot(122), plt.imshow(dst), plt.title('Output')


            cv2.imwrite('pers.png', dst)
            plt.show()
            counter += 1
            counter=0
        circles.append([x,y,myColor])
        counter2 += 1

while True:
    # To Display points
    for x,y,color in circles:
        cv2.circle(img,(x,y),3,myColor,cv2.FILLED)# r=3 olan x-y koordinatlarında içi dolu çember oluşturma
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('s'): #  s'ye basıldığında print özelliği aktif olacak
        print(myPoints)
        break