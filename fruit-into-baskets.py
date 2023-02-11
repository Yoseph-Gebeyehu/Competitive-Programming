class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        r,l = 0,0
        window = 0
        tmp = {}
        while r < len(fruits):
            tmp[fruits[r]] = r
            if len(tmp) >= 3:
                min_val = min(tmp.values())
                del tmp[fruits[min_val]]
                l = min_val + 1
            window = max(window , r - l +1)
            r += 1
        return window
