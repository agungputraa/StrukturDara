class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.first is None:
            print("Queue is empty.")
        else:
            data = self.first.data
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
                self.first.prev = None
            self.size -= 1
            return data

    def first_element(self):
        if self.first is None:
            print("Queue is empty.")
        else:
            return self.first.data

    def last_element(self):
        if self.last is None:
            print("Queue is empty.")
        else:
            return self.last.data

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def print_queue(self):
        if self.first is None:
            print("Queue is empty.")
        else:
            current = self.first
            while current:
                print(current.data, end=" ")
                current = current.next
            print()


def menu():
    queue = Queue()
    while True:
        print("\nQueue Double Linked List Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. First")
        print("4. Last")
        print("5. Size")
        print("6. Is Empty")
        print("7. Print Queue")
        print("8. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter the data to enqueue: ")
            queue.enqueue(data)
            print("Enqueued", data)
        elif choice == 2:
            data = queue.dequeue()
            if data is not None:
                print("Dequeued", data)
        elif choice == 3:
            first = queue.first_element()
            if first is not None:
                print("First element:", first)
        elif choice == 4:
            last = queue.last_element()
            if last is not None:
                print("Last element:", last)
        elif choice == 5:
            size = queue.get_size()
            print("Queue size:", size)
        elif choice == 6:
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == 7:
            print("Queue elements:")
            queue.print_queue()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please enter a valid option.")


menu()