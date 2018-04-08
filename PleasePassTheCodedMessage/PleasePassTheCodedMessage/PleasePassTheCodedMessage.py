import itertools

def answer(l):
    num = ""
    count = 0
    l.sort(reverse = True)
    for i in range(len(l), 0, -1):
        for subset in itertools.combinations(l,i):
            for j in range(0,i):
                count += subset[j]
            if(count%3 == 0):
                for k in range(0,i):
                    num+=(str(subset[k]))
                return int(num)
            count = 0
    return 0

l = [3,1,4,1]
print(answer(l))
# answer = 4311
l = [3,1,4,1,5,9]
print(answer(l))
# answer = 4322
l = [4,7]
print(answer(l))
# answer = 0