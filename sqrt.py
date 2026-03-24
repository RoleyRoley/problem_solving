class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci pattern.
        # n = steps.

        # Handle base case.
        # If n is 1 or 2, answer is n ways.
        if n <= 2:
            return n

        # Starting values.
        prev2 = 1
        prev1 = 2

        # Loop through steps.
        for i in range(3, n + 1):
            # Add starting values for current value.
            current = prev1 + prev2
            # Swap starting values.
            prev2 = prev1
            prev1 = current
        
        return prev1