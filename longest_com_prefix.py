class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start at first word
        prefix = strs[0]
        
        # If empty, return ""
        if not strs:
            return ""

        # Loop through words
        for s in strs[1:]:
            # While words does NOT start with prefix, -1 character from prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                # Return "" if not common prefix found
                if not prefix:
                    return ""
        return prefix