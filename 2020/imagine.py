import numpy as np

class Pixel:
    def __init__(self,red=0,green=0,blue=0,alpha=0,location=(0,0)):
        self.red = red if red < 256 else 255
        self.green = green if green < 256 else 255
        self.blue = blue if blue < 256 else 255
        self.alpha = alpha if alpha < 256 else 255
        self.x = location[0]
        self.y = location[1]
    def __repr__(self):
        rep = self.red,self.green,self.blue,self.alpha,self.x,self.y
        return str(rep)
        
    def mirror(self,other):
        self.red = other.red
        self.green = other.green
        self.blue = other.blue
        
    def getR(self):
        return self.red
        
    def getG(self):
        return self.green
    
    def getB(self):
        return self.blue
        
    def getA(self):
        return self.alpha
    
    def setR(self,value):
        self.red = value
    
    def boostR(self,value):
        self.red += value if self.red+value < 256 else 255-self.red
        
    def cut(self,value,dimension):
        eval(f"self.{dimension} -= value if self.{dimension}-{value} > 0 else self.{dimension}")
        
    
# testPixel = Pixel(1)
# print(testPixel)
# testPixel.cut(256,'red')
# print(testPixel)
# testPixel.boostR(256)
# print(testPixel)

class Image:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.frame = [[Pixel(location=(i,j)) for i in range(self.width)] for j in range(self.height)]
        # self.content = [Pixel(location=(i,j)) for i]
        
    def __repr__(self):
        return str(self.frame)
        
    def flat(self):
        return np.array(self.frame).flat
        
    def getPixel(self,x,y):
        return tuple(pixel for pixel in self.flat() if pixel.x==x and pixel.y==y)[0]
        
testImage = Image(2,3)
print(testImage.flat())
for i in testImage.flat(): print(i)

print('retrieved:',testImage.getPixel(1,1))