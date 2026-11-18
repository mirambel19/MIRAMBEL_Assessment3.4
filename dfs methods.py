class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Preorder: Root, Left, Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder: Left, Root, Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Postorder: Left, Right, Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create Binary Tree
root = Node("M")
root.left = Node("I")
root.right = Node("R")

root.left.left = Node("A")
root.left.right = Node("M")

root.right.left = Node("B")
root.right.right = Node("E")

root.right.left.left = Node("L")


# Display DFS Traversals
print("PREORDER:")
preorder(root)

print("\n\nINORDER:")
inorder(root)

print("\n\nPOSTORDER:")
postorder(root)

print()
