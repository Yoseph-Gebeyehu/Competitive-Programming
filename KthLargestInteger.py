class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums) - 1):
            for j in range(len(nums)-i-1):
                if int(nums[j]) > int(nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[len(nums) - k]
