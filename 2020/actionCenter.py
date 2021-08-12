import os

import numpy
from PIL import Image

picdirs = 'C:\Users\Kenneth\Pictures\Saved Pictures*'.split('*')

def subFiles(path):
    return [os.path.join(path,name) for name in os.listdir(path) if not os.path.isdir(os.path.join(path,name))]
for path in picdirs:
    for pic in subFiles(path):
        with Image.open(pic) as im:
            print(im.))