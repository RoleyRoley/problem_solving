class Solution:
    def isUgly(self, n: int) -> bool:
        

        # Ugly numbers must be positive
        if n <= 0:
            return False

        # Keep dividing by 2 while possible
        while n % 2 == 0:
            n //= 2

        # Keep dividing by 3 while possible
        while n % 3 == 0:
            n //= 3

        # Keep dividing by 5 while possible
        while n % 5 == 0:
            n //= 5

        # If only factors 2,3,5 existed, number becomes 1
        return n == 1