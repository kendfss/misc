from itertools import combinations, permutations

def checker(pair):
	x,y = pair
	for i in range(len(x)):
		yield True if x[i]==y[i] else False
		
iterates = lambda x: hasattr(x,'__iter__')
finity = lambda x: hasattr(x,'__len__')
generate = lambda x: (i for i in x) if iterates(x) else None
def getStationaryPoints(*args,strict=False):
    "doomed to fail if no finite argument is given"
    assert all(all(iterates(i) for i in args)), "Argument(s) does not support iteration, choose one that does"
    pairs = combinations(args,2)
    assert all(len(pair[0])==len(pair[1]) for pair in pairs), "Argument lengths do not agree"
    
    invariances = []
    if len(args) == 1:
        arg = args[0]
        for i in range(1,len(arg)):
            if arg[i]==arg[i-1]:
                invariances.append(i)
        return invariances
    elif strict:
        sequencers = tuple(arg for arg in args if finite(finite))
        sequencer = sequencers[0]
        time = 0
        while time < len(sequencer):
            state = (next(arg))
            
            time += 1
    else:
        pass
def hasStationaryPoints(pair):
	if len(pair) == 2:
		x,y = pair
		if len(x) != len(y):
			main = y if len(x)>len(y) else x
			extension = y if len(x)<len(y) else x
			return True if any(checker((main,extension))) else False
		else:
			return True if any(checker(pair)) else False
	else:
		raise Exception('The argument must be an iterable of length two')

if __name__ == '__main__':
    
	# from itertools import combinations, permutations
	# base = 'rgba'
	# perms = tuple(''.join(i) for i in permutations(base,len(base)))
	# combs = combinations(perms,2)
	# pairs = tuple(pair for pair in combs if pair[0] == base)
	
	# for pair in pairs:
        # print(getStationaryPoints(pairs))
		# if not hasStationaryPoints(pair):
			# print(pair)
	# print('')
	
	# for pair in pairs:
		# if hasStationaryPoints(pair):
			# print(pair)
            
    pass