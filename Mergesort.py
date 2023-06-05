angka =[]
nilai = int(input("Masukan Nilai:"))
for i in range (1,nilai):
    inp = int(input("Masukan Nilai Ke:"))
    angka.append(inp)

def mergesort(angka):
    jumlah = len(angka)
    if jumlah > 1 :
        posisi_tengah = jumlah//2
        potong_kiri = angka[:posisi_tengah]
        potong_kanan = angka[posisi_tengah:]
        mergesort(potong_kiri)
        mergesort(potong_kanan)
        jumlah_kiri = len(potong_kiri)
        jumlah_kanan = len(potong_kanan)
        c_all,c_kiri,c_kanan = 0,0,0
        while c_kiri < jumlah_kiri or c_kanan < jumlah_kanan:
            #element di potong kiri habis
            if c_kiri == jumlah_kiri:
                angka [c_all] = potong_kanan[c_kanan]
                c_kanan = c_kanan+1
            #element di potongan kanan habis
            elif c_kanan == jumlah_kanan:
                angka[c_all] = potong_kiri[c_kiri]
                c_kiri = c_kiri+1
            elif potong_kiri[c_kiri]<= potong_kanan[c_kanan]:
                angka[c_all] = potong_kiri[c_kiri]
                c_kiri = c_kiri+1
            else:
                angka[c_all] = potong_kanan[c_kanan]
                c_kanan = c_kanan+1
            c_all = c_all+1


print('sebelum',angka)
mergesort(angka)
print('sesudah',angka)