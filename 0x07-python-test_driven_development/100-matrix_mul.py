#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Perform matrix multiplication on two matrices.

    Args:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Returns:
    - list of lists: The result of matrix multiplication.

    Raises:
    - TypeError: If m_a or m_b is not a list, not a list of lists, empty, or contains non-integer/float values.
    - ValueError: If m_a and m_b cannot be multiplied due to incompatible shapes.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    num_cols_m_a = len(m_a[0])
    num_cols_m_b = len(m_b[0])

    if not all(len(row) == num_cols_m_a for row in m_a) or not all(len(row) == num_cols_m_b for row in m_b):
        raise TypeError("Each row of m_a must be of the same size or each row of m_b must be of the same size")

    if not all(isinstance(value, (int, float)) for row in m_a for value in row) or \
            not all(isinstance(value, (int, float)) for row in m_b for value in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if num_cols_m_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[0 for _ in range(num_cols_m_b)] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(num_cols_m_b):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
