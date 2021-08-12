"""
https://stackoverflow.com/questions/66192897/develop-a-module-to-help-generate-lottery-tickets-in-python
"""
import random, getopt, sys



def make_ticket(length, maximum):
    """
    Generate a ticket of a given length using numbers from [1, maximum]
    return random.sample(range(1, maximum+1), length) would be the best way
    """
    ticket = []
    while len(ticket) < length:
        num = random.randint(1, maximum+1)
        if not num in ticket:
            ticket.append(num)
    return ticket

def usage():
    print("lottohelper.py [-h|--help] [-v|--verbose] <0/1> [-t|--type] <649/MAX> <integer>")


def main(args):
    try:
        opts, args = getopt.getopt(args, "ht:v:", "help type= verbose=".split()) # students: complete this statement
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    
    # get optional arguments
    # this approach intentionally breaks if the user misses an option
    for k, v in opts:
        if k in '--help':
            usage()
        elif k in '--type':
            tp = {
                '649': (6, 49),
                'MAX': (7, 50)
            }[v] # ternary operator
        elif k in '--verbose':
            ver = {
                '0': False, 
                '1': True
            }[v] # ternary operator
    
    # get positional argument
    N = eval(args[0]) # causes an exception if anything other than an integer is given; a float will not be converted
    
    # do actual work here
    tickets = [make_ticket(*tp) for i in range(N)] # list comprehension
    
    if ver:
        print(f'Ticket Type:\t{649 if tp[0]==6 else "MAX"}') # format string
        
    for i, t in enumerate(tickets, 1):
        print(f'Ticket #{i}:\t{t}') #format string
        
    
if __name__=='__main__':
    args = sys.argv[1:]
    args = '-v 1 --t 649 3'.split()
    main(args)
    args = '--verbose 1 --type MAX 3'.split()
    main(args)