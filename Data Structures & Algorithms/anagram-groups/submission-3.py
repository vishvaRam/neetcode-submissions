from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            sstring = "".join(sorted(i))
            res[sstring].append(i)
        return list(res.values())

