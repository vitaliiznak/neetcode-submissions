from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_seq = set(nums)

        potential_start = []
        for num in nums:
            r =  num
            l = num - 1 
            if r in set_seq and l  not in set_seq:
                potential_start.append(num)

        print('potential_start', potential_start)

        max_length = 0
        for start in potential_start:
            length = 0

            in_seq = start
            while in_seq in set_seq:
                length += 1
                in_seq += 1
            max_length = max(length,max_length )

        return max_length

                


        




        


            
            
        