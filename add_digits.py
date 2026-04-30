class Solution:
    def addDigits(self, num: int) -> int:

        

        
       
        # While num is more than 9
        while num > 9:

            # Create list of digits
            digits = [int(digit) for digit in str(num)]
            
            # Set total to 0
            total = 0


            
            # Iterate through digits list
            for digit in digits:

                # Add digits together
                total += digit
                
            # set num to new total of added digits
            num = total

            

         
        return num