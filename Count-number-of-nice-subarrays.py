class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [1 if n%2 != 0 else 0 for n in nums]
        m = {0:1}
        sum = 0
        count = 0
        for i in range(len(odd)):
            sum += odd[i]
            diff = sum - k
            
            count += m.get(diff,0)
            m[sum] = 1 + m.get(sum,0)
        return count
