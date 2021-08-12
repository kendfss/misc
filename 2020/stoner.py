"""
Take two sets x,y. let their common derivative be the function that grows where they overlap and changes direction wherever they do not.
check for: 
    dx==dy
    sign(dx)==sign(dy)
    
"""
import math
import numpy as np, matplotlib.pyplot as plt

deltas = lambda iterable: tuple(iterable[i]-iterable[i-1] for i in range(1,len(iterable)))
sign = lambda x: True if x>0 else False if x<0 else None

domain = np.linspace(0,2*np.pi,1000)
x,y = np.cos,np.sin
X,Y = list(x(domain)), list(y(domain))
# print(domain,x(domain),y(domain),sep='\n',end='\n\n')

deldom = np.linspace(0,2*np.pi,1001)
dx,dy,dd = deltas(x(deldom)),deltas(y(deldom)),deltas(deldom)
# print(dx,dy,sep='\n',end='\n\n')

z0,z1,z2,z3,z4,z5 = [],[],[],[],[],[]
r0,r1,r2,r3,r4,r5 = 0,0,0,0,0,0


for i in list(domain)[:len(list(domain))]: 
    # j = deltas(domain)[domain.index(i)]
    j = list(domain).index(i)
    
    r0 += 1 if X[j]==Y[j] else -1
    z0.append(r0)
    
    r1 += 1 if sign(X[j])==sign(Y[j]) else -1
    z1.append(r1)
    
    r2 += 1 if dx[j]==dy[j] else -1
    z2.append(r2)

    r3 += 1 if sign(dx[j])==sign(dy[j]) else -1
    z3.append(r3)
    
    r4 += 1 if sign(dx[j])==sign(dd[j]) else -1
    z4.append(r4)
    
    r5 += 1 if sign(dy[j])==sign(dd[j]) else -1
    z5.append(r5)
    
    # print(j)
    # if x(i)**2==y(i)**2: 
        # register += 1
        # z.append(register)
    # else:
        # register -= 1
        # z.append(register)



fig,ax = plt.subplots()

# ax.plot(domain,np.sin(domain),label='x')
# ax.plot(domain,np.cos(domain),label='y')
ax.plot(domain,z0,label='z0 - value agreement')
ax.plot(domain,z1,label='z1 - sign agreement')
ax.plot(domain,z2,label='z2 - delta agreement')
# ax.plot(domain,z3,label='z3 - delta sign agreement')
# ax.plot(domain,z4,label='z4 - delta sign agreement (x,dom)')
# ax.plot(domain,z5,label='z5 - delta sign agreement (y,dom)')


ax.legend()
fig.show()