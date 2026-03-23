class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert a and b to int.
        int_a = int(a, 2)
        int_b = int(b, 2)

        # Add a and b
        int_sum = int_a + int_b

        # Convert back to binary, removing '0b' prefix.
        binary_sum = bin(int_sum)[2:]
        return binary_sum