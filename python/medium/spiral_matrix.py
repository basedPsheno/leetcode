# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        curDir = 'r'
        spiral = []
        m, n = len(matrix), len(matrix[0])
        km = m * n
        k = 1
        i, j = 0, 0

        while k <= km:
            spiral.append(matrix[i][j])
            matrix[i][j] = 101

            if (j == n - 1 or matrix[i][j + 1] == 101) and curDir == 'r':
                curDir = 'd'
            if (i == m - 1 or matrix[i + 1][j] == 101) and curDir == 'd':
                curDir = 'l'
            if (j == 0 or matrix[i][j - 1] == 101) and curDir == 'l':
                curDir = 'u'
            if (i == 0 or matrix[i - 1][j] == 101) and curDir == 'u':
                curDir = 'r'
                
            match curDir:
                case 'r': j += 1
                case 'd': i += 1
                case 'l': j -= 1
                case 'u': i -= 1

            k += 1

        return spiral

