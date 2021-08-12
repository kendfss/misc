import math

import matplotlib.pyplot as plt, numpy as np

def sum(start,iterations,base=1):
    for i in range(iterations):
        start += base*i
    return start
def prod(start,iterations,base=2):
    for i in range(iterations):
        start *= base*i
    return start

# sumprod = tuple((sum(1,100),prod(1,100)))
for i in range(100):
    print(i,prod(1,i,i))
sums = tuple(sum(0,i,1) for i in range(100))
prods = tuple(prod(1,i) for i in range(100))
# print(sums)
print(prods)
x = tuple(i for i in range(100))
y = tuple(((i-1)/2)*(i) for i in range(100))
# print(ts==sums)

# fig, ax = plt.subplots(2,1)
# ax[0].plot(x,y)
# ax[1].plot(x,np.log(y))
fig, ax = plt.subplots(2,1)
ax[0].plot(x,sums,label='sums')
ax[0].plot(x,np.log(sums),label='ln sums')

ax[1].plot(x,np.log(prods),label='ln prods')
# ax[1].plot(x,prods,label='prods')

ax[0].legend()
ax[1].legend()
fig.show()

