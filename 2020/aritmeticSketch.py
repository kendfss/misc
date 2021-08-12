maxDigit = lambda x: max(int(i) for i in str(x))
# minBase = lambda x: maxDigit(x)+1
# def add(x,y,base=10)

# def successor(value,base)

class Arithmetic:
    def __init__(self,base,origin=0):
        self.atoms = atoms
        self.base = base
        self.origin = origin
    def succ(self,value):
        if maxDigit(value)<self.base:
            pass
        else:
            raise ValueError(f'Argument is locally undefined. Choose an argument whose maximal digit is no greater than {self.base}')
        
        # if value==self.root:
            # return int(str(self.root).replace(str(self.root),str(self.base)))
        # elif 