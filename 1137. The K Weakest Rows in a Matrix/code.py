class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        vals = []
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            count = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count += 1
            vals.append((count, i))
        cur = []
        heapq.heapify(vals)
        for _ in range(k):
            cur.append(heapq.heappop(vals)[1])
        return cur

