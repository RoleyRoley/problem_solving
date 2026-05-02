class Solution:
    def arrangeCoins(self, n: int) -> int:



       
        
        # Starting row
        staircase_rows = 1
        
        complete_rows = 0

        # Total coins
        coins = n

        
        # While total coins > rows, add row.
        while coins >= staircase_rows:

            coins -= staircase_rows

            complete_rows += 1
            staircase_rows += 1
            
            

            # print(f"Coins:", {coins}, " - ", "Rows:", {staircase_rows})
            

            
            # Return rows - 1 for all fully completed rows.
        return staircase_rows - 1