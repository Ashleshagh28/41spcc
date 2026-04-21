import heapq

# Goal State
goal_state = [[1,2,3],
              [4,5,6],
              [7,8,0]]

# Heuristic: Manhattan Distance
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Convert state to tuple
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate neighbors with moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dx, dy, move in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append((new_state, move))

    return neighbors

# A* Algorithm
def a_star(start):
    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start))

    came_from = {}
    move_taken = {}
    g_cost = {to_tuple(start): 0}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == goal_state:
            path = []
            moves = []

            while to_tuple(current) in came_from:
                path.append(current)
                moves.append(move_taken[to_tuple(current)])
                current = came_from[to_tuple(current)]

            path.append(start)
            path.reverse()
            moves.reverse()
            return path, moves

        for neighbor, move in get_neighbors(current):
            new_g = g + 1
            t_neighbor = to_tuple(neighbor)

            if t_neighbor not in g_cost or new_g < g_cost[t_neighbor]:
                g_cost[t_neighbor] = new_g
                f_cost = new_g + heuristic(neighbor)
                heapq.heappush(open_list, (f_cost, new_g, neighbor))
                came_from[t_neighbor] = current
                move_taken[t_neighbor] = move

    return None, None


# 🔹 Initial State (you can change this)
start_state = [[1,2,3],
               [4,0,6],
               [7,5,8]]

# 🔹 Print Initial State
print("Initial State:")
for row in start_state:
    print(" ".join(str(x) if x != 0 else "_" for x in row))

# 🔹 Print Goal State
print("\nGoal State:")
for row in goal_state:
    print(" ".join(str(x) if x != 0 else "_" for x in row))

# Solve
solution, moves = a_star(start_state)

# 🔹 Output (Step-by-step like your screenshot)
if solution:
    print("\nGoal Reached!\n")

    for i in range(len(solution)):
        if i == 0:
            print(f"Step {i} | Move: Start")
        else:
            print(f"Step {i} | Move: {moves[i-1]}")

        for row in solution[i]:
            print(" ".join(str(x) if x != 0 else "_" for x in row))

        print()
else:
    print("No solution found.")
