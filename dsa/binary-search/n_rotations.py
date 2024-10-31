"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the number of times the array was rotated.
You must write an algorithm that runs in O(log n) time.
Example:
Input: nums = [3,4,5,1,2]
[5,6,1,2,3,4]
Output: 3
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Note: This is exactly same as rotated_sorted_array_min.py but here we return the index
instead of the value.
"""
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG)


class Solution:
    def findNumberOfRotations(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low<high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return low

tests = [{
    "nums": [4,5,6,7,0,1,2],
    "expected": 4},
    {
    "nums": [3,4,5,1,2],
    "expected": 3},
]
for i, test in enumerate(tests):
    logging.info(f"Running test case #{i+1}")
    sol = Solution().findNumberOfRotations(nums=test["nums"])
    assert sol == test["expected"], f"Expected {test['expected']} but got {sol}"
    logging.info("Passed!")