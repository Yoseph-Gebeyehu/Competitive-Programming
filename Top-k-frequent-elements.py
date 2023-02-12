class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c.most_common()
        new_list = [j[0] for i, j in enumerate(c.most_common()) if i < k]
        return new_list
