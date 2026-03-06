class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Is x positive or negative
        if x < 0:
            return False
        # flip  x
        reversed_x = int(str(x)[::-1])

        return reversed_x == x