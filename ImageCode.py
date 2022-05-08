from turtle import width
from PIL import Image

image = Image.open('Maze1.jpg')

imageConverted = image.convert("RGB")

width, height = image.size

for row in range(0, height):
    for column in range(0, width):    
        color = imageConverted.getpixel((column, row))
        print (color)
