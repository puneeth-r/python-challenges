"""81. Search in Rotated Sorted Array II
Medium
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
Example:
Input: nums = [2,5,6,0,0,1,2], target = 1
Output: true"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pass

    def find_pivot(nums:List[int], target: int):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            elif nums[low] <= nums[mid]:
                high = mid - 1
            else:
                high = mid
        return mid
