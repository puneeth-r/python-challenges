"""
540. Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.
Example:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
"""
from typing import List
import logging

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """Hint: so in the array if (current_index, current_index + 1)
        1. is (even,odd) with same element then you are on left side of the single element
        2. is (odd,even) with same element then you are on right side of the single element
        """ 
        n = len(nums) - 1
        if nums[0] != nums[1]:
            return nums[0]
        elif nums[n-1] != nums[n-2]:
            return nums[n-1]
        else:
            low, high = 1, len(nums) - 2
            while low<=high:
                mid = (low+high)//2
            if (mid == 0 or nums[mid] != nums[mid - 1]) and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 == 1 and nums[mid] == nums[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1
            return -1

tests = [{
    "nums": [1,1,2,3,3,4,4,8,8],
    "expected": 2}
]
for i, test in enumerate(tests):
    logging.info(f"Running test case #{i+1}")
    sol = Solution().singleNonDuplicate(nums=test["nums"])
    assert sol == test["expected"], f"Expected {test['expected']} but got {sol}"
    logging.info("Passed!")



