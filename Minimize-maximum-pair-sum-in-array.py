class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        j = 0
        pair_sum = []
        nums.sort()
        for i in range(len(nums)- 1,len(nums)//2 -1,-1):
            pair_sum.append(nums[i] + nums[j])
            j += 1
        return max(pair_sum)
