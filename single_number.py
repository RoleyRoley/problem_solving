class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # For every num, is num in nums twice? 
        for num in nums:
            # Find number of occurences.
            if nums.count(num) < 2:
                return num
            