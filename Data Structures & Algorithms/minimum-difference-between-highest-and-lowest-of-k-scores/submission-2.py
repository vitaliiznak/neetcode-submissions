class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        sorted_n = sorted(nums)
        l = 0

        if len(nums) < 2:
            return 0

        minimum = sorted_n[k-1] - sorted_n[0]
        for r in range(k-1, len(sorted_n)):
            l = r - k + 1
            minimum = min(minimum, sorted_n[r] - sorted_n[l])
        return minimum

