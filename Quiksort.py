# Mengambil input dari pengguna
numbers = []
nilai = int(input("Masukan Nilai:"))
for i in range (1,nilai):
    inp = int(input("Masukan Nilai Ke:"))
    numbers.append(inp)

def quicksort(angka):
    if len(angka) <= 1:
        return angka
    else:
        #pilih element pertama
        pivot = angka[0]
        less = [x for x in angka[1:] if x <= pivot]
        greater = [x for x in angka[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print('sebelum',numbers)
#Memproses QuickSort
sorted_numbers = quicksort(numbers)
#Menampilkan hasil pengurutan
print("sesudah", sorted_numbers)