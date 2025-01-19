class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
    
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.isEmpty():
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.value
    
    def Peek(self):
        return self.head.value
    

    # Lets print the entire items in stack
    def printStack(self):
        if self.isEmpty():
            print("Stack is Empty")
        
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next

stack = Stack()
stack.push(00)
stack.push(10)
stack.push(20)
print(stack.isEmpty())
stack.printStack()