"""
Location: LeetCode - 217. Contains Duplicate

Description: Given an integer array nums, return true if any value appears at least twice in the array, and 
return false if every element is distinct.

Time Complexity: O(n)
Space Complexity: O(n)
Time to efficient solution: 45 mins
"""

# Notes:
    # 1. Input is an int array
    # 2. Output expects a boolean

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # if nums only has one number, return false
        if len(nums) == 1:
            return False
        
        # initialize dictionary for fast lookup
        nums_dict = defaultdict(int)
        
        # iterate through list
        for num in nums:            
            
            # None entries in default dictionary returns 0 by default
            # if entry does not equal zero just return true because we increment below
            if nums_dict[num] != 0:
                return True
            
            nums_dict[num] += 1
            
        return False