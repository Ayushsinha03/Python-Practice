l = [45,85,75,95,67,-25,34,69,79,-12]
def Quick_sort(l):
    if len(l)<1:
        return l
    pivot = l[0]
    left = [ele for ele in l[1:] if ele<pivot]
    right = [ele for ele in l[1:] if ele>=pivot]
    return Quick_sort(left)+[pivot]+Quick_sort(right)
print(Quick_sort(l))
            
