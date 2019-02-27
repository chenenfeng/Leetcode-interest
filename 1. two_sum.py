"""
set a dictionary
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[target-nums[i]] = nums[i]
            else:
                return [nums.index(target-nums[i]),i]
            
