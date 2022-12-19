class Solution:
    def targetIndices(self, a: List[int], targetNo: int) -> List[int]:
        arr = []
        for i in range(len(a) - 1):
            for j in range(len(a) - i -1):
                if a[j] > a[j+1]:    
                    a[j], a[j+1] = a[j+1], a[j]
        for i in range(len(a)):
            if a[i] == targetNo:
                arr.append(i)    
        return arr
