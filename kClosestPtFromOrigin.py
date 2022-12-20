class Solution:
    def kClosest(self, arr: List[List[int]], k: int) -> List[List[int]]:
        num = []
        for i in range(len(arr)):
            d = ((arr[i][0]) ** 2 + arr[i][1] ** 2) ** 0.5
            num.append(round(d,3))

        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if num[min_index] > num[j]:
                    min_index = j       
            arr[i], arr[min_index] = arr[min_index], arr[i]
            
        if k == 1:
            return [arr[0]]  
        elif k == 2:
            return [arr[0],arr[1]]
