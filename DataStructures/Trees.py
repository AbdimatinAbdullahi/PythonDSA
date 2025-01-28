class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node = Node(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self, root, value):
        if value < root.value:
            if root.left is None:
                root.left = node = Node(value)
            else:
                self.insert_recursive(root.left, value)

        elif value > root.value:
            if root.right is None:
                root.right = node = Node(value)
            else:
                self.insert_recursive(root.right, value)
        else:
            return "Value already exist in Tree"
    def Inorder(self):
        return self.inorder_recursive(self.root, result=[])
    

    def inorder_recursive(self, root, result):
        if root:
            self.inorder_recursive(root.left, result)
            result.append(root.value)
            self.inorder_recursive(root.right, result)
        return result


tr = Tree()
tr.insert(4)
tr.insert(1)
tr.insert(6)
tr.insert(2)
tr.insert(5)
tr.insert(0)
tr.insert(7)
print(tr.Inorder())