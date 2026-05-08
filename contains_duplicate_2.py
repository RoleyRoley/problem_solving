class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        # Store number -> latest index
        seen = {}

        # Loop through array
        for i, num in enumerate(nums):

            # If number already seen before
            if num in seen:

                # Check distance between indices
                if i - seen[num] <= k:
                    return True

            # Update latest index of number
            seen[num] = i

        return False