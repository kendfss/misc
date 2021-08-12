"""
Taken from
    https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python
"""

import random, string, re, subprocess, uuid
from m3ta import shuffle
from typing import Optional

print(str(uuid.uuid4()))

# guid = lambda: subprocess.run("powershell;'{'+[guid]::NewGuid().ToString()+'}'")


# defining function for random 
# string id with parameter 
def ran_gen(size, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for x in range(size)) 

# function call for random string 
# generation with size 8 and string  
print(ran_gen(8, "AEIOSUMA23"))
    
    

def generate_uuid():
    random_string = ''
    random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uuid_format = [8, 4, 4, 4, 12]
    for n in uuid_format:
        for i in range(0,n):
            random_string += str(random_str_seq[random.randint(0, len(random_str_seq) - 1)])
        if n != 12:
            random_string += '-'
    return random_string
print(generate_uuid())



def get_windows_uuid() -> Optional[uuid.UUID]:
    try:
        # Ask Windows for the device's permanent UUID. Throws if command missing/fails.
        txt = subprocess.check_output("wmic csproduct get uuid").decode()
        # txt = subprocess.check_output("powershell;'{'+[guid]::NewGuid().ToString()+'}'").decode()
        
        # Attempt to extract the UUID from the command's result.
        match = re.search(r"\bUUID\b[\s\r\n]+([^\s\r\n]+)", txt)
        if match is not None:
            txt = match.group(1)
            if txt is not None:
                # Remove the surrounding whitespace (newlines, space, etc)
                # and useless dashes etc, by only keeping hex (0-9 A-F) chars.
                txt = re.sub(r"[^0-9A-Fa-f]+", "", txt)

                # Ensure we have exactly 32 characters (16 bytes).
                if len(txt) == 32:
                    return uuid.UUID(txt)
    except:
        pass # Silence subprocess exception.

    return None

print(get_windows_uuid())

print('\n10010101001\n')
#mine
def guid():
    import random,string
    example = "xBeiPwtw-XYU3-et3p-AFaB-MvqcqrcnYwwj"
    chars = ''.join(i for i in shuffle(string.ascii_uppercase + string.digits+string.ascii_lowercase))
    ranstr = [(random.choice(chars),'-')[example[i]=='-'] for i in range(len(example))]
    return ''.join(ranstr)
print(guid())
def guid():
    import random,string
    format = [8, 4, 4, 4, 12]
    chars = ''.join(i for i in shuffle(string.ascii_uppercase + string.digits+string.ascii_lowercase))
    ranstr = [(random.choice(chars),'-')[any(i==j for j in [sum(format[:1+k])+k for k in range(len(format))])] for i in range(sum(format)+4)]
    return ''.join(ranstr)  
print(guid())
def guid():
    import random,string
    format = [8, 4, 4, 4, 12]
    chars = ''.join(i for i in shuffle(string.ascii_uppercase + string.digits+string.ascii_lowercase))
    ranstr = [random.choice(chars) for i in range(sum(format))]
    [ranstr.insert(i+sum(format[:i+1]),'-') for i,j in enumerate(format[:-1])]
    return ''.join(ranstr)  
print(guid())
def guid(format:tuple = [8, 4, 4, 4, 12],sep:str='-',copy:bool=False) -> str:
    """
    Generate a GUID for different resources
    Dependencies: random,string,m3ta.shuffle
    In: format{length of the intervals of the guid you want}
    Out: str
    """
    import random,string
    import pyperclip
    chars = ''.join(i for i in shuffle(string.ascii_uppercase + string.digits+string.ascii_lowercase) if i!=sep)
    ranstr = [random.choice(chars) for i in range(sum(format))]
    [ranstr.insert(i+sum(format[:i+1]),sep) for i,j in enumerate(format[:-1])]
    pyperclip.copy(''.join(ranstr)) if copy else None
    return ''.join(ranstr)
t = guid(sep='')
print(t,len(t))
# help(guid)

print('\n10010101001\n')

# print(str(uuid.uuid3()))
