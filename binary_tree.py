
# BINARY TREE: MIRAMBEL

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create Binary Tree
root = Node("M")

root.left = Node("I")
root.right = Node("R")

root.left.left = Node("A")
root.left.right = Node("M")

root.right.left = Node("B")
root.right.right = Node("E")

root.left.left.left = Node("L")

# BFS Traversal
def bfs(root):
    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result

# DFS Preorder Traversal
def dfs(root):
    result = []

    def preorder(node):
        if node is None:
            return

        result.append(node.data)
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return result

# Display Results
print("BINARY TREE: MIRAMBEL")
print("BFS:", " -> ".join(bfs(root)))
print("DFS:", " -> ".join(dfs(root)))
