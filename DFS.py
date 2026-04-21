# Packet Routing using DFS

def dfs(graph, current, destination, visited, path):
    visited.add(current)
    path.append(current)

    # If destination is reached
    if current == destination:
        return True

    # Visit all neighbors
    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, destination, visited, path):
                return True

    # Backtrack if not found
    path.pop()
    return False


# Graph (Network Topology)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Input
source = 'A'
destination = 'F'

# 🔹 Print Graph
print("Network Graph (Adjacency List):")
for node in graph:
    print(f"{node} -> {', '.join(graph[node]) if graph[node] else 'No connections'}")

# 🔹 Print Source & Destination
print("\nSource Node:", source)
print("Destination Node:", destination)

visited = set()
path = []

# DFS Call
if dfs(graph, source, destination, visited, path):
    print("\nPacket routed successfully!")
    print("Path taken:", " -> ".join(path))
else:
    print("\nNo path found between source and destination.")
