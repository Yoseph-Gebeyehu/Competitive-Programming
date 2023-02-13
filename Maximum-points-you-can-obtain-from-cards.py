class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maximum = 0
        sum = 0

        for i in range(len(cardPoints) - k,len(cardPoints)):
            sum += cardPoints[i]
            
        maximum = max(sum,maximum)
        j = (len(cardPoints) - k)
        
        if k == len(cardPoints):
            return maximum
            
        
        for i in range(len(cardPoints),len(cardPoints) + k):
            l = j % len(cardPoints)
            r = i % len(cardPoints)
            
            sum += cardPoints[r] 
            sum -= cardPoints[l]
            
            maximum = max(maximum,sum)
            j += 1
        return maximum
