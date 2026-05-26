# Maze Graph Algorithms Report

## Team Members

- Thomas Aaran Paul Moses - 231ADB187
- Herath Mudiyanselage Sahan Kavinda Sepala - 231ADB248
- Yabesh Canistan Raj Kumar - 231ADB199

---

# Division of Work

### Thomas Aaran Paul Moses
- Maze file parsing
- Maze representation
- Graph construction
- Breadth First Search (BFS) implementation
- Project integration and testing

### Herath Mudiyanselage Sahan Kavinda Sepala
- Dijkstra minimum-cost path implementation
- Movement mode comparison
- Output generation
- Result verification

### Yabesh Canistan Raj Kumar
- Edmonds-Karp maximum flow implementation
- Prim minimum spanning tree implementation
- Complexity analysis
- Documentation support

All team members participated in testing, debugging, discussion, and validation of results.

---

# Maze Representation

The maze is read from a text file.

Each character represents one cell:

| Symbol | Meaning |
|----------|----------|
| S | Start cell |
| G | Goal cell |
| X | Wall |
| 0–9 | Passable cell with numeric value |

The maze is stored internally as a two-dimensional list.

Example coordinate format:

```text
(row,column)
```

Example:

```text
(0,0)
```

represents the top-left cell.

---

# Graph Representation

The maze is interpreted as a graph.

Vertices:

- Every non-wall cell

Edges:

- Connections between neighboring passable cells

Movement modes:

### 4-Directional

- Up
- Down
- Left
- Right

### 8-Directional

- Up
- Down
- Left
- Right
- Up-left
- Up-right
- Down-left
- Down-right

Wall cells are excluded from the graph.

---

# Subtask A – Shortest Path by Number of Moves

## Chosen Approach

Breadth First Search (BFS)

## Reason for Choice

Every legal move has equal cost.

BFS guarantees the shortest path in an unweighted graph because vertices are explored level by level.

## Output Result

Minimum Moves:

```text
18
```

Movement Mode:

```text
4-directional
```

## Time Complexity

```text
O(V + E)
```

## Space Complexity

```text
O(V)
```

Where:

- V = number of vertices
- E = number of edges

---

# Subtask B – Minimum Cost Path

## Chosen Approach

Dijkstra's Algorithm

## Cost Model

Entering Cost:

```text
cost(u,v) = value(v)
```

Special values:

```text
value(S)=0
value(G)=0
```

## Reason for Choice

The maze graph contains weighted edges.

Dijkstra's algorithm guarantees the minimum-cost path when all edge weights are non-negative.

## Output Result

Minimum Cost:

```text
26
```

Movement Mode:

```text
4-directional
```

## Time Complexity

```text
O((V + E) log V)
```

## Space Complexity

```text
O(V)
```

---

# Subtask C – Movement Mode Comparison

## Chosen Approach

Both BFS and Dijkstra were executed using:

- 4-directional movement
- 8-directional movement

## Results

### Shortest Path

| Movement Mode | Moves |
|---------------|--------|
| 4-directional | 18 |
| 8-directional | 11 |

### Minimum Cost

| Movement Mode | Cost |
|---------------|------|
| 4-directional | 26 |
| 8-directional | 18 |

## Discussion

Allowing diagonal movement significantly reduced the path length.

The shortest path decreased from 18 moves to 11 moves.

The minimum-cost path also improved from cost 26 to cost 18.

The path with the fewest moves is not always identical to the path with the lowest cost. A route may require additional moves but still have a lower total traversal cost if it passes through lower-value cells.

## Time Complexity

Same as BFS and Dijkstra:

```text
O(V + E)
O((V + E) log V)
```

## Space Complexity

```text
O(V)
```

---

# Subtask D – Maximum Flow from G to S

## Chosen Approach

Edmonds-Karp Algorithm

## Network Interpretation

Source:

```text
G
```

Sink:

```text
S
```

Vertices:

- All non-wall cells

Capacity Rule:

```text
capacity(u,v) = value(v)
```

Special Cases:

```text
capacity into S = 100
capacity into G = 100
```

## Reason for Choice

Edmonds-Karp is a BFS-based implementation of the Ford-Fulkerson method and guarantees the maximum flow in a directed network.

## Output Result

Maximum Flow:

```text
1
```

Movement Mode:

```text
4-directional
```

## Time Complexity

```text
O(VE²)
```

## Space Complexity

```text
O(V + E)
```

---

# Subtask E – Minimum Spanning Tree

## Chosen Approach

Prim's Algorithm

## Graph Interpretation

Vertices:

- All non-wall cells

Edge Weight Rule:

```text
weight(u,v)=value(u)+value(v)
```

## Reason for Choice

Prim's algorithm efficiently constructs a minimum spanning tree by repeatedly adding the minimum-weight edge that connects a new vertex.

Cycles are avoided because edges leading to already-visited vertices are ignored.

## Output Result

Total MST Weight:

```text
390
```

Vertices in Connected Component:

```text
76
```

Edges in Tree:

```text
75
```

Goal Reachable:

```text
True
```

## Time Complexity

```text
O(E log V)
```

## Space Complexity

```text
O(V + E)
```

---

# Discussion of Results

All required subtasks were successfully completed.

The maze was correctly represented as a graph and all graph algorithms produced valid results.

The shortest path contained 18 moves under 4-directional movement.

The minimum-cost path had total cost 26 using the entering-cost model.

Allowing diagonal movement improved both shortest-path length and minimum-cost values.

The maximum flow between G and S was limited to 1 due to low-capacity bottleneck regions within the maze.

The MST successfully connected all reachable vertices in the connected component containing S with total weight 390.

---

# Known Limitations

- Only Cost Model 1 (Entering Cost) is implemented.
- Flow and MST visualizations are not included.
- Output is generated as plain text rather than graphical form.

Despite these limitations, all required subtasks for a three-member team were successfully completed.

---

# AI Usage Disclosure

AI tools, including ChatGPT, were used for:

- Learning support
- Algorithm explanations
- Debugging assistance
- Code review assistance
- Documentation guidance
- Report preparation support

All submitted code was reviewed, tested, executed, and understood by the team members before submission.

---

# Conclusion

The project demonstrates how a maze can be interpreted as a graph and solved using classical graph algorithms.

Breadth First Search, Dijkstra's Algorithm, Edmonds-Karp Maximum Flow, and Prim's Minimum Spanning Tree were successfully applied to solve the required subtasks.

The implementation produced correct results for the required maze and supports both 4-directional and 8-directional movement modes.