class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        new_pushed = []
        l = 0

        for i in pushed:
            new_pushed.append(i)
            while new_pushed and new_pushed[-1] == popped[l]:
                new_pushed.pop()
                l += 1
        return len(new_pushed) == 0
