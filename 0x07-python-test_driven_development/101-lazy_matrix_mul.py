#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using matmul, and returns the result.
    """
    if not isinstance(m_a, (list, np.ndarray)) or not isinstance(m_b, (list, np.ndarray)):
        raise ValueError("Inputs must be lists or numpy arrays")

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    if m_a.ndim != 2 or m_b.ndim != 2:
        raise ValueError("Inputs must be 2-dimensional")

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError(e)
