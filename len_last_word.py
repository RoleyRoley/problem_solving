class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split string into substrings.
        words = s.split()
        # Return length of last substring.
        return len(words[-1])
