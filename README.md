# CISC 121 Assignment One

This repository contains solutions for the selected programming problems in the CISC 121 assignment.

## Problem 1 — Cyclic Rotation

**Problem source:** [Codility — Cyclic Rotation](https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/)

### Problem summary
Given a list of integers `A` and a non-negative integer `K`, rotate the list to the right by `K` positions. Each right rotation moves the last element to the front.

### Python solution
The solution is in [`cyclic_rotation.py`](cyclic_rotation.py).

It first handles an empty list, then uses `K % len(A)` to remove full rotations. Python slicing moves the final `K` elements to the beginning in one operation.

### Example
Input:
```python
A = [3, 8, 9, 7, 6]
K = 3
```

Output:
```python
[9, 7, 6, 3, 8]
```

### Run the solution
From this repository's directory, run:

```bash
python cyclic_rotation.py
```

### Complexity
- **Time:** O(N), where N is the length of the list.
- **Space:** O(N), because slicing creates a new list.

## Remaining assignment work
Add the other four selected problems as separate Python files. The assignment report should also include photos of handwritten pseudocode, commented Python code, required citations, the AI conversation link, and this repository link.
