
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    while node.left:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None: return root.right
        if root.right is None: return root.left
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, val)

print("In-order Traversal:")
inorder(root)   

print("\nSearch 40:", "Found" if search(root, 40) else "Not Found")

root = delete(root, 50)
print("After deleting 50:")
inorder(root)   
