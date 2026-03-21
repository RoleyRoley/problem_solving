class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Loop through digits in reverse order.
        for num in range(len(digits) -1, -1, -1):
            # If last digit is less than 9, add 1.
            if digits[num] < 9:
                digits[num] += 1
                return digits
            # last digit is now 0
            digits[num] = 0
        # Adds 1 infront if all digits were 9s
        return [1] + digits
        