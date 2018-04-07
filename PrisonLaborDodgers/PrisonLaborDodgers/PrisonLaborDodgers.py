def answer(x,y):
    if(len(x) > len(y)):
        return(list(set(x) - set(y))[0])
    else:
        return(list(set(y) - set(x))[0])

# Test cases

x = [13,5,6,2,5]
y = [5,2,5,13]
print(answer(x,y))
# answer = 6

x = [14,27,1,4,2,50,3,1]
y = [2,4,-4,3,1,1,14,27,50]
print(answer(x,y))
# answer = -4
