class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Find needle string within haystack string.
        index = haystack.find(needle)
        # Returns index where substring starts, or -1 if not found.
        if index != -1:
            return index
        else: 
            return -1