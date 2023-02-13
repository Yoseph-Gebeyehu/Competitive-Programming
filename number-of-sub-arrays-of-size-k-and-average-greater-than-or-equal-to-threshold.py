class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        sum = 0
        average = 0
        
        for i in range(k):
            sum += arr[i]
            
        if sum / k >= threshold:
            ans += 1
        l = 0
        for i in range(k,len(arr)):
            sum += arr[i]
            sum -= arr[l]
            
            if sum / k >= threshold:
                ans += 1
            l += 1
        return ans
