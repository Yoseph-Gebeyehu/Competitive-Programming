class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        s = 0
        new_set = set()
        for i in c.most_common():
            if s < len(arr)//2:
                new_set.add(i[0])
                s += c[i[0]]
            else:
                break
        return len(new_set)
