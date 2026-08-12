class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegrees = [ 0 for _ in range(numCourses)]

        for u,v in prerequisites:
            adj_list[v].append(u)
            indegrees[u] +=1

        queue = deque()
        result = []

        for i in range(0, numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while len(queue) != 0:

            current_node = queue.popleft()
            result.append(current_node)

            for adjNode in adj_list[current_node] :
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
        if len(result) == numCourses:
            return True
        return False
        
            
        