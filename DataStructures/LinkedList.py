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
    
    def delete_at(self, index):
        prevNde = self.head
        curIndex = 0

        while curIndex < index - 1:
            prevNde = prevNde.next
            curIndex = curIndex + 1
        prevNde.next = prevNde.next.next

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
linkedlist.delete_from_end()
linkedlist.delete_from_start()
linkedlist.display()
