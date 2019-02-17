import MatrixProcessing
import Determinant
print('Input the size of matrix: ')
n = int(input())
matrix = MatrixProcessing.input_matrix([], n)
MatrixProcessing.output_matrix(matrix)
print('Determinant: ', Determinant.amount_determinant(matrix))



