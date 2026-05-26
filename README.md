# Maze Graph Algorithms

Final Group Project for Graph Algorithms demonstrating graph-based problem solving using maze environments represented as graphs.

---

# Team Members

- Thomas Aaran Paul Moses - 231ADB187
- Herath Mudiyanselage Sahan Kavinda Sepala - 231ADB248
- Yabesh Canistan Raj Kumar - 231ADB199

---

# Project Overview

This project models a maze as a graph and applies classical graph algorithms to solve several graph-related problems.

Each non-wall maze cell is treated as a graph vertex and edges are created between neighboring cells according to the selected movement mode.

Implemented algorithms:

1. Breadth First Search (BFS)
2. Dijkstra's Shortest Path Algorithm
3. Edmonds-Karp Maximum Flow Algorithm
4. Prim's Minimum Spanning Tree Algorithm

Supported movement modes:

- 4-directional movement
  - Up
  - Down
  - Left
  - Right

- 8-directional movement
  - Up
  - Down
  - Left
  - Right
  - Up-Left
  - Up-Right
  - Down-Left
  - Down-Right

---

# Repository Structure

```text
maze-graph-algorithms
│
├── maze_solver.py
├── maze_10x10_A.txt
├── output.txt
├── report.md
└── README.md
```

---

# Implemented Subtasks

## Subtask A – Shortest Path by Number of Moves

Algorithm Used:

- Breadth First Search (BFS)

Objective:

- Find a path from S to G using the minimum possible number of moves.

Output:

- Minimum number of moves
- Path from S to G
- Movement mode used

---

## Subtask B – Minimum Cost Path

Algorithm Used:

- Dijkstra's Algorithm

Cost Model:

```text
cost(u,v) = value(v)
```

(Entering Cost Model)

Objective:

- Find the path from S to G with the minimum total traversal cost.

Output:

- Minimum total cost
- Path from S to G
- Cost model used
- Movement mode used

---

## Subtask C – Movement Mode Comparison

Comparison Between:

- 4-directional movement
- 8-directional movement

Objective:

- Compare shortest-path and minimum-cost results under different movement rules.

Discussion Includes:

- Effect of diagonal movement on shortest paths
- Effect of diagonal movement on minimum-cost paths
- Difference between shortest paths and cheapest paths

---

## Subtask D – Maximum Flow

Algorithm Used:

- Edmonds-Karp Algorithm

Source Vertex:

- G (Goal)

Sink Vertex:

- S (Start)

Capacity Rule:

```text
capacity(u,v) = value(v)
```

Special Cases:

```text
capacity into S = 100
capacity into G = 100
```

Objective:

- Compute the maximum possible flow from G to S.

Output:

- Maximum flow value
- Positive flow edges
- Movement mode used

---

## Subtask E – Minimum Spanning Tree

Algorithm Used:

- Prim's Algorithm

Edge Weight Rule:

```text
weight(u,v) = value(u) + value(v)
```

Objective:

- Compute the Minimum Spanning Tree (MST) for the connected component containing S.

Output:

- Total MST weight
- Number of vertices
- Number of tree edges
- List of MST edges
- Reachability of G

---

# Time Complexity Summary

| Algorithm | Time Complexity | Space Complexity |
|------------|----------------|------------------|
| BFS | O(V + E) | O(V) |
| Dijkstra | O((V + E) log V) | O(V) |
| Edmonds-Karp | O(VE²) | O(V + E) |
| Prim MST | O(E log V) | O(V) |

Where:

- V = Number of vertices
- E = Number of edges

---

# Required Test Maze Results

Maze File:

```text
maze_10x10_A.txt
```

Results Produced:

- Minimum Moves: 18
- Minimum Cost: 26
- Maximum Flow: 1
- MST Total Weight: 390

Additional comparison:

- 4-direction shortest path = 18 moves
- 8-direction shortest path = 11 moves
- 4-direction minimum cost = 26
- 8-direction minimum cost = 18

---

# Running the Program

Run using:

```bash
python maze_solver.py maze_10x10_A.txt
```

or

```bash
python3 maze_solver.py maze_10x10_A.txt
```

The program automatically:

1. Loads the maze file
2. Solves Subtasks A–E
3. Displays results in the terminal
4. Saves results to:

```text
output.txt
```

---

# Technologies Used

- Python 3
- Git
- GitHub
- GitHub Codespaces

---

# Academic Integrity and AI Usage Disclosure

AI tools were used for:

- Learning support
- Algorithm explanations
- Debugging assistance
- Code review assistance
- Documentation guidance
- Report preparation support

All submitted code was reviewed, tested, executed, and understood by the team members before submission.

---

# Course Information

Course: Graph Algorithms

Project Type: Final Group Project

Completed Subtasks:

- Subtask A
- Subtask B
- Subtask C
- Subtask D
- Subtask E

This project satisfies the requirements for a three-member team by implementing all mandatory subtasks and producing reproducible results for the required maze file.