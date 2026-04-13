class Solution:
    def reverse(self, x: int) -> int:
        
        # Defining 32 bit limits
        int_max = 2**31 - 1 # 2147483647
        int_min = -2**31    # -2147483648


        # Storing the sign of the number
        sign = -1 if x < 0 else 1


        x = abs(x)


        # Will store the reversed number
        rev = 0


        # Loop until all digits are processed
        while x != 0:
            # Get last digit fo x
            digit = x % 10

            # Removed last digit from x
            x //= 10

            # Check if number with 'overflow'
            # Check edge case
            if rev > int_max // 10 or (rev == int_max // 10 and digit > 7):
                return 0 # if 'overflow' occurs, return 0

            # Append digit to reversed number
            rev = rev * 10 + digit
        
        # Reapply original sign, return result
        return sign * rev