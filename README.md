# Maze Graph Algorithms

Final group project for Graph Algorithms demonstrating graph-based problem solving on maze environments.

## Team Members

- Paul Moses
- Sahan
- Canistan

---

## Project Overview

This project models a maze as a graph and applies classical graph algorithms to solve different tasks.

Implemented algorithms:

1. Breadth First Search (BFS)
2. Dijkstra's Shortest Path Algorithm
3. Edmonds-Karp Maximum Flow Algorithm
4. Prim's Minimum Spanning Tree Algorithm

Both 4-directional and 8-directional movement modes are supported.

---

## Repository Structure

```
maze-graph-algorithms
│
├── maze_solver.py
├── maze_10x10_A.txt
├── output.txt
├── report.md
└── README.md
```

---

## Implemented Tasks

### Subtask A – Shortest Path

Algorithm:
- Breadth First Search (BFS)

Objective:
- Find the minimum number of moves from S to G.

---

### Subtask B – Minimum Cost Path

Algorithm:
- Dijkstra's Algorithm

Cost Model:

```
cost(u,v) = value(v)
```

Objective:
- Find the minimum traversal cost path.

---

### Subtask C – Movement Mode Comparison

Comparison between:

- 4-directional movement
- 8-directional movement

Objective:
- Analyze the effect of diagonal movement on path length and path cost.

---

### Subtask D – Maximum Flow

Algorithm:
- Edmonds-Karp Algorithm

Source:
- G

Sink:
- S

Objective:
- Compute the maximum flow through the maze graph.

---

### Subtask E – Minimum Spanning Tree

Algorithm:
- Prim's Algorithm

Edge Weight:

```
weight(u,v) = value(u) + value(v)
```

Objective:
- Construct a minimum spanning tree for the connected component containing S.

---

## Running the Program

Run:

```bash
python maze_solver.py
```

---

## Sample Results

- Minimum Moves: 18
- Minimum Cost: 26
- Maximum Flow: 1
- MST Total Weight: 390

---

## Technologies Used

- Python 3
- GitHub
- GitHub Codespaces

---

## Academic Integrity

This project was completed as part of a Graph Algorithms course.

AI tools were used for learning support, debugging assistance, documentation guidance, and algorithm explanations.