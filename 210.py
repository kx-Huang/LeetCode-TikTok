from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)  # space: O(V+E)
        in_degree = defaultdict(int)  # space: O(V)
        for end, start in prerequisites:  # O(E)
            # build the graph
            graph[start].append(end)
            # calculate in-degree
            in_degree[end] += 1

        # topology sort
        queue = deque()
        for i in range(numCourses):  # O(V)
            if in_degree[i] == 0:
                queue.append(i)

        # no starting point
        if not queue:
            return []

        # O(V+E)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return ans if len(ans) == numCourses else []
