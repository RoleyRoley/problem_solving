class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Using sets to track elements
        seen = set()

        # Cycle through elements in array, if num appears in seen, return True.
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
