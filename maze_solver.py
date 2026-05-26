from collections import deque
import heapq

# =====================================================
# Maze Graph Algorithms
#
# Team Members:
# - Paul Moses
# - Sahan
# - Canistan
# =====================================================


# =====================================================
# Load Maze
# =====================================================

def load_maze(filename):
    maze = []

    with open(filename, "r") as file:
        for line in file:
            maze.append(list(line.strip()))

    return maze


def find_start_goal(maze):
    start = None
    goal = None

    for r in range(len(maze)):
        for c in range(len(maze[0])):

            if maze[r][c] == "S":
                start = (r, c)

            elif maze[r][c] == "G":
                goal = (r, c)

    return start, goal


# =====================================================
# Neighbor Function
# =====================================================

def get_neighbors(maze, row, col, movement_mode="4"):

    if movement_mode == "4":
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
    else:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

    neighbors = []

    rows = len(maze)
    cols = len(maze[0])

    for dr, dc in directions:

        nr = row + dr
        nc = col + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if maze[nr][nc] != "X":
                neighbors.append((nr, nc))

    return neighbors


# =====================================================
# Cell Value
# =====================================================

def cell_value(cell):

    if cell in ("S", "G"):
        return 0

    return int(cell)


# =====================================================
# BFS Shortest Path
# =====================================================

def bfs_shortest_path(maze, start, goal, movement_mode="4"):

    queue = deque([start])

    visited = {start}

    parent = {}

    while queue:

        current = queue.popleft()

        if current == goal:
            break

        for neighbor in get_neighbors(
            maze,
            current[0],
            current[1],
            movement_mode
        ):

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    if goal not in visited:
        return None

    path = []

    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)

    path.reverse()

    return path


# =====================================================
# Dijkstra Minimum Cost
# =====================================================

def dijkstra_min_cost(maze, start, goal, movement_mode="4"):

    pq = [(0, start)]

    distances = {start: 0}

    parent = {}

    visited = set()

    while pq:

        current_cost, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        for neighbor in get_neighbors(
            maze,
            current[0],
            current[1],
            movement_mode
        ):

            nr, nc = neighbor

            move_cost = cell_value(maze[nr][nc])

            new_cost = current_cost + move_cost

            if neighbor not in distances or new_cost < distances[neighbor]:

                distances[neighbor] = new_cost

                parent[neighbor] = current

                heapq.heappush(
                    pq,
                    (new_cost, neighbor)
                )

    if goal not in distances:
        return None, None

    path = []

    current = goal

    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)

    path.reverse()

    return distances[goal], path


# =====================================================
# Flow Network
# =====================================================

def build_flow_network(maze, movement_mode="4"):

    graph = {}

    rows = len(maze)
    cols = len(maze[0])

    for r in range(rows):
        for c in range(cols):

            if maze[r][c] == "X":
                continue

            node = (r, c)

            graph[node] = {}

            for nr, nc in get_neighbors(
                maze,
                r,
                c,
                movement_mode
            ):

                value = maze[nr][nc]

                if value in ("S", "G"):
                    capacity = 100
                else:
                    capacity = int(value)

                graph[node][(nr, nc)] = capacity

    return graph


def bfs_flow(residual, source, sink, parent):

    visited = {source}

    queue = deque([source])

    while queue:

        u = queue.popleft()

        for v, capacity in residual[u].items():

            if v not in visited and capacity > 0:

                visited.add(v)

                parent[v] = u

                queue.append(v)

    return sink in visited


def edmonds_karp(graph, source, sink):

    residual = {}

    for u in graph:

        residual[u] = {}

        for v in graph[u]:
            residual[u][v] = graph[u][v]

    for u in graph:
        for v in graph[u]:

            if v not in residual:
                residual[v] = {}

            if u not in residual[v]:
                residual[v][u] = 0

    max_flow = 0

    positive_flow = []

    while True:

        parent = {}

        if not bfs_flow(
            residual,
            source,
            sink,
            parent
        ):
            break

        path_flow = float("inf")

        s = sink

        while s != source:

            path_flow = min(
                path_flow,
                residual[parent[s]][s]
            )

            s = parent[s]

        max_flow += path_flow

        v = sink

        while v != source:

            u = parent[v]

            residual[u][v] -= path_flow
            residual[v][u] += path_flow

            positive_flow.append(
                (u, v, path_flow)
            )

            v = parent[v]

    return max_flow, positive_flow


# =====================================================
# Weighted Graph For MST
# =====================================================

def build_weighted_graph(maze, movement_mode="4"):

    graph = {}

    rows = len(maze)
    cols = len(maze[0])

    for r in range(rows):
        for c in range(cols):

            if maze[r][c] == "X":
                continue

            node = (r, c)

            graph[node] = []

            for nr, nc in get_neighbors(
                maze,
                r,
                c,
                movement_mode
            ):

                weight = (
                    cell_value(maze[r][c])
                    + cell_value(maze[nr][nc])
                )

                graph[node].append(
                    ((nr, nc), weight)
                )

    return graph


# =====================================================
# Prim MST
# =====================================================

def prim_mst(graph, start):

    visited = set()

    mst_edges = []

    total_weight = 0

    pq = []

    visited.add(start)

    for neighbor, weight in graph[start]:
        heapq.heappush(
            pq,
            (weight, start, neighbor)
        )

    while pq:

        weight, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)

        mst_edges.append(
            (u, v, weight)
        )

        total_weight += weight

        for nxt, w in graph[v]:

            if nxt not in visited:

                heapq.heappush(
                    pq,
                    (w, v, nxt)
                )

    return total_weight, mst_edges, visited


# =====================================================
# MAIN
# =====================================================

maze = load_maze("maze_10x10_A.txt")

start, goal = find_start_goal(maze)

print("================================================")
print("Maze Graph Algorithms")
print("================================================")

print("\nStart:", start)
print("Goal:", goal)

# ---------- A ----------

path_a_4 = bfs_shortest_path(
    maze,
    start,
    goal,
    "4"
)

print("\n================================================")
print("SUBTASK A")
print("================================================")

print("Movement Mode: 4-directional")
print("Minimum Moves:", len(path_a_4) - 1)

# ---------- B ----------

cost_b_4, path_b_4 = dijkstra_min_cost(
    maze,
    start,
    goal,
    "4"
)

print("\n================================================")
print("SUBTASK B")
print("================================================")

print("Minimum Cost:", cost_b_4)

# ---------- C ----------

path_a_8 = bfs_shortest_path(
    maze,
    start,
    goal,
    "8"
)

cost_b_8, path_b_8 = dijkstra_min_cost(
    maze,
    start,
    goal,
    "8"
)

print("\n================================================")
print("SUBTASK C")
print("================================================")

print("4-direction shortest path:", len(path_a_4) - 1)
print("8-direction shortest path:", len(path_a_8) - 1)

print("4-direction minimum cost:", cost_b_4)
print("8-direction minimum cost:", cost_b_8)

# ---------- D ----------

graph = build_flow_network(
    maze,
    "4"
)

max_flow, positive_edges = edmonds_karp(
    graph,
    goal,
    start
)

print("\n================================================")
print("SUBTASK D")
print("================================================")

print("Maximum Flow:", max_flow)

# ---------- E ----------

weighted_graph = build_weighted_graph(
    maze,
    "4"
)

mst_weight, mst_edges, component = prim_mst(
    weighted_graph,
    start
)

print("\n================================================")
print("SUBTASK E")
print("================================================")

print("MST Total Weight:", mst_weight)
print("Vertices In Component:", len(component))
print("Edges In Tree:", len(mst_edges))
print("Goal Reachable:", goal in component)