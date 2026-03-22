

"""Given a sorted array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice. """

from typing import List



class Solution:
    def twoSum(self, numbers: List[int], target: int) :
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1

# Example usage:
numbers = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(numbers, target))  # Output: [1, 2]
