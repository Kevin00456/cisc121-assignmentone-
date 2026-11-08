def solution(A):
    """
    Count the number of passing car pairs.

    A pair (P, Q), where P < Q, is passing when:
    - A[P] == 0 (car travels east)
    - A[Q] == 1 (car travels west)

    Return -1 if the number of pairs exceeds 1,000,000,000.
    """

    # Count the eastbound cars seen so far.
    east_cars = 0

    # Count all passing pairs.
    passing_pairs = 0

    # Process each car from left to right.
    for car in A:
        if car == 0:
            # This eastbound car can pass every westbound car after it.
            east_cars += 1
        else:
            # Each westbound car forms a pair with all earlier eastbound cars.
            passing_pairs += east_cars

        # Codility requires -1 if the count exceeds one billion.
        if passing_pairs > 1_000_000_000:
            return -1

    return passing_pairs


# Example test cases.
if __name__ == "__main__":
    print(solution([0, 1, 0, 1, 1]))  # 5
    print(solution([0, 0, 1, 1]))     # 4
    print(solution([1, 1, 0, 0]))     # 0
    print(solution([0, 1, 1]))        # 2
    print(solution([]))               # 0
