class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        counter = 0

        new_list = list(dict.fromkeys(nums))
        
        if len(new_list) < 3:
            
            return max(new_list)

        for number in new_list:
            new_list.remove(max(new_list))
            counter += 1
            if counter == 2:
                return max(new_list)
