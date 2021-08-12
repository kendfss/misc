def empty(filename):
    """
    Check if a given file is empty or not
    """
    with open(filename,'rb') as f:
        return False if len(f.readlines())>0 else True

if __name__ == "__main__":
    f = r'e:\projects\monties\2020\fileManagement\knownExtensions.pkl'
    print(empty(f))