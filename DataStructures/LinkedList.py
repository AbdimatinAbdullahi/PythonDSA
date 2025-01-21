class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head is None
    
    def insertAtBegining(self, value):
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
    
    def display(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
    

linkedlist = LinkedList()

linkedlist.insertAtBegining(10)
linkedlist.insertAtBegining(20)
linkedlist.insertAtBegining(30)
linkedlist.display()
