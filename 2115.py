from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for recipe, ingredient in zip(recipes, ingredients):
            for item in ingredient:
                graph[item].append(recipe)
                in_degree[recipe] += 1

        ans = []
        # only add supplier to initial queue
        queue = deque(supplies[::])
        while queue:
            node = queue.popleft()
            if node in recipes:
                ans.append(node)
            for neighbour in graph[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        return ans
