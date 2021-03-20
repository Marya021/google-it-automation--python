from PIL import Image, ImageFilter
import os

image1 = Image.open('Bridge.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('Blurnies.jpg')