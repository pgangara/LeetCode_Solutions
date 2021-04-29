# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1




class Solution:
    def moveZeroes(self,nums):
        if len(nums)==1:
            return nums
        num_zeros = nums.count(0)
        if num_zeros == 0:
            return nums
        start_index = 0
        i = 0
        while i <= num_zeros:
            if nums[start_index]!= 0 :
                start_index = start_index+1
            else:
                del nums[start_index]
                nums.append(0)
                i = i+1
        return nums
