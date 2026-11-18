
# GRAPH: MIRAMBEL

# Create the graph
graph = {
    "M1": ["I", "R"],
    "I": ["M1", "A", "M2"],
    "R": ["M1", "B", "E"],
    "A": ["I", "L"],
    "M2": ["I", "B"],
    "B": ["M2", "R"],
    "E": ["R", "L"],
    "L": ["A", "E"]
}

# Breadth First Search
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.append(vertex)

            for neighbor in sorted(graph[vertex]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    return visited

# Depth First Search
def dfs(graph, start):
    visited = []

    def visit(vertex):
        if vertex not in visited:
            visited.append(vertex)

            for neighbor in sorted(graph[vertex]):
                visit(neighbor)

    visit(start)
    return visited

# Display the results
print("GRAPH: MIRAMBEL")

print("\nAdjacency List:")
for vertex in sorted(graph):
    print(vertex, ":", sorted(graph[vertex]))

print("\nBFS Traversal:")
print(" -> ".join(bfs(graph, "M1")))

print("\nDFS Traversal:")
print(" -> ".join(dfs(graph, "M1")))
