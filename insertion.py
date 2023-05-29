def insertionSort(arr):
    for i in range (1,len(arr)):
        key = arr[i]
        j= i-1
        while j >= 0 and key.lower() < arr[j].lower():
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
arr=[]
nilai = int(input("Masukan Nilai:"))
for i in range (1,nilai+1):
    inp = str(input("Masukan Nilai Ke:"))
    arr.append(inp)
insertionSort(arr)
print(arr)