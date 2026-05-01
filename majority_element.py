class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        """
        O(n²) SOLUTION:

        # Max function, uses 'key' to find most frequent element
        most_frequent = max(nums, key=nums.count)

        return most_frequent

        Passes for small datasets, fails on large inputs


        """
        

        count = 0
        candidate = None

        # Loop through data
        for num in nums:

            # Set new candidate if needed
            if count == 0:
                candidate = num

            # Add or subtract from count 
            if num == candidate:
                count += 1
            else:
                count -= 1
            
        # Return
        return candidate