from asyncore import read
from ctypes.wintypes import SIZE
from fileinput import filename
import cv2
import os 
os.system("clear")
path="sunrise-main/Images"
images=os.listdir(path)
allImages=[]
for i in images:
    filename=path+"/"+i
    allImages.append(filename)
frame=cv2.imread(allImages[0])
height,width,chanels=frame.shape
sizes=(width,height)
sunrise=cv2.VideoWriter("sunrise.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5,sizes)
for i in reversed (allImages):
    frame=cv2.imread(i)
    sunrise.write(frame)
sunrise.realese()
cv2.destroyAllWindows()
