class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left  = None

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive(self.root, value)
    
    def insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.insert_recursive(current.left, value)
        
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self.insert_recursive(current.right, value)
        else:
            print("The value exist already in the tree")
    
    
    
    # Inorder Traversal: left -> root -> right 
    def in_order_traversal(self):
        return self.in_order_recursive(self.root, result=[])

    def in_order_recursive(self, root, result=[]):
        if root:
            self.in_order_recursive(root.left, result)
            result.append(root.value)
            self.in_order_recursive(root.right, result)
        return result
    
    
    
    # Pre order Traversal: root -> left -> right
    def pre_order(self):
        return self.pre_order_recursive(self.root, results =[])
    
    def pre_order_recursive(self, root, results=[]):
        if root:
            results.append(root.value)
            self.pre_order_recursive(root.left, results)
            self.pre_order_recursive(root.right, results)
        return results
    
    
    
    # Post Order Traversal: left -> right -> root
    def post_order(self):
        return self.post_order_recursive(self.root, results =[])
    
    def post_order_recursive(self, root, results=[]):
        if root:
            self.post_order_recursive(root.left, results)
            self.post_order_recursive(root.right, results)
            results.append(root.value)
        return results
    


    def search(self, value):
        if self.root.value == value:
            return True
        else:
            return self.search_recursive(self.root, value)
    
    def search_recursive(self, currentNode, value):
        if currentNode is None:
            return False
        elif currentNode.value == value:
            return True
        elif currentNode.value < value:
            return self.search_recursive(currentNode.right, value)
        else :
            return self.search_recursive(currentNode.left, value)









tr = Tree()
tr.insert(2)
tr.insert(1)
tr.insert(0)
tr.insert(4)
tr.insert(5)
tr.insert(1.5)
print(tr.in_order_traversal())
print(tr.pre_order())
print(tr.post_order())
print(tr.search(-1))