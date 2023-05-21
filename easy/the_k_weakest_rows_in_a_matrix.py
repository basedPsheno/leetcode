# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strongs = {}
        i = 0
        for row in mat:
            strongs[i] = 0
            for el in row:
                strongs[i] += el
            i += 1
        strongs = dict(sorted(strongs.items(), key=lambda item: item[1]))
        strongs = list(tuple(strongs)[:k])
        return strongs
