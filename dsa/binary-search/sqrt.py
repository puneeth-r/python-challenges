"""
Question:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python."""
import logging
logging.basicConfig(level=logging.DEBUG)


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        low = 2
        high = (x+1)//2
        while low <= high:
            mid = (low+high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
tests = [{
    "x": 4,
    "expected": 2},
    {"x":16,
    "expected": 4},
    {"x":144,
    "expected": 12},
    {"x":10,
    "expected": -1}
]
for i, test in enumerate(tests):
    x = test['x']
    expected = test['expected']
    logging.info(f"Running test case #{i+1}")
    sol = Solution().mySqrt(x=x)
    assert sol == expected, f"Expected {expected} but got {sol}"
    logging.info("Passed!")