# Maze Graph Algorithms

## Team Members

- Paul Moses
- Sahan
- Canistan

## Division of Work

### Paul Moses
- Maze parsing
- Graph representation
- BFS shortest path

### Sahan
- Dijkstra minimum-cost path
- Movement mode comparison

### Canistan
- Maximum flow (Edmonds-Karp)
- Minimum spanning tree (Prim)

## Graph Representation

Each non-wall cell is represented as a graph vertex.

Edges connect neighboring cells according to the selected movement mode.

Wall cells (X) are excluded from the graph.

## Subtask A

### Algorithm
Breadth First Search (BFS)

### Time Complexity
O(V + E)

### Space Complexity
O(V)

## Subtask B

### Algorithm
Dijkstra's Algorithm

### Cost Model

cost(u,v) = value(v)

### Time Complexity
O((V + E) log V)

### Space Complexity
O(V)

## Subtask C

Both 4-directional and 8-directional movement were tested.

Allowing diagonal movement reduced both path length and path cost.

The shortest path and minimum-cost path were different.

## Subtask D

### Algorithm
Edmonds-Karp Maximum Flow

### Source
G

### Sink
S

### Time Complexity
O(VE²)

### Space Complexity
O(V + E)

## Subtask E

### Algorithm
Prim Minimum Spanning Tree

### Edge Weight

weight(u,v) = value(u) + value(v)

### Time Complexity
O(E log V)

### Space Complexity
O(V + E)

## Results

- Minimum Moves: 18
- Minimum Cost: 26
- Maximum Flow: 1
- MST Total Weight: 390

## AI Usage Disclosure

ChatGPT was used for guidance, debugging assistance, algorithm explanations, and documentation preparation.

All submitted code was reviewed and executed by team members.