# Time complexity is O(n) because we iterate through the list of numbers once.

class Solution:  
  def two_sum(nums, target):
    numbers_and_indices = {}
    for i, num in enumerate(nums):
      if target - num in numbers_and_indices:
        return [numbers_and_indices[target-num], i]
      numbers_and_indices[num] = i
      
    return []
