def solution(X, Y, D):
    """
    Return the minimum number of jumps needed for the frog
    to travel from position X to a position at least Y.

    Args:
        X: The frog's starting position.
        Y: The target position.
        D: The fixed distance covered by each jump.

    Returns:
        The minimum number of jumps required.
    """

    # If the frog is already at or beyond the target, no jump is needed.
    if X >= Y:
        return 0

    # Calculate the total distance the frog must cover.
    distance = Y - X

    # Calculate the number of complete jumps.
    jumps = distance // D

    # If there is a remainder, one additional jump is needed.
    if distance % D != 0:
        jumps += 1

    return jumps


# Example test cases.
if __name__ == "__main__":
    print(solution(10, 85, 30))  # 3
    print(solution(10, 10, 30))  # 0
    print(solution(10, 11, 30))  # 1
    print(solution(10, 70, 20))  # 3
    print(solution(1, 5, 2))     # 2
