class Solution(object):
    def setZeroes(self, matrix):
        row=set()
        column=set()
        for i in range(len(matrix)):
            for a in range(len(matrix[i])):
                if matrix[i][a] ==0:
                        row.add(i)
                        column.add(a)
        for i in range(len(matrix)):   
            for a in range(len(matrix[i])):
                if i in row or a in column:
                    matrix[i][a]=0
        return matrix