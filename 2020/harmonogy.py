"""
https://stackoverflow.com/questions/64284406/when-i-run-the-mathematical-formula-code-to-draw-harmonograph-it-says-cos-is-no
"""

import numpy as np
import matplotlib.pyplot as plt
# import math
from math import cos,sin
a=(1,2,3,4)
b=(4,5,5,5)
t=1
# x= (a + b)cos(t)-bcos((a/b + 1)t)
x = tuple((a[i] + b[i])*cos(t)-b[i]*cos((a[i]/b[i] + 1)*t) for i in range(len(a)))
# y= (a + b)sin(t)-bsin((a/b + 1)t)
y = tuple((a[i] + b[i])*sin(t)-b[i]*sin((a[i]/b[i] + 1)*t) for i in range(len(a)))
plt.plot(x,y)
plt.show()