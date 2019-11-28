import requests
from PIL import Image
import io
import numpy as np
from matplotlib import pyplot as plt

r=requests.get("http://192.168.2.103:8080/shot.jpg")

print(r.content)

image = Image.open(io.BytesIO(r.content))

image.save("Image.jpg")

image=np.asarray(image)

print(image)

plt.imshow(image)
plt.show()