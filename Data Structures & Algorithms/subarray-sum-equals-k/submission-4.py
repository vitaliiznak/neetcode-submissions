from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # prefix_sum = []
        # for i, num in enumerate(nums):
        #     if len(prefix_sum):
        #         previous_sum = prefix_sum[i-1]
        #     else:
        #         previous_sum = 0
        #     prefix_sum.append(previous_sum + num)

        # prefix_dic = defaultdict(int)

        # for i, num in enumerate(nums):
        #     prefix_dic[num] += 1


     
      

        sum_t = 0
        sum_nums = 0
        prefix_sum_one: list[int] = []
        pr_sum_dict = defaultdict(int)
        pr_sum_dict[0] = 1

        for i, num in enumerate(nums):
            sum_t += num
            diff = sum_t - k 
            sum_nums += pr_sum_dict.get(diff, 0) 
            prefix_sum = (prefix_sum_one[i-1] if prefix_sum_one else 0) + num
            prefix_sum_one.append(prefix_sum)
            pr_sum_dict[prefix_sum] += 1


  


      
  
        return sum_nums


            


        
        





        