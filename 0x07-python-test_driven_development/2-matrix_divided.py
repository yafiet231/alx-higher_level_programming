How to Use 2-matrix_divided.py
==============================

This module defines a matrix division function ``matrix_divided(matrix, div)``.

Usage
=====

``matrix_divided(...)`` returns a new matrix that is a copy of the parameter
``matrix`` with all elements divided by ``div``.

::

    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided
    >>> matrix = [
    ...     [3, 6, 9],
    ...     [12, 15, 18]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

Note that quotients are rounded to a maximum of two decimal places.

::

    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

The original matrix is left unchanged.

::

    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]

The function can also handle floating-point numbers.

::

    >>> matrix = [
    ...     [1.1, -2.2, 3.3],
    ...     [4.4, 5.5, -6.6]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[0.37, -0.73, 1.1], [1.47, 1.83, -2.2]]

Integers and floats can be combined.

::

    >>> matrix = [
    ...     [1, -2.2, 3, 4.4, 5],
    ...     [-6.6, 7.00, 8, 9.999, 10]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, -0.73, 1.0, 1.47, 1.67], [-2.2, 2.33, 2.67, 3.33, 3.33]]


