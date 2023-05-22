class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def isEmpty(self):
        return self.head is None
            
    def first_element(self):
        if self.head is None:
            print("Antrian kosong.")
        else:
            return self.head.data

    def last_element(self):
        if self.tail is None:
            print("Antrian kosong.")
        else:
            return self.tail.data
        
    def remove(self):
        if self.isEmpty():
            return None
        else:
            removed_node = self.head
            if self.head is self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return removed_node.data
    #menghitung panjang queue
    def qsize(self):
        return self.size
  
    def print(self):
        if self.head is None:
            print("Antrian kosong.")
        else:
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
            print()
   
            #menu
    def menu(self):
        queue = Queue()
        pilih = 'y'
        while pilih == 'y':
            print("1. Menambah Elemen")
            print("2. Mengeluarkan Elemen")
            print("3. Antrian Pertama")
            print("4. Antrian Terakhir")
            print("5. Size queue")
            print("6. Cek Kosong")
            print("7. Tampilkan Queue")
            
            pilihan = str(input("Pilih Menu: "))
            if pilihan == "1":
                obj = str(input("Masukan Data: "))
                self.add(obj)
                print("elemen"+obj+"sudah di tambahkan")
            elif pilihan == "2":
                obj = self.remove()
                if obj != "empty":
                    print("elemen "+obj+" Sudah di hapus")
                else:
                    print("Queue Kosong")
            elif pilihan == "3":
                first = self.first_element()
                if first is not None:
                    print("Antrian pertama:", first)
            elif pilihan == "4":
                last = self.last_element()
                if last is not None:
                    print("Antrian terakhir:", last)
            elif pilihan == "5":
                ukuran = queue.qsize()
                print("ukuran queue",ukuran)
            elif pilihan == "6":
                print(self.isEmpty())
            elif pilihan == "7":
                print(self.print())
            else:
                pilih = 'n'
if __name__ == "__main__":
    q = Queue()
    q.menu()