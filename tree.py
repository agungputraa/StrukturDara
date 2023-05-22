class Node:
    def __init__(self,data) :
        self.left = None
        self.right = None
        self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()
tree = Node(2) #Root
tree.left = Node(3) #Child Root Kiri
tree.right = Node(4) #Child Root Kanan
tree.left.left = Node(5) #Child 3 Kiri
tree.left.right = Node(6) #Child 3 Kanan
tree.right.left = Node(7) #Child 4 Kiri
tree.right.right = Node(8) #Child 4 Kanan

tree.PrintTree()