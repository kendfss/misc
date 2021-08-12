"""
How to find missing number in a string of numbers with no separator in python?
    https://stackoverflow.com/questions/64289404/how-to-find-missing-num..
        Parse a string of digits into integers, check if it has any incomplete sequences of consecutive integers, fill in the blanks
        
Cannot work if the first integer is longer than a third of the sequence length
"""

from m3ta import factors,powerset,chords
from itertools import combinations,chain,product,combinations_with_replacement as cwr

examples = {
    89101113:12,
    9899101102:100,
    596597598600601602:599,
    909192939495969798100101:99,
    11111211311411511:-1,
    11111311511:[112,114],
    1234567812345680:12345679
}
t = str(list(examples.keys())[0])
# def split(string,sizes):
    # if not len(string)%sizes:
        # return [string]
def split(sequence, x):
    return sequence[:x], sequence[x:]

def parse(digits):
    """
    Try to parse "digits" into numbers, and find the missing one.

    The numbers will have no more than six digits.
    Return -1 if "digits" isn't parseable or isn't missing one.

    >>> parse("89101113")  # 8, 9, 10, (12), 13
    12
    >>> parse("9899101102")  # 98, 99, (100), 101, 102
    100
    >>> parse("596597598600601602")  # 596, 597, 598, (599), 600, 601, 602
    599
    >>> parse("909192939495969798100101")  # 90, ...
    99
    >>> parse("11111211311411511")  # Looks like "111, ..." but isn't
    -1
    """
    for n in range(1, len(digits)+1):
        expected, remainder = split(digits, n)
        failures = []
        while len(failures) <= 1 and remainder:
            expected = str(int(expected) + 1)
            actual, remainder = split(remainder, len(expected))
            if actual != expected:
                failures.append(expected)
                remainder = actual + remainder  # Re-parse
        if len(failures) == 1:
            return int(failures[0])
    return -1

for k,v in examples.items():
    print(parse(str(k)))