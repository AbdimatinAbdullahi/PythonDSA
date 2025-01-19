class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.rear = None # Rear or mwisho wa Queue
        self.front = None # Front or mbele wa Queue =>  the one that gets out first 
    
    def is_Empty(self):
        return self.front is None
    
    def enqueue(self, val):
        newNode = Node(val)

        if self.is_Empty():
            self.front = self.rear = newNode
        
        self.rear.next = newNode
        self.rear = newNode
    
    def dequeue(self):
        if self.is_Empty():
            return None
        deque_data = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return deque_data
    
    def display(self):
        currentNode = self.front

        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
        


que = Queue()
print(que.is_Empty())
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.dequeue()
que.display()
