from m3ta import kbd, main

def monoalphabetic(message:str, shift:int, decode:bool=False, alphabet:str=kbd(), space:str=None) -> str:
    words = message.split(space)
    for index, word in enumerate(words):
        new = ''
        for letter in word:
            if decode:
                substitute = alphabet[(alphabet.index(letter) - shift) % len(alphabet)]
            else:
                substitute = alphabet[(alphabet.index(letter) + shift) % len(alphabet)]
            new += substitute
        words[index] = new
    if space == None:
        space = ' '
    return space.join(words)


if eval(main):
    test = "Some kernels are more markov than others"
    for i in range(10):
        print(i)
        ft = monoalphabetic(test,i)
        print(ft)
        print(monoalphabetic(ft,i,True))
        print(2*'\n')