from collections import deque

# -----------------------------
# Graph Representation
# -----------------------------

# Adjacency List (for BFS)
graph_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

# Adjacency Matrix (for DFS)
nodes = ['A', 'B', 'C', 'D', 'E']
graph_matrix = [
    # A  B  C  D  E
    [0, 1, 1, 0, 0],  # A
    [1, 0, 0, 1, 0],  # B
    [1, 0, 0, 0, 1],  # C
    [0, 1, 0, 0, 0],  # D
    [0, 0, 1, 0, 0]   # E
]

# -----------------------------
# BFS using Adjacency List
# -----------------------------
def bfs(start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Add neighbors
            for neighbor in graph_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

# -----------------------------
# DFS using Adjacency Matrix
# -----------------------------
def dfs(start_index, visited=None):
    if visited is None:
        visited = set()
    node = nodes[start_index]
    visited.add(node)
    print(node, end=" ")

    for i, connected in enumerate(graph_matrix[start_index]):
        if connected == 1 and nodes[i] not in visited:
            dfs(i, visited)

# -----------------------------
# Main Program
# -----------------------------
print("BFS Traversal (Adjacency List) starting from A:")
print(" -> ".join(bfs('A')))

print("\nDFS Traversal (Adjacency Matrix) starting from A:")
dfs(0)  # Start from index 0 (which is 'A')
