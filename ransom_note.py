class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count = {}

        # Loop through letters in magazine. 
        for letter in magazine:

            # Add letter to count dict, increase count.
            count[letter] = count.get(letter, 0) + 1
            


        # Loop through letters in ransomNote
        # Attempt to build
        for letter in ransomNote:
            
            # If letter is not count or letter count = 0, return False.
            if letter not in count or count[letter] == 0:
                return False
            
            # Decrease count
            count[letter] -= 1
        
        return True
