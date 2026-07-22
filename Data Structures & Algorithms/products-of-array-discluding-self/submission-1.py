import math

# prefix =      1  [1, 2, 8, 48]
# suffix = [1, 48, 24 ,6] 1
         
        #  [44, 24, 12, 8 ]
        #   [1,2,4,6]



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul: list[int] = []
        suffix_mul: list[int] = []
        
        # Build prefix products (product of all elements to the left)
        current = 1
     
        for num in nums:
            prefix_mul.append(current)
            current *= num
        # prefix_mul = [1] + prefix_mul
        # prefix_mul.pop()

        print('prefix', prefix_mul)
        
        # Build suffix products (product of all elements to the right)
        # Using reversed for suffix
        current = 1
        for num in reversed(nums):
            suffix_mul.append(current)
            current *= num
        suffix_mul.reverse()  # Reverse back to original order
        # suffix_mul.pop(0)
        # suffix_mul.append(1)
        print('suffix_mul', suffix_mul)

        prod = []
        for i, (pr, suf) in enumerate(zip(prefix_mul,suffix_mul)):
            prod_to = pr * suf
            prod.append(prod_to)
        return prod








        