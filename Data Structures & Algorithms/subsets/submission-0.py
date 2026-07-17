class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        def dfs(start, path):
            res.append(path[:])                 # ① every node IS a subset → always snapshot
            for i in range(start, len(nums)):   # ② choice = each remaining number
                path.append(nums[i])   # CHOOSE
                dfs(i + 1, path)             # EXPLORE
                path.pop()             # UN-CHOOSE
        dfs(0,[])
        return res
        