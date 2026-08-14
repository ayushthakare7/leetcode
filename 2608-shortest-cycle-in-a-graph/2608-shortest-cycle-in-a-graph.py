from collections import deque

class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = float('inf')

        for start in range(n):

            dist = [-1] * n
            parent = [-1] * n

            queue = deque([start])
            dist[start] = 0

            while queue:
                node = queue.popleft()

                for nei in graph[node]:

                    if dist[nei] == -1:
                        dist[nei] = dist[node] + 1
                        parent[nei] = node
                        queue.append(nei)

                    elif parent[node] != nei:
                        # Cycle found
                        cycle_length = dist[node] + dist[nei] + 1
                        ans = min(ans, cycle_length)

        return -1 if ans == float('inf') else ans