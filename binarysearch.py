def search(arr,x):
    low = 0
    mid = 0
    high = len(arr)-1
    while low <= high:
        mid = (high+low)//2
        if(arr[mid]<x):
            low = mid + 1
        elif (arr[mid]>x):
            high = mid-1
        else:
            return mid
    return -1

def recsearch (arr,low,high,x):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] ==x:
            return mid
        elif arr[mid]>x:
            return recsearch (arr,low,mid-1,x)
        else:
            return recsearch (arr,mid+1,high,x)
    else:
        return -1

nilai =int(input("Masukan Nilai Yang Ingin anda Cari:"))
arr = [1,2,3,4,5,6,7,8,9]
x= nilai

print (recsearch(arr,0,len(arr)-1,x))



