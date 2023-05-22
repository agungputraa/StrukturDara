#class node
class Node(object):
    #inisialisasi node
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleList(object):
    head = None
    tail = None
    
    #menambahkan data
    def menuTambah(self):
        inp = int(input('Masukkan Data : '))
        new_node = Node(inp,None,None)
        #memeriksa apakah list kosong
        if self.head is None:
            #menunjuk head dan tail ke node baru
            self.head = self.tail = new_node
        #ketika list tidak kosong
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        
    #menghapus node
    def menuHapus(self):
        inp = int(input('Masukkan data yang ingin dihapus : '))
        #pointer untuk menunjuk node pertama
        current_node = self.head
        #lakukan perulangan sebanyak node
        while current_node is not None:
            #memeriksa apakah data tersebut yang ingin dihapus
            if current_node.data == inp:
                #cek apakah data berada di elemen node terakhir
                if current_node.next is None:
                    current_node.prev.next = None
                #jika node yang dicari bukan di elemen node pertama
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                #jika node berada di elemen pertama
                else:
                    self.head = current_node.next #memindahkan head ke elemen berikutnya
                    current_node.next.prev = None #menunjuk head prev menjadi none
                    
            #mimindahkan pointer menuju ke node berikutnya
            current_node = current_node.next
    
    #menu melihat isi list
    def menuTampil(self):
        print('List data : ')
        #membuat pointer untuk menunjuk ke node pertama
        current_node = self.head
        #perulangan menampilkan data berserta data sebelum dan setelahnya
        while current_node is not None:
            print(current_node.prev.data) if hasattr(current_node.prev,"data") else None
            print(current_node.data)
            print(current_node.next.data) if hasattr(current_node.next,"data") else None
            #menunjuk ke node berikutnya
            current_node = current_node.next
    
    #Delete All       
    def deleteAll(self):
        current = self.head
        if current is None:
            print("No Data")
        while current:
            self.head = current.next
            current = None
            current = self.head
    
    def menuUmum(self):
        pilih = "y"
        while ((pilih == "y") or (pilih == "Y")):
            print('Pilih menu : ')
            print('1. Tambah data')
            print('2. Hapus data')
            print('3. Tampil data')
            print('4. Delete All data')
            pilihan = str(input('Masukkan pilihan : '))
            if(pilihan == "1"):
                self.menuTambah()
            elif(pilihan == "2"):
                self.menuHapus()
            elif(pilihan == "3"):
                self.menuTampil()
            elif(pilihan == "4"):
                self.deleteAll()
            else:
                pilih = "n"

if __name__ == "__main__":
    dl = DoubleList()
    dl.menuUmum()