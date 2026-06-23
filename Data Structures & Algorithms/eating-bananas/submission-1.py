class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        curr_min = -1
        while l <=r:
            m = l + (r-l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/m)
            if total_time <= h:
                curr_min = m
                r = m - 1
            else:
                l = m + 1
                
        return curr_min              
        
