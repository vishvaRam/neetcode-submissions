class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp=OrderedDict()
        orderedStr=["".join(sorted(s))   for s   in  strs]
        for original,sortedstr in  zip(strs,orderedStr):
            if sortedstr not in temp:
                temp[sortedstr] = []
            temp[sortedstr].append(original)
        return  list(temp.values())