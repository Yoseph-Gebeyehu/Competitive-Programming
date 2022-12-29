class Solution:
    def rearrangeArray(self, num: List[int]) -> List[int]:
        for i in range(1,len(num)-1):
            if (num[i-1] + num[i+1]) / 2 == num[i] and i < len(num)-1:
                if i < len(num) - 2:
                    temp = num[i+1]
                    num[i+1] = num[i+2]
                    num[i+2] = temp
                else:
                    temp2 = num[i]
                    num[i] = num[i+1]
                    num[i+1] = temp2
        return num
