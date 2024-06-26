test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([-3, 4, 3, 90], 0, [0, 2]),
    ([5, 10, 15, 20], 25, [1, 3]),
    ([1, 2, 3, 4, 5], 9, [3, 4]),
    ([10, 20, 30, 40, 50], 60, [2, 4]),
    ([100, 200, 300, 400], 500, [1, 3]),
    ([1, 3, 5, 7, 9], 6, [1, 2]),
    ([0, 0, 0, 0], 0, [0, 1]),
    ([2, 4, 6, 8, 10], 12, [2, 3]),
    ([10, 9, 8, 7, 6, 5], 15, [0, 1]),
    ([1, 2, 3, 4, 5, 6, 7], 14, [5, 6]),
    ([1, 1, 1, 1], 2, [0, 1]),
    ([2, 4, 6, 8, 10], 19, None),
    ([-1, -2, -3, -4, -5], -9, [0, 4]),
    ([5, 4, 3, 2, 1], 5, [0, 1]),
    ([100, 200, 300, 400, 500], 1000, [0, 4]),
    ([10, 20, 30, 40, 50], 90, [3, 4]),
    ([1, 2, 3, 4, 5], 5, [0, 4]),
    ([1, 2, 3, 4, 5], 3, [0, 2]),
    ([1, 3, 5, 7, 9], 5, [0, 2]),
    ([0, 1, 2, 3, 4], 4, [0, 4]),
    ([10, 20, 30, 40, 50], 60, None),
    ([1, 2, 3, 4, 5], 10, None),
    ([1, 3, 5, 7, 9], 8, None),
    ([1, 2, 3, 4, 5], 6, [1, 4]),
    ([2, 4, 6, 8, 10], 10, [0, 4]),
    ([1, 2, 3, 4, 5], 8, None),
    ([1, 3, 5, 7, 9], 4, None),
    ([2, 4, 6, 8, 10], 5, None),
    ([1, 2, 3, 4, 5], 7, None),
    ([1, 3, 5, 7, 9], 10, None),
    ([2, 4, 6, 8, 10], 11, None),
    ([1, 2, 3, 4, 5], 2, None),
    ([1, 3, 5, 7, 9], 3, None),
    ([2, 4, 6, 8, 10], 9, None),
    ([1, 2, 3, 4, 5], 1, None),
    ([1, 3, 5, 7, 9], 0, None),
    ([2, 4, 6, 8, 10], 7, None),
    ([1, 2, 3, 4, 5], 0, None),
    ([1, 3, 5, 7, 9], 12, None),
    ([2, 4, 6, 8, 10], 15, None),
    ([1, 2, 3, 4, 5], -1, None),
    ([1, 3, 5, 7, 9], -5, None),
    ([2, 4, 6, 8, 10], -3, None),
    ([1, 2, 3, 4, 5], -7, None),
    ([1, 3, 5, 7, 9], -9, None),
    ([2, 4, 6, 8, 10], -11, None),
    ([1, 2, 3, 4, 5], -2, [0, 2]),
    ([1, 3, 5, 7, 9], -3, [0, 1]),
    ([2, 4, 6, 8, 10], -9, None),
    ([1, 2, 3, 4, 5], -4, None),
    ([1, 3, 5, 7, 9], -7, None),
    ([2, 4, 6, 8, 10], -15, None),
    ([1, 2, 3, 4, 5], -6, None),
    ([1, 3, 5, 7, 9], -10, None),
    ([2, 4, 6, 8, 10], -19, None),
    ([1, 2, 3, 4, 5], -5, [0, 2]),
    ([1, 3, 5, 7, 9], -15, [0, 3]),
    ([2, 4, 6, 8, 10], -25, [0, 4]),
    ([1, 2, 3, 4, 5], -25, None),
    ([1, 3, 5, 7, 9], -2, None),
    ([2, 4, 6, 8, 10], -6, [0, 1]),
    ([1, 2, 3, 4, 5], -8, None),
    ([1, 3, 5, 7, 9], -4, [0, 2]),
    ([2, 4, 6, 8, 10], -10, [0, 3]),
    ([1, 2, 3, 4, 5], -3, None),
    ([1, 3, 5, 7, 9], -8, None),
    ([2, 4, 6, 8, 10], -12, [0, 2]),
    ([1, 2, 3, 4, 5], -9, [0, 3]),
    ([1, 3, 5, 7, 9], -11, [0, 4]),
    ([2, 4, 6, 8, 10], -20, None),
    ([1, 2, 3, 4, 5], -15, [0, 4]),
    ([1, 3, 5, 7, 9], -19, [0, 4]),
    ([2, 4, 6, 8, 10], -21, None),
    ([1, 2, 3, 4, 5], -20, [0, 4]),
    ([1, 3, 5, 7, 9], -25, None),
    ([2, 4, 6, 8, 10], -30, None),
    ([1, 2, 3, 4, 5], -30, None),
    ([1, 3, 5, 7, 9], -30, None),
    ([2, 4, 6, 8, 10], -35, None),
    ([1, 2, 3, 4, 5], -35, None),
    ([1, 3, 5, 7, 9], -35, None),
    ([2, 4, 6, 8, 10], -40, None),
    ([1, 2, 3, 4, 5], -40, None),
    ([1, 3, 5, 7, 9], -40, None),
    ([2, 4, 6, 8, 10], -45, None),
    ([1, 2, 3, 4, 5], -45, None),
    ([1, 3, 5, 7, 9], -45, None),
    ([2, 4, 6, 8, 10], -50, None),
    ([1, 2, 3, 4, 5], -50, None),
    ([1, 3, 5, 7, 9], -50, None)
]

# Printing the test cases
for i, (nums, target, expected_output) in enumerate(test_cases, 1):
    print(f"Test Case {i}: Input: nums = {nums}, target = {target}, Expected Output: {expected_output}")
