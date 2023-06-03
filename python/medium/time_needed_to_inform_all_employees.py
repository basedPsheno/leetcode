# https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        company = {}

        for i in range(n):
            if manager[i] in company:
                company[manager[i]].append(i)
            else:
                company[manager[i]] = [i]

        def DFS(ID: int, time: int) -> int:
            time += informTime[ID]
            if ID in company:
                sub_time = []
                for sub in company[ID]:
                    sub_time.append(DFS(sub, 0))
                time += max(sub_time)
            return time

        return DFS(headID, 0)
