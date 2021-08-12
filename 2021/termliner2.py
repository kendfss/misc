import sys, time

for x in range(10):
    # print(f'{x}', end='\r', flush=True)
    print(f'{x}', end='\r')
    time.sleep(.4)
    # sys.stdout.flush()
print("\n", flush=True)
