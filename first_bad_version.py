class Solution:
    def firstBadVersion(self, n: int) -> int:

        # Split n into halves
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            # Narrow down bad version
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left