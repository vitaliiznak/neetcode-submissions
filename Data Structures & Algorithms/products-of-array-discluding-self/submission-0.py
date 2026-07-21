import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        zeros_count = nums.count(0)

        if zeros_count > 1:
            return [0] * len(nums)
        elif 0 < zeros_count <= 1:
           
            non_zero_prod = math.prod([ num for num in nums if num != 0])
            output = [0]* len(nums)
            output[nums.index(0)] = non_zero_prod
            return output
        else: 
            output = []
            product = math.prod(nums)
            for num in nums:
                output.append(product//num)
            
            return output








        