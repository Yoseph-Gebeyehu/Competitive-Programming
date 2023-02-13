class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        answer = []
        counter = 0
        for i in nums:
            if i != 0:
                pro *= i
            else:
                counter += 1
        for i in nums:
            if i != 0 and counter == 1:
                answer.append(0)
            elif i == 0 and counter == 1:
                answer.append(pro)
            elif counter == 0:
                answer.append(pro//i)
            elif counter > 1:
                answer.append(0)
        return answer
