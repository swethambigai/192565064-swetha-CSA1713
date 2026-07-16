# 8 Puzzle Problem

## Problem Description
The 8-puzzle problem is a classic problem in Artificial Intelligence used to demonstrate state-space search algorithms.

It consists of:
- A 3 × 3 grid
- 8 numbered tiles (1–8)
- 1 blank space (represented as 0 or _)

## Initial State
2 8 3  
1 6 4  
7 _ 5  

## Goal State
1 2 3  
8 _ 4  
7 6 5  

## Rules
- Only one tile can be moved at a time.
- A tile moves into the adjacent blank space.
- Moves allowed: Up, Down, Left, Right.
- The goal is to reach the target configuration in minimum moves.

## State Space
- Total possible states = 9! = 362,880
- Solvable states = 181,440

## Approach
We use **A\* Search Algorithm**.

### Heuristic Used
**Manhattan Distance**:
Sum of horizontal and vertical distances of each tile from its goal position.

## Algorithm Steps
1. Start from initial state
2. Generate all possible moves
3. Calculate cost: f(n) = g(n) + h(n)
4. Choose state with lowest cost
5. Repeat until goal is reached

## Output
Sequence of steps from initial state to goal state.