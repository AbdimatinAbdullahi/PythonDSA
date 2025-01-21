class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def insert_at_the_begining(self, value):
        newNode = Node(value)

        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insert_at_end(self, value):
        newNode = Node(value)

        if self.isEmpty():
            self.head = newNode
        
        last = self.head

        while last.next:
            last = last.next
        last.next = newNode

    def delete_from_end(self):
        if self.isEmpty():
            print("Nothing to print")
            return

        secondLast = self.head

        while secondLast.next.next:
            secondLast = secondLast.next
        secondLast.next = None
    
    def delete_from_start(self):
        if self.isEmpty():
            print("LinkedList is empty")
            return
        
        if self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next
    
    def size(self):
        if self.isEmpty():
            print("LinkedList is Empty")
            return 0 

        len = 0
        currentNode = self.head

        while currentNode:
            len = len + 1
            currentNode = currentNode.next
        
        return len
        
    
    def delete_at(self, index):
        if self.isEmpty():
            print("Nothing to delete: List is Empty")
            return

        #  Providing index that is less that one or greater than len of linked list
        if index < 0 and index >= self.size():
            print("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        prevNde = self.head
        curIndex = 0

        while curIndex < index - 1:
            prevNde = prevNde.next
            curIndex += 1
        prevNde.next = prevNde.next.next
    
    def inserted_at(self, value, index):
        if index < 0 or index > self.size():
            print(f"Invalid Index: the length of linked list is: {self.size()}")
            return

        newNode = Node(value)

        if index == 0 and self.head is None:
            self.head = newNode
        
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        prevNode = self.head
        currIndex = 0

        while currIndex < index - 1:
            currIndex += 1
            prevNode = prevNode.next
        
        newNode.next = prevNode.next
        prevNode.next = newNode


    def display(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
    

linkedlist = LinkedList()

linkedlist.insert_at_the_begining(10)
linkedlist.insert_at_the_begining(20)
linkedlist.insert_at_the_begining(30)
linkedlist.insert_at_end(40)
linkedlist.inserted_at(50, 4)
linkedlist.inserted_at(60, 4)
linkedlist.inserted_at(70, 6)
print(linkedlist.size())
linkedlist.display()
