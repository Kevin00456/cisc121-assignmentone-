def solution(X, A):
    """
    Find the earliest time when leaves have appeared at every position
    from 1 through X.

    Args:
        X: The destination position across the river.
        A: A list where A[K] is the position of a leaf falling at time K.

    Returns:
        The earliest time when all positions are covered, or -1 if
        the frog can never cross.
    """

    # Keep track of positions where a leaf has already appeared.
    covered_positions = set()

    # Count how many different required positions have been covered.
    covered_count = 0

    # Check each leaf in the order it falls.
    for time in range(len(A)):
        position = A[time]

        # Only count a position the first time a leaf appears there.
        if position not in covered_positions:
            covered_positions.add(position)
            covered_count += 1

            # If all positions from 1 through X are covered,
            # the frog can cross at this time.
            if covered_count == X:
                return time

    # At least one required position never received a leaf.
    return -1


# Example test cases.
if __name__ == "__main__":
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))  # 6
    print(solution(3, [1, 2, 3]))                # 2
    print(solution(3, [1, 2, 2, 1]))             # -1
    print(solution(1, [1]))                      # 0
    print(solution(2, [2, 2, 2]))                # -1
