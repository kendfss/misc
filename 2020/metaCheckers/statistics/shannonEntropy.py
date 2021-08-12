from math import log
from itertools import combinations, chain

from meta import freq, sigma, alphabet


string = 'aabbccdd'

def shannonEntropy(iterable):
	"""
	Returns the Information, or Shannon, Entropy of an iterable
	Dependencies: math.log, meta.sigma, meta.freq
	Argument: 1-d iterable
	Output: float
	"""
	weights = {j:freq(j,iterable)/len(iterable) for j in set(iterable)}
	return -sigma([val*log(val,2) for val in weights.values()])

strings = ['aaaaaaaa','baadabac','dbcadacb','aabbccdd']
for string in strings: print(string,shannonEntropy(string))
print(strings,shannonEntropy(strings))