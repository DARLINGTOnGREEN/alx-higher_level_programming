#!/usr/bin/python3
"""Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """Return the matrix resulting from
    the multiplication of m_a and m_b."""

    # Check for correct types of inputs
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if matrices are empty
    if not m_a or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not m_b or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if all elements are integers or floats
    if not all(
        all(isinstance(element, (int, float)) for element in row) for row in m_a
    ):
        raise TypeError("m_a should contain only integers or floats")
    if not all(
        all(isinstance(element, (int, float)) for element in row) for row in m_b
    ):
        raise TypeError("m_b should contain only integers or floats")

    # Check if each row in m_a and m_b is of the same size
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrix dimensions are compatible for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize result matrix
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
