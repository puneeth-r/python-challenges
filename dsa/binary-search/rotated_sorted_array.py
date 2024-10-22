"""81. Search in Rotated Sorted Array II
Medium
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: true"""
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG)


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1 
            else:
                if  nums[high]>= target and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


tests = [{
    "nums": [4,5,6,7,0,1,2],
    "target": 0,
    "expected": 4},
    {
    "nums": [1],
    "target": 0,
    "expected": -1},
        {
    "nums": [4,5,6,7,0,1,2],
    "target": 3,
    "expected": -1},
]
for i, test in enumerate(tests):
    logging.info(f"Running test case #{i+1}")
    sol = Solution().search(nums=test["nums"], target=test['target'])
    assert sol == test["expected"], f"Expected {test['expected']} but got {sol}"
    logging.info("Passed!")