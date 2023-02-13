class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,len(nums) - 1
        output = 0
        while r>l:
            if nums[r] + nums[l] > k:
                r -= 1
            elif nums[r] + nums[l] < k:
                l += 1
            else:
                output += 1
                l += 1
                r -= 1
        return output
