#preorder traversal of a binary tree full code
def preorder(root):
    if root:
        print(root.val, end = ' ')
        preorder(root.left)
        preorder(root.right)
#test the function
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)

root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Preorder traversal of binary tree is: ")
preorder(root)
print()
