import os
import time
from itertools import cycle
from subprocess import run


a=input("Enter a number: ")

run('clear')
#os.system('cls')
print(a)
a=input("Enter a number: ")

run('clear')
#os.system('clear')
print(a)
a=input("Enter a number: ")
run('clear')
#os.system('clear')
print(a)

os.system('date')

statements = cycle(("This is a multi-line screen print test",
    "Line 1",
    "Line 2",
    """
    triple quotes go hard
    """
))

while(1):
    
    # os.system('cls')
    
    
    print(next(statements))
    time.sleep(.5)
    os.system('clear')