class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        l_s = 0
        for i in range(len(nums)):
            r_s = total_sum - l_s - nums[i]
            if l_s  == r_s:
                return i
            l_s += nums[i]
        return -1
