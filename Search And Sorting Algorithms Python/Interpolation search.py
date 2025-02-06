l = [12,23,34,45,56,67,78,89,99,109,125]
def Interpolation_search(l):
    user = 56
    low = 0
    high = len(l)-1
    while low<=high:
        mid = int(low+((user-l[low])*(high-low))//(l[high]-l[low]))
        if l[mid]>user:
            high = mid-1
        elif l[mid]<user:
            low = mid+1
        elif l[mid]==user:
            return mid
    return -1
print(Interpolation_search(l))
