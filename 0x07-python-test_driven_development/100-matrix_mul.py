#!/usr/bin/python3
"""
matrix_mul module
This module miltiplies 2 matrices, this matrices must be a
list of lists of integers or floats.
Otherwise raise a TypeError or ValueError exception with custom error messages.
"""
def matrix_mul(m_a, m_b):
    """
    Arguments:
    @m_a: matriz 1
    @m_b: matriz 2
    
    Returns:
    in the successful case, the result of the multiplication
    
    Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    for r in range(len(m_a)):
        if type(m_a[r]) != list:
            raise TypeError("m_a must be a list of lists")

    for r in range(len(m_b)):
        if type(m_b[r]) != list:
            raise TypeError("m_b must be a list of lists")

    for r in range(len(m_a)):
        for c in range(len(m_a[r])):
            if type(m_a[r][c]) != int and type(m_a[r][c]) != float:
                raise TypeError("m_a should contain only integers or floats")

    ty_err = "m_b should contain only integers or floats"
    for r in range(len(m_b)):
            for c in range(len(m_b[r])):
                if type(m_b[r][c]) != int and type(m_b[r][c]) != float:
                    raise TypeError(ty_err)

    for row in range(len(m_a)):
        if row > 0:
            if len(m_a[row]) != len(m_a[row - 1]):
                raise TypeError("each row of m_a must be of the same size")

    for row in range(len(m_b)):
        if row > 0:
            if len(m_b[row]) != len(m_b[row - 1]):
                raise TypeError("each row of m_b must be of the same size")

    A = m_a
    B = m_b
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        raise ValueError("m_a and m_b can't be multiplied")

    """ Create the result matrix
        Dimensions would be rows_A x cols_B
    """
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C
