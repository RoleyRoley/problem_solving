class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Loop through nums, find target, return index of target
        # Else:
        # Copy nums array
        # Add target to copy
        # sort copy
        # return index of target
        copy = nums
        for number in nums:
            if number == target:
                return nums.index(target)
            else:
                copy.append(target)
                copy.sort()
                for number in copy:
                    if number == target:
                        return nums.index(target)


         