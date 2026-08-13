from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)

        indegrees = [0] * n
        adjlist = [[] for _ in range(n)]

        queue = deque()
        result = []

        # Reverse graph
        for node in range(n):
            for adj_node in graph[node]:
                adjlist[adj_node].append(node)
                indegrees[node] += 1

        # Terminal nodes have outdegree 0
        for node in range(n):
            if indegrees[node] == 0:
                queue.append(node)

        # Kahn's algorithm
        while queue:
            node = queue.popleft()
            result.append(node)

            for adjNode in adjlist[node]:
                indegrees[adjNode] -= 1

                if indegrees[adjNode] == 0:
                    queue.append(adjNode)

        result.sort()

        return result