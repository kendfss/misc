import math

import numpy as np, matplotlib.pyplot as plt
# help(np.sin)
# print(np.sin(2*np.pi))

# fig, ax = plt.subplots(2,1)
# ax[0].plot(np.linspace(0,360,1000),np.sin(np.linspace(0,360,1000)))
# ax[1].plot(np.linspace(0,2*np.pi,1000),np.sin(np.linspace(0,2*np.pi,1000)))
# ax.set_title("sin(x): 0 <= x <= 2pi")
# fig.title("")
# fig.show()

def pythagoras(h=0,x=0,y=0):
    if h==0: return x**2 + y**2
    elif x==0: return h**2 - y**2
    elif y==0: return h**2 - x**2
    return True if h**2 == x**2 + y**2 else False
    
def sctAngle(hyp=0,adj=0,opp=0):
    if hyp==0: return math.arctan(opp/adj)
    elif adj==0: return math.arcsin(opp/hyp)
    elif opp==0: return math.arccos(adj/hyp)
    

def segmentArea(radius,chordLength):
    # angle = 2*np.arcsin(chordLength/(2/radius))
    opp = chordLength/2
    adj = (radius**(2) - opp**(2))**(1/2)
    # print(opp/radius,adj/radius)
    a = 2 * math.asin(opp/radius)
    b = 2 * math.acos(adj/radius)
    
    conv = 180/np.pi
    angle = a
    return ((angle-math.sin(angle))*radius**(2))/2
    
circumference = lambda x: 2*np.pi*x
area = lambda x: np.pi*x*x


def calc(radius,partitions):
    circ = circumference(radius)
    arcLen = circ/partitions
    angle = (2*np.pi)/partitions
    chordLen = math.sin(angle/2)*radius
    return (segmentArea(radius,chordLen),chordLen,arcLen)
    
