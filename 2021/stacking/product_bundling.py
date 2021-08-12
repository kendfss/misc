"""
https://stackoverflow.com/questions/66295311/create-product-bundle-by-matching-user-input-to-product-features-recursively

"""


user_input=['a','b','c']

d1=['a','c','d']
d2=['a','b','e','f']
d3=['a','c','b','f']
d4=['b']
d5=['g','e','a']
d6=['g']

dlist=[d1,d2,d3,d4,d5,d6]
diff_match=[]
# find match n diff of each product based on user input
# for i in range(len(dlist)):
for i in dlist:
    match=set(user_input).intersection(set(i))
    #print("match is",match)
    diff=set(user_input).difference(set(i))
    #print("diff is",diff)
    temp={'match':match,'diff':diff}
    diff_match.append(temp)
    
for i in range(len(diff_match)):
    # if match is found, recommend the product alone
    diff_match_temp=diff_match[i]['match']
    print("diff match temp is",diff_match_temp)
    if diff_match_temp==user_input:
        print ("absolute match")
    #scenario where the user input is subset of product features, seperate from partial match
    elif (all(x in list(diff_match_temp) for x in list(user_input))):
        print("User input subset of product features")
        print("The parent list is",diff_match[i]['match'])
        print("the product is", dlist[i])
    else:
        '''else check if the difference between user input and the current product is fulfilled by other product, 
        if yes, these products are bundled together'''
        for j in range(len(diff_match)):
            temp_diff=diff_match[i]['diff']
            print("temp_diff is",temp_diff)
            # empty set should be explicitly checked to avoid wrong match
            if (temp_diff.intersection(diff_match[j]['match'])==temp_diff and len(temp_diff)!=0 and list(temp_diff) != user_input) :
            #if temp_diff==diff_match[j]['match'] and len(temp_diff)!=0 and list(temp_diff) != user_input :
                print("match found with another product")
                print("parent is",dlist[i])
                print("the combination is",dlist[j] )