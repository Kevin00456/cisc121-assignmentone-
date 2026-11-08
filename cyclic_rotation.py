def solution(A, K):
    """
    Rotate list A to the right by K positions.

    Args:
        A: A list of integers.
        K: The number of right rotations.

    Returns:
        A new list containing A rotated to the right K positions.
    """

    # An empty list cannot be rotated.
    if len(A) == 0:
        return A

    # Rotating by the list length (or a multiple of it)
    # brings the list back to its original order.
    K = K % len(A)

    # If K is 0, no rotation is needed.
    if K == 0:
        return A

    # Move the last K elements to the beginning.
    return A[-K:] + A[:-K]


# Example test cases.
if __name__ == "__main__":
    print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
    print(solution([0, 0, 0], 1))        # [0, 0, 0]
    print(solution([1, 2, 3, 4], 4))     # [1, 2, 3, 4]
    print(solution([1, 2, 3], 1))        # [3, 1, 2]
    print(solution([], 3))              # []
