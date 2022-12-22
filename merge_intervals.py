class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        num = []
        for i in range(len(arr)-1):
            if arr[i+1][0] - arr[i][0] == arr[i][0] and arr[i+1][1] - arr[i][1] == arr[i][1] or arr[i][1] == arr[i+1][0]:
                num.append ([arr[i][0] , arr[i+1][1]])    
            else:
                num.append([arr[i+1][0],arr[i+1][1]])
        return num
