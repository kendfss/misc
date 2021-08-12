def firstShared(story,elementsToCheck,n=2):
    overlap = set(i for i in elementsToCheck if i in story)
    firstn = sorted(overlap,key=elementsToCheck.index)[:n]
    indices = [story.index(i) for i in firstn]
    return(indices)
    
    
if __name__ == '__main__':
    n = 2
    story = ['a', 'b', 'c', 'd', 'b', 'c', 'c']
    elementsToCheck = ['a', 'c', 'f', 'h']
    # elementsToCheck = ['a', 'b', 'c', 'd', 'f', 'h']
    for i in range(4):
        print(firstShared(story,elementsToCheck,i))
    # []
    # [0]
    # [0, 2]
    # [0, 2]