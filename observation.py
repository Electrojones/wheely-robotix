import requests
from PIL import Image
import io
import numpy as np
from matplotlib import pyplot as plt
import cv2


#returns the position of the marker in the cameras field of view
def get_marker_pos():

    #get the image, extract it, make an array out of it and convert the colorspace
    r=requests.get("http://192.168.2.103:8080/shot.jpg")
    image = Image.open(io.BytesIO(r.content))
    image=np.asarray(image)
    image=cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    #boundaries to be considered blue
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([150,255,255])

    #search for blue areas
    mask=cv2.inRange(image, lower_blue, upper_blue)

    #locate blue pixels
    x_coll=[]
    y_coll=[]

    for y in range(len(mask)):
        for x in range(len(mask[0])):
            if(mask[y, x]==255):
                x_coll.append(x)
                y_coll.append(y)

    #calculate the center of blue in the image
    y_cen=sum(y_coll)/len(y_coll)
    x_cen=sum(x_coll)/len(x_coll)

    return (x_cen,y_cen), mask

if __name__ == "__main__":
    pos, mask=get_marker_pos()
    Image.fromarray(mask).save("Image.png")
    print(pos)
