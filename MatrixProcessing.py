from __future__ import print_function


def input_matrix(a, n):
    print('Input the matrix (each number from a new line)')
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(float(input()))
    return a


def output_matrix(a):
    print('The matrix:')
    for i in a:
        for j in i:
            print(j, end=' ')
        print('\n', end='')

