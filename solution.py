from heapq import heappush, heappop

goal = [[1,2,3],[8,0,4],[7,6,5]]

def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            dist += abs(x - i) + abs(y - j)
    return dist

def get_neighbors(state):
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def astar(start):
    visited = set()
    heap = []
    heappush(heap, (manhattan(start), 0, start, []))

    while heap:
        f, g, state, path = heappop(heap)

        if state == goal:
            return path + [state]

        visited.add(str(state))

        for neighbor in get_neighbors(state):
            if str(neighbor) not in visited:
                heappush(heap, (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [state]))

    return None

start = [[2,8,3],[1,6,4],[7,0,5]]

solution = astar(start)

for step in solution:
    for row in step:
        print(row)
    print("------")