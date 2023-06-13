# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowsAndCols = {}
        numberOfPairs = 0

        for i in range(len(grid)):
            cur_row = ' '.join(map(str, grid[i]))
            if cur_row in rowsAndCols:
                rowsAndCols[cur_row][0] += 1
            else:
                rowsAndCols[cur_row] = [1, 0]

            cur_col_list = []
            for j in range(len(grid)):
                cur_col_list.append(grid[j][i])

            cur_col = ' '.join(map(str, cur_col_list))
            if cur_col in rowsAndCols:
                rowsAndCols[cur_col][1] += 1
            else:
                rowsAndCols[cur_col] = [0, 1]

        for _, v in rowsAndCols.items():
            numberOfPairs += v[0] * v[1]

        return numberOfPairs
