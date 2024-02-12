#!/usr/bin/python3
"""

Module with a function that divides all elements of a matrix

"""
import copy


def matrix_divided(matrix, div):
    """

    Divides all elements of a matrix

    Args:
    matrix (list): a list of list of integers or floats
    div (integer or float): the divisor for matrix elements

    Returns:
    a new matrix

    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = copy.deepcopy(matrix)

    for i in range(len(result)):
        if not isinstance(result[i][j], int) \
                and not isinstance(result[i][j], float):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        for j in range(len(result[i])):
            if not isinstance(result[i][j], int) \
                    and not isinstance(result[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

                result[i][j] = round(result[i][j] / div, 2)

    return result
