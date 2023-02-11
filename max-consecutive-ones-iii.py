class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = k
        l,i = 0,0
        maxi = 0
        while i < (len(nums)):
            if n >= 0 and nums[i] == 0:
                n -= 1
            while n == -1:
                if  nums[i] == 0:
                    if nums[l] == 0:
                        n += 1
                    l += 1
                else:
                    i += 1
                    break
            maxi = max(maxi, i - l + 1)
            i += 1
        return maxi
