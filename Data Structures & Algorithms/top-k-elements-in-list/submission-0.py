from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        most_freq = freq.most_common(k)

        return [num for num, _ in most_freq]