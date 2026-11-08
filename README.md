# CISC 121 Assignment One

This repository contains Python solutions for the selected programming problems in the CISC 121 assignment.

## Problem 1 — Cyclic Rotation

**Problem source:** [Codility — Cyclic Rotation](https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/)

Given a list of integers `A` and a non-negative integer `K`, rotate the list to the right by `K` positions. Each right rotation moves the last element to the front.

**Python file:** [`cyclic_rotation.py`](cyclic_rotation.py)

**Example:** `solution([3, 8, 9, 7, 6], 3)` returns `[9, 7, 6, 3, 8]`.

**Approach:** Handle an empty list, reduce the number of rotations using `K % len(A)`, then use slicing to move the final `K` elements to the beginning.

**Complexity:** O(N) time and O(N) additional space, where N is the list length.

## Problem 2 — Frog Jmp

**Problem source:** [Codility — Frog Jmp](https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/)

A frog starts at position `X` and wants to reach or pass position `Y`. Each jump covers exactly `D` units. Return the minimum number of jumps needed.

**Python file:** [`frog_jmp.py`](frog_jmp.py)

**Example:** `solution(10, 85, 30)` returns `3`.

**Approach:** Calculate the distance `Y - X`, divide by `D`, and round up when there is a remainder. If `X >= Y`, return 0.

**Complexity:** O(1) time and O(1) additional space.

## Problem 3 — Tape Equilibrium

**Problem source:** [Codility — Tape Equilibrium](https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/)

Given a non-empty list of integers `A`, split it at a position `P` where `1 <= P < len(A)`. Find the minimum absolute difference between the sum of the left part and the sum of the right part.

**Python file:** [`tape_equilibrium.py`](tape_equilibrium.py)

**Example:** `solution([3, 1, 2, 4, 3])` returns `1`.

**Approach:** Calculate the total sum once. Move through each valid split while updating the left sum; calculate the right sum as the total minus the left sum. Track the smallest absolute difference.

**Complexity:** O(N) time and O(1) additional space.

## Problem 4 — Frog River One

**Problem source:** [Codility — Frog River One](https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/)

A frog wants to cross a river by jumping to the opposite bank at position X + 1. Leaves fall at positions recorded in array `A`, where `A[K]` is the position of a leaf at time K. Return the earliest time when every position from 1 through X has a leaf, or -1 if this never happens.

**Python file:** [`frog_river_one.py`](frog_river_one.py)

**Example:** `solution(5, [1, 3, 1, 4, 2, 3, 5, 4])` returns `6`.

**Approach:** Use a set to remember distinct positions that have received leaves. Increase the count only when a new required position appears. Return the current time once X distinct positions are covered; otherwise return -1.

**Complexity:** O(N) expected time and O(X) space, where N is the number of leaves.
