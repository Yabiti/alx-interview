#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    for i in range(n):
        triangle.append([])
    for i in range(n):
        for j in range(i+1):
            if j < i:
                if j == 0:
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i-1][j] + triangle[i-1][j-1])
            if i == j:
                triangle[i].append(1)
    return triangle
