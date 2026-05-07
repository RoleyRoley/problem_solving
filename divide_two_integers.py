class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        

        # Handle overflow case for 32-bit signed integer.
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Positive or negative, ^ = XOR (If one negative, answer is negative,)
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1


        # Make both numbers positive for ease.
        dividend, divisor = abs(dividend), abs(divisor)


        # Quotient = answer
        quotient = 0

        # Iterate from most to least significant bit.
        for i in range(31, -1, -1):

            # << shift left, 2**i
            # Can divisor * 2**i fit inside dividend?
            if (divisor << i) <= dividend:

                # Subtract
                dividend -= (divisor << i)
                
                # Set matching bit in quotient
                quotient |= (1 << i)

        # Truncate to zero (E.g. 4.7968 -> 4)
        return int(sign * quotient)