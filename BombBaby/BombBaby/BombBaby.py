
def answer(M,F):
    count = 0
    M = int(M)
    F = int(F)

    while M != 0 and F != 0:

        if M == 1 or F == 1:
            if M == 1 and F == 1:
                return str(count)
            if M > F:
                return str(count + M - 1)
            else:
                return str(count + F - 1)

        if M is F:
            return "impossible"

        if M > F:
            if M > 100*F:
                count += M//F
                M = M - F*(M//F)
            else:
                M -= F
                count += 1
        else:
            if F > 100*M:
                count += F//M
                F = F - M*(F//M)
            else:
                F -= M
                count +=1

    if (M == 0 or F == 0) and (M == 1 or F == 1):
        return str(count)
    return "impossible"

print(answer("4", "7"))
#4
print(answer("2", "4"))
# impossible
print(answer("2", "1"))
#1
print(answer("1", "10"))
#9
print(answer("1", "1"))
#0

print(answer("19999999", "19"))