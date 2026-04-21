from collections import deque

def bfs(graph, source, destination):
    visited = set()
    queue = deque([[source]])   # queue stores paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        # If destination found
        if node == destination:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None


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

# BFS Call
path = bfs(graph, source, destination)

if path:
    print("\nPacket routed successfully using BFS!")
    print("Shortest Path:", " -> ".join(path))
else:
    print("\nNo path found between source and destination.")
