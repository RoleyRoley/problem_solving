class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        # Start with square root, closest rectangle to square will have smallest difference between L and W.
        
        # Start width at square root of area
        width = int(area ** 0.5)


        # Move down until width divides area exactly
        while area % width != 0:
            width -= 1

        # Length is area divided by width
        length = area // width

        return [length, width]