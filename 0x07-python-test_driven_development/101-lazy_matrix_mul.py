#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    - m_a (list of lists): The first matrix.
    - m_b (list of lists): The second matrix.

    Returns:
    - numpy.ndarray: The result of matrix multiplication.

    Raises:
    - ValueError: If the matrices cannot be multiplied.
    """
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("Matrix shapes are not compatible for multiplication")

if __name__ == "__main__":
    m_a = [[1, 2], [3, 4]]
    m_b = [[2, 0], [1, 2]]
    print(lazy_matrix_mul(m_a, m_b)) 

    m_a = [[1, 2, 3], [4, 5, 6]]
    m_b = [[7, 8], [9, 10], [11, 12]]
    print(lazy_matrix_mul(m_a, m_b))
    
    m_a = [[1, 2], [3, 4]]
    m_b = [[5, 6], [7, 8], [9, 10]]
    try:
        print(lazy_matrix_mul(m_a, m_b))
    except ValueError as e:
        print(e)
