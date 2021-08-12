# Q: is "[om[om[om]]]" a possible object?

class om(dict):
    def __hash__(self):
        return hash(str(self))


# o = ''

print([om[om[om]]])