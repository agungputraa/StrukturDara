def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def recsearch(arr,x,cur_idx):
    if cur_idx == -1:
        return -1
    if arr[cur_idx] == x:
        return cur_idx
    return recsearch(arr,x,cur_idx-1)

arr = [1,2,3,4,5,6,7,8,9,0]
x = 5

print(recsearch(arr,x,len(arr)-1))

# print(search(arr,x))