class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result ,cursum = 0,0
        prefixsum = {0:1}
        for val in nums:
            cursum += val
            diff = cursum - k
            
            result += prefixsum.get(diff,0)
            prefixsum[cursum] = 1 + prefixsum.get(cursum,0)
        return result
