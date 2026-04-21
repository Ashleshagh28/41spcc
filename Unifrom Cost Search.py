import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, node, path)
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        # Goal check
        if node == goal:
            return cost, path

        # Explore neighbors
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return float("inf"), []


# Graph (with costs)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

start = 'A'
goal = 'F'

# 🔹 Print Graph
print("Graph (Node -> (Neighbor, Cost)):")
for node in graph:
    print(f"{node} -> {graph[node]}")

# 🔹 Print Start & Goal
print("\nStart Node:", start)
print("Goal Node:", goal)

# UCS Call
cost, path = uniform_cost_search(graph, start, goal)

# Output
if path:
    print("\nOptimal path found using UCS!")
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("\nNo path found.")
