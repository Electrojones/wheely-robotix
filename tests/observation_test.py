import requests
from PIL import Image
import io
import numpy as np
from matplotlib import pyplot as plt
import cv2

r=requests.get("http://192.168.2.111:8080/shot.jpg")

#print(r.content)

image = Image.open(io.BytesIO(r.content))

#image.save("Image.jpg")
image=np.asarray(image)
print(image)
print("---")
image=cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
lower_blue = np.array([90,50,50])
upper_blue = np.array([150,255,255])
print(image)

mask=cv2.inRange(image, lower_blue, upper_blue)


Image.fromarray(mask).save("Image.png")

x_coll=[]
y_coll=[]

for y in range(len(mask)):
    for x in range(len(mask[0])):
        if(mask[y, x]==255):
            x_coll.append(x)
            y_coll.append(y)

print(len(image))

print(sum(y_coll)/len(y_coll))
print(sum(x_coll)/len(x_coll))
