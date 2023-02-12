class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        new_arr = [""] * len(arr)
        for i in arr:
            new_arr[int(i[-1]) - 1 ] = i[0:len(i) - 1]
        return " ".join(new_arr)
