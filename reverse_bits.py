class Solution:
    def reverseBits(self, n: int) -> int:
        # Convert int to binary, remove '0b'
        binary = bin(n)[2:]

        # Pad to 32 bits
        binary_str = binary.zfill(32)

        # Reverse str
        reversed_binary_str = binary_str[::-1]

        # Convert str to int (base 2)
        return int(reversed_binary_str, 2)

