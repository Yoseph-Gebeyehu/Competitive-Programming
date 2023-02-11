class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        window = 0
        for i in range(len(s)):
            queue.append(s[i])
            c = Counter(queue)
            while c[s[i]] > 1:
                queue.pop(0)
                c = Counter(queue)
            window = max(len(queue),window)
        return window
