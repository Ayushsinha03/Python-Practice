l = [25,64,43,16,71,11,6]
def Insertion_sort(l):
    for ind in range(len(l)):
        h = ind
        val = l[h]
        while h>0 and val< l[h-1]:
            l[h] = l[h-1]
            h-=1
        l[h] = val
    return l
print(Insertion_sort(l))
