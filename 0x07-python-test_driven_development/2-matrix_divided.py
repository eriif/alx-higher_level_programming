#!/usr/bin/python3
"""this function divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
    matrix (list): A list of lists of ints or floats.
    div (int/float): The divisor.
    Raises:
    TypeError: If the matrix contains non-numbers.
    TypeError: If the matrix contains rows of different sizes.
    TypeError: If div is not an int or float.
    ZeroDivisionError: If div is 0.
    Returns:
    A new matrix representing the result of the division.
    """
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if not matrix or not matrix[0]:
        raise ValueError("matrix cannot be empty")

    for row in matrix:
        if not all(isinstance(col, (int, float)) for col in row):
            raise TypeError("matrix must contain only integers or floats")
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    rows_L = []
    for row in matrix:
        rows_L.append(len(row))
    if not all(col == rows_L[0] for col in rows_L):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]

    return (new_matrix)
