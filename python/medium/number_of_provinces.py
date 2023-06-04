# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        prov = 0
        visited = [False] * n

        def dfs(node: int):
            visited[node] = True
            for neighbor in range(n):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for i in range(n):
            if not visited[i]:
                prov += 1
                dfs(i)

        return prov
