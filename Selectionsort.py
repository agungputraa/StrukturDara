def selectionsort(angka):
    for tujuan in range(len(angka)-1,0,-1):
        max=0
        for i in range(1,tujuan+1):
            max_temp = angka[max]
            if max_temp < angka[i]:
                max = i
        angka[max],angka[tujuan] = angka [tujuan],angka[max]
    return angka

angka =[]
nilai = int(input("Masukan Nilai:"))
for i in range (1,nilai):
    inp = int(input("Masukan Nilai Ke:"))
    angka.append(inp)
print('sebelum',angka)
selectionsort(angka)
print('sesudah',angka)
