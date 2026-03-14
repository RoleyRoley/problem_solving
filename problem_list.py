class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # Loop through nums.
        for number in nums:
            # If number is NOT equal to val.
            if number != val:
                # Place at nums[k]
                nums[k] = number
                k = k + 1
        return k
        