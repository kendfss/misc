# for var in range(0,len(x)):
# if x[var] in y:
  # z.append(x)
  # print(z) 
  

x = 'abc'   
y = 'abcdefg' 
z = []

for char in x:
    if char in y:
        z.append(char)

z2 = [char for char in x if char in y] # alternatively