class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        m_f = max(freq.values())

        l_p = (m_f - 1) * (n+1)
        n_o_f = 0
        for k,v in freq.items():
            if m_f == v:
                n_o_f += 1
        return max(l_p + n_o_f,len(tasks))
