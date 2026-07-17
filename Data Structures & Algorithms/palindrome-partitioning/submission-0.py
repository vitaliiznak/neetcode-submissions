class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # BASE CASE: empty string. There's exactly one way to cut nothing:
        # into zero pieces. So we return a list holding one empty partition.
        if not s:
            return [[]]

        res = []
        # try every possible front piece: "a", "aa", "aab", ...
        for end in range(1, len(s) + 1):
            front = s[:end]
            if front == front[::-1]:            # is that front piece a palindrome?
                # LEAP OF FAITH: trust this gives every way to cut the leftover
                for rest in self.partition(s[end:]):
                    res.append([front] + rest)  # glue front onto each of those
        return res          



        