def answer(l):
    # Most extrem case: l = [1 for i in range(1,2000)]

    n = len(l)

    # First step: extract lucky doubles
    lucky_doubles_next = []  # Were to go from there
    lucky_doubles_count = {}  # Keep count of original
    # o(n*n) ~= 4000000 (still good)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if l[j] % l[i] == 0:  # Lucky double found !
                lucky_doubles_next.append(j)
                lucky_doubles_count[i] = lucky_doubles_count.get(i, 0) + 1  # Counting how many double there is for the current id

    # Early exit
    #n_doubles = len(lucky_doubles_next)
    #if n_doubles < 2:  # Not enough tuples
    #    return 0

    # Then, combine lucky doubles together
    glob_sum = 0
    for v in lucky_doubles_next:  # Linear time :)
        glob_sum += lucky_doubles_count.get(v, 0)

    return glob_sum

l = [1, 1, 1]
print(answer(l))
#1
l = [1, 1, 1, 1]
print(answer(l))
l = [1, 2, 3, 4, 5, 6]
print(answer(l))
#3
l = [1 for n in range(2000)]
print(answer(l))





#import itertools

#def answer(l):
#    print("in")
#    tupleList = []
#    count = 0

#    for subset in itertools.combinations(l,3):
#        if((subset[0] <= subset[1] <= subset[2]) and (subset[2]%subset[1] == 0 and subset[1]%subset[0] == 0) and not (subset in tupleList)):
#            tupleList.append(subset)
#            #print(subset)
#            count +=1
#    return count