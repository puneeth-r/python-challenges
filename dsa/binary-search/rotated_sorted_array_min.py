"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
Example:
Input: nums = [3,4,5,1,2]
[5,6,1,2,3,4]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG)


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low<high:
            mid = (low+high)//2
            if  nums[mid]> nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


tests = [{
    "nums": [4,5,6,7,0,1,2],
    "expected": 0},
    {
    "nums": [3,4,5,1,2],
    "expected": 1},
    #     {
    # "nums": [4,5,6,7,0,1,2],
    # "target": 3,
    # "expected": -1},
]
for i, test in enumerate(tests):
    logging.info(f"Running test case #{i+1}")
    sol = Solution().findMin(nums=test["nums"])
    assert sol == test["expected"], f"Expected {test['expected']} but got {sol}"
    logging.info("Passed!")