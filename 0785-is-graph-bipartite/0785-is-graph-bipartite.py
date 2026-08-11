class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        def dfs(node, curr_color):
            color[node] = curr_color

            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei, 1 - curr_color):
                        return False

                elif color[nei] == curr_color:
                    return False

            return True

        for i in range(n):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False

        return True