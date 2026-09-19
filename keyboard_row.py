class Solution:
    def findWords(self, words: list[str]) -> list[str]:

        # Convert rows to lists
        first_row = list("qwertyuiop")

        second_row = list("asdfghjkl")

        third_row = list("zxcvbnm")


        # Set blank output
        output = []

        
        for word in words:
            # Normalise
            word_lower = word.lower()
            
            # Create list of word
            chars = list(word_lower)
            print(chars)
            print(len(chars))
            
            # Find number of matching characters in rows.
            first_comp = set(chars) & set(first_row)
            second_comp = set(chars) & set(second_row)
            third_comp = set(chars) & set(third_row)
            print("Length of chars", len(set(chars)))

            # If comparison is an exact match, append output list.
            if len(first_comp) == len(set(chars)) or len(second_comp) == len(set(chars)) or len(third_comp) == len(set(chars)):
                output.append(word)
            

           


            
            
        # Return answer
        return output

