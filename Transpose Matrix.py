class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(matrix), len(matrix[0])
        res = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                res[j][i] = matrix[i][j]
        return res
matrix=eval(input("enter your matrix:"))
solution=Solution()
print(solution.transpose(matrix))