import re

string = 'streetName=BENEDITO DE PAULA, QD 03 LT 03, state=AM, complement=SJ BANDEIRANTES, number=4, country=BRA'

# pairs = re.split(r'(\w+=)', string)[1:]   
parts = re.split(r'(\w+=)', string)#[1:]   
# pairs = [partitions[i],partitions[i+1]]
# for i in [a + b.strip(', ') for a, b in zip(pairs[::2], pairs[1::2])]:
pairs = {a.strip('=').strip('') : b.strip(', ').strip() for a, b in zip(parts[1::2], parts[2::2])}
    # print(i)
    
for p in pairs:
    print(p,pairs[p],sep='\t:\t')
