'''

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
'''
def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    if not (matrix and matrix[0]):
        return matrix
    
    m = len(matrix)
    n = len(matrix[0])
    
    zeros = [0 for _ in range(m+n)]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zeros[i] = 1
                zeros[m + j] = 1
    
    for i in range(len(zeros)):
        if zeros[i] == 1:
            if i < m:
                for j in range(n):
                    matrix[i][j] = 0
            else:
                for j in range(m):
                    matrix[j][i - m] = 0