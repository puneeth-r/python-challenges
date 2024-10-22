"""34. Find First and Last Position of Element in Sorted Array
Medium
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start = self.find_start(nums, target)
        if start == -1:
            return [-1, -1]
        end = self.find_end(nums, target)
        return [start, end]

    def find_start(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low if low < len(nums) and nums[low] == target else -1
    
    def find_end(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return high if high < len(nums)and nums[high] == target else -1


tests = [{
    "nums": [5,7,7,8,8,10],
    "target": 8,
    "expected": [3,4]},
    {
    "nums": [],
    "target": 8,
    "expected": [-1,-1]},
        {
    "nums": [2,2],
    "target": 8,
    "expected": [-1,-1]}
]
for i, test in enumerate(tests):
    logging.info(f"Running test case #{i+1}")
    sol = Solution().searchRange(nums=test["nums"], target=test['target'])
    assert sol == test["expected"], f"Expected {test['expected']} but got {sol}"
    logging.info("Passed!")
