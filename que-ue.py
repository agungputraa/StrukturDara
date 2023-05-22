import queue
class myQ:
    def __init__(self):
        self.item = queue.Queue()
    #Memeriksa queue
    def isEmpty(self):
        return self.item.empty()
    #menambah element queue
    def qPut(self,item):
        self.item.put(item)
    #mengeluarkan element pada queue
    def qGet(self):
        if not self.item.empty():
            return self.item.get()
        else:
            return "empty"
    #menghitung panjang queue
    def size (self):
        return self.item.qsize()
    #print queue
    def print(self):
        return self.item.queue
    #menu
    def menu(self):
        pilih = 'y'
        while pilih == 'y':
            print("1. Menambah Elemen")
            print("2. Mengeluarkan Elemen")
            print("3. Ukuran Queue")
            print("4. Cek Kosong")
            print("5. Print Queue")
            pilihan = str(input("Pilih Menu: "))
            if pilihan == "1":
                obj = str(input("Masukan Data: "))
                self.qPut(obj)
                print("elemen"+obj+"sudah di tambahkan")
            elif pilihan == "2":
                obj = self.qGet()
                if obj != "empty":
                    print("elemen"+obj+"Sudah di hapus")
                else:
                    print("Queue Kosong")
            elif pilihan == "3":
                print("ukuran queue"+str(self.size()))
            elif pilihan == "4":
                print(self.isEmpty())
            elif pilihan == "5":
                print(self.print())
            else:
                pilih = 'n'
if __name__ == "__main__":
    q = myQ()
    q.menu()