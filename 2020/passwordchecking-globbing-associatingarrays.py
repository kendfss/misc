def check_password_exclusive(passwd:str,minlen:int=6) -> bool:
    long_enough = len(passwd)>=minlen
    alpha_numeric = passwd.isalnum()
    return long_enough and alpha_numeric
    
print(check_password_exclusive('I<3csc108!')) ## False
print(check_password_exclusive('time2sleep4me')) ## True


import glob,os
from m3ta import ffplay
result = glob.glob(os.path.join(os.path.expanduser('~'),'*melanie.wav'))
print(result)
ffplay(result,loop=False)

bmi = lambda weight, height: weight * 703/height**2
# names = input('Enter the names of the users, each separated by a comma\n\t').split(',')

# df = {
    # name.strip():[
        # int(input(f"What is {name.strip()}'s weight?\t(pounds)\n\t")),
        # int(input(f"What is {name.strip()}'s height?\t(inches)\n\t"))
    # ] for name in names
# }

# for k,v in df.items():print(f"{k}'s BMI is {bmi(*v)}")

A = 'China, India, France, Italy'.split(', ')
B = [2000, 3000, 3500, 1000]
C = {a:B[i] for i,a in enumerate(A)}

sort = sorted(C.keys(),key=C.get,reverse=True)
first = sort[0]
second = sort[1]
# etc


