class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_s = dict()

        for str_i in strs:
            sorted_id = sorted(str_i)
            if tuple(sorted_id) in map_s:
                map_s[tuple(sorted_id)].append(str_i)
            else:
                map_s[tuple(sorted_id)] = [str_i]

        return list(map_s.values())


        