from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # Sort values along with original indices
        arr = sorted((nums[i], i) for i in range(n))

        # position[original_index] = position in sorted order
        pos = [0] * n

        # component id in sorted order
        comp = [0] * n

        values = [0] * n

        component = 0

        for i, (value, idx) in enumerate(arr):
            values[i] = value
            pos[idx] = i

            if i > 0 and values[i] - values[i - 1] > maxDiff:
                component += 1

            comp[i] = component

        # -------------------------
        # Compute next[] using two pointers
        # next_jump[i] = farthest index reachable in one edge
        # -------------------------
        next_jump = [0] * n

        r = 0

        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            next_jump[l] = r

        # -------------------------
        # Binary lifting
        # up[k][i] = position after 2^k jumps
        # -------------------------
        LOG = 18

        up = [next_jump]

        for _ in range(1, LOG):
            prev = up[-1]
            curr = [0] * n

            for i in range(n):
                curr[i] = prev[prev[i]]

            up.append(curr)

        # -------------------------
        # Answer queries
        # -------------------------
        ans = []

        for u, v in queries:

            u = pos[u]
            v = pos[v]

            if u > v:
                u, v = v, u

            # Different connected components
            if comp[u] != comp[v]:
                ans.append(-1)
                continue

            # Same node
            if u == v:
                ans.append(0)
                continue

            jumps = 0
            cur = u

            # Binary lifting
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < v:
                    cur = up[k][cur]
                    jumps += 1 << k

            ans.append(jumps + 1)

        return ans