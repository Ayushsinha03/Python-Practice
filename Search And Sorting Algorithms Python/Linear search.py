l = [12,52,85,96,78,26,37,78,65]
def linear_search(l):
    user = 78
    for ind in range(len(l)):
        if l[ind]==user:
            return ind
    return -1
print(linear_search(l))
