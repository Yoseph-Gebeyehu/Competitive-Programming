class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        a = 0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] > nums[j]:
                    a += 1
            arr.append(a)
            a = 0
        return arr
