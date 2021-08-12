from m3ta import show, chords, join
# from m3ta import chords, join
# import m3ta 




string = str([*range(10)])

def remove(string,element):
    return string.replace(element,'')
    
print(remove(string,','))