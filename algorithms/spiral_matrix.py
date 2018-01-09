class Solution:
    def spiralOrder(self, matrix):
        """
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        spiral = []
        i,j,di,dj = 0, 0, 0, 1
        for _ in range(rows*cols):
            spiral.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i+di)%rows][(j+dj)%cols] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return spiral

                
        

assert Solution().spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]) == [1,2,3,6,9,8,7,4,5]

assert Solution().spiralOrder([[2,3]]) == [2,3]