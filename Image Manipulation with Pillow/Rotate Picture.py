from PIL import Image
import os

image1 = Image.open('Bridge.jpg')
image1.rotate(90).save('Brige_rotate.jpg')