#!/usr/bin/python3
'''The function divides all elements in a matrix and rounded to 2 decimal places
Can be imported as its not executable directly
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix by a given divisor, div

    Args:
        matrix: the 2d array
        div: the divisor

    Returns:
        The result of the division

    Raises:
        TypeError: if not matrix (list of lists) of integers/floats
        TypeError: if div not integer or float
    ZeroDivisionError: if div equals zero
    '''
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
         raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    flag = 0

    for i in matrix:
        if not i or not isinstance(i, list)
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if flag != 0 and len(i) != flag:
            raise TypeError("Each row of the matrix must have the same size")

        for num in i:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        flag = len(i)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)
    return (m)
