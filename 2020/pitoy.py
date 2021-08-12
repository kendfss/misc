import numpy as np

from m3ta import freq, entropy

import math

# print(len(str(math.e))/len(str(np.e)))
# print(np.pi,np.e,sep='\n',end='\n\n')

pi = str(np.pi)

l = lambda x: len(str(x))
rat = lambda x: x.as_integer_ratio()
for i in range(3,len(pi)):
    z = float(pi[:i])
    rz = rat(z)
    print(i-2,z,rz[0]/rz[1],entropy(z,mode='shan'),sep=' ... ',end='\n\n')
    
    
numerators = tuple(rat(float(pi[:i]))[0] for i in range(2,len(pi)))
denominators = tuple(rat(float(pi[:i]))[1] for i in range(2,len(pi)))
# for z in zip(numerators,denominators): print(z,z[0]/z[1])

all = numerators + denominators
# print(all)
# for i in enough: print(i,entropy(i,mode='shan')) if freq(i,all) > 1 else print()

enough = set(all)
enough = sorted(list(enough))
# print(enough)
# print(len(enough)/len(all))

popular = tuple(i for i in enough if freq(i,all)>1)
popularity = tuple((i,freq(i,all)) for i in enough); print(popularity)
# print(popular) #[2251799813685248, 562949953421312, 1125899906842624]
# for i in popular: print(freq(i,all),i,entropy(i,mode='shan'),sep=' ... ',end='\n\n')
