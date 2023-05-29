def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
arr=[]
nilai = int(input("Masukan Nilai:"))
for i in range (1,nilai):
    inp = int(input("Masukan Nilai Ke:"))
    arr.append(inp)
bubbleSort(arr)
print(arr)