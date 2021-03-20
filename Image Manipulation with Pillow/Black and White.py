from PIL import Image
import os

image1 = Image.open('Bridge.jpg')
image1.convert(mode='L').save('Bridge_White_and_Black.jpg')