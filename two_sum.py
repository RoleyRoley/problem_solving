class Solution:
    def two_sum(self, nums, target):
        seen = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
        
            
            complement = target - num
            
            # If the complement is already in the seen dictionary, we have found our solution
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
