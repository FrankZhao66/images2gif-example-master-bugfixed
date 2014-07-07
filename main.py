#!/usr/bin/env python
from images2gif import writeGif
from PIL import Image
import os

file_names = ['doge1.jpg', 'doge2.jpg', 'doge3.jpg', 'doge4.jpg', 'doge5.png']

images = [Image.open(fn) for fn in file_names]
size = (300,350)

for key in range(len(images)):
    images[key]=images[key].resize(size)

filename = "doge.gif"

writeGif(filename, images, duration=0.2, subRectangles=False)