class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        count = {}

        # Loop through letters in s. 
        for letter in s:

            # Add letter to count dict, increase count.
            count[letter] = count.get(letter, 0) + 1
            


        # Loop through letters in t
        # Attempt to build
        for letter in t:
            
            # If letter is not count or letter count = 0, return letter.
            if letter not in count or count[letter] == 0:
                return letter
            
            # Decrease count
            count[letter] -= 1
        
        return True