l = [12,23,34,45,56,67,78,89,99,109,125]
def Binary_search(l):
    user = 99
    low = 0
    high = len(l)-1
    while low<=high:
        mid = (low+high)//2
        if l[mid]>user:
            high = mid-1
        elif l[mid]<user:
            low = mid+1
        elif l[mid]==user:
            return mid
    return -1
print(Binary_search(l))
