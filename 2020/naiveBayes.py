from math import pi, sqrt, exp

mean = lambda array: sum(array)/len(array)
variance = lambda array: sum([(i-mean(array))**2 for i in array])/(len(array)-1)
stDev = lambda array: variance(array)**(1/2)

summarizeTable = lambda table: [(mean(column), stDev(column), len(column)) for column in zip(*table)][:-1]
summarizeClasses = lambda x: {key:summarizeTable(val) for key,val in x.items()}

gaussian = lambda x,a,b,c: a*exp((-1/2)*((x-b)/c)**2)
probabilities = lambda array: tuple(gaussian(i,1/stDev(array)*sqrt(2*pi),stDev(array)) for i in array)
    
# f(dom) = (1 / sqrt(2 * PI) * stDev(dom)) * exp(-((x-mean(dom))^2 / (2 * sigma^2)))

def parser(dataset):
    frame = {}
    with open(dataset,'r') as d:
        table = d.readlines()
        for line in table:
            key = line.split(',')[-1].strip('\n') if isinstance(line,str) else line[-1]
            values = tuple(float(i) for i in line.split(',')[:-1])
            if key not in frame.keys(): frame[key] = []
            frame[key].append(values)
    return frame

ds = r"E:\Resources\dataSets\Loosies\Iris Flower Species Dataset.csv"
df = parser(ds)
print(df)
for key,val in df.items(): print(key,len(val))

for i,j,k in zip(*df): print(i,j,k)


# print(summaries)

dataset = [
    [3.393533211,2.331273381,0],
	[3.110073483,1.781539638,0],
	[1.343808831,3.368360954,0],
	[3.582294042,4.67917911,0],
	[2.280362439,2.866990263,0],
	[7.423436942,4.696522875,1],
	[5.745051997,3.533989803,1],
	[9.172168622,2.511101045,1],
	[7.792783481,3.424088941,1],
	[7.939820817,0.791637231,1]
]

def ds2dict(ds):
    keys = set(row[-1] for row in ds)
    frame = {}
    for key in keys:
        frame[key] = [row[:-1] for row in ds if row[-1]==key]
    return frame

# print(summarizeTable(dataset)==[(5.178333386499999, 2.7665845055177263, 10), (2.9984683241, 1.218556343617447, 10)])
print(summarizeClasses(ds2dict(dataset)))
"""
0
(2.7420144012, 0.9265683289298018, 5)
(3.0054686692, 1.1073295894898725, 5)
1
(7.6146523718, 1.2344321550313704, 5)
(2.9914679790000003, 1.4541931384601618, 5)
"""

# Test Gaussian PDF
print(calculate_probability(1.0, 1.0, 1.0))
print(calculate_probability(2.0, 1.0, 1.0))
print(calculate_probability(0.0, 1.0, 1.0))
0.3989422804014327
0.24197072451914337
0.24197072451914337