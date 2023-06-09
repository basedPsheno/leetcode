# https://leetcode.com/problems/sum-of-matrix-after-queries/

class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        seenRows, seenCols, sumMatrix = 0, 0, 0
        rows, cols = [True] * n, [True] * n

        for query in reversed(queries):
            if query[0] == 0 and rows[query[1]]:
                seenRows += 1
                rows[query[1]] = False
                sumMatrix += (n - seenCols) * query[2]

            if query[0] == 1 and cols[query[1]]:
                seenCols += 1
                cols[query[1]] = False
                sumMatrix += (n - seenRows) * query[2]
        
        return sumMatrix
