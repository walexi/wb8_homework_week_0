class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        sol = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                sol[c][r]=matrix[r][c]
#       
        return sol
    def solution2(self, matrix: List[List[int]]) -> List[List[int]]:
        
#       
        return zip(*matrix) # zip iterates through the rows in matrix, the asterisk unpacks the rows so each one is given

