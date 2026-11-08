def solution(A):
    """
    Find the minimum difference between the sums of the two parts
    created by splitting A at any position P (1 <= P < len(A)).

    Args:
        A: A list of integers.

    Returns:
        The smallest absolute difference between the two part sums.
    """

    # Calculate the sum of all elements in the list.
    total_sum = sum(A)

    # Start with the sum of the left part containing only A[0].
    left_sum = 0
    minimum_difference = None

    # Try every valid split, leaving at least one element on each side.
    for P in range(1, len(A)):
        left_sum += A[P - 1]

        # The right sum is the total minus the left sum.
        right_sum = total_sum - left_sum

        # Calculate the absolute difference between both sides.
        difference = abs(left_sum - right_sum)

        # Keep the smallest difference found so far.
        if minimum_difference is None or difference < minimum_difference:
            minimum_difference = difference

    return minimum_difference


# Example test cases.
if __name__ == "__main__":
    print(solution([3, 1, 2, 4, 3]))  # 1
    print(solution([5, 6]))           # 1
    print(solution([1, 2, 3, 4]))      # 2
    print(solution([-3, -1, -2, -4])) # 2
