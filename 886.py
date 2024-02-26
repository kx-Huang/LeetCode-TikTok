from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        parent = list(range(n))
        size = [1] * n

        def find(node):
            nonlocal parent
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(a, b):
            nonlocal parent
            nonlocal size
            i = find(a)
            j = find(b)
            if i == j:
                return
            if size[i] > size[j]:
                parent[j] = i
                size[i] += size[j]
            else:
                parent[i] = j
                size[j] += size[i]

        table = defaultdict(list)
        for pair in dislikes:
            a, b = pair[0]-1, pair[1]-1
            table[a].append(b)
            table[b].append(a)
        for i in range(n):
            for j in table[i]:
                if find(i) == find(j):
                    return False
                union(j, table[i][0])
        return True


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
        color = [-1] * (n+1)

        def dfs(i):
            nonlocal color
            nonlocal adj
            q = deque([i])
            color[i] = 0
            while q:
                cur = q.popleft()
                for i in adj[cur]:
                    if color[i] == color[cur]:
                        return False
                    if color[i] == -1:
                        q.append(i)
                        color[i] = 1 - color[cur]
            return True

        for i in range(1, n+1):
            if color[i] == -1:
                ans = dfs(i)
                if ans == False:
                    return False
        return True
