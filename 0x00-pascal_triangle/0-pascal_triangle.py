#!/usr/bin/python3
"""
Pascal's Triangle Generator
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle with 'n' rows.
    Returns a list of lists containing values of each row.
    """
    triangle = []
    if n > 0:
        for row in range(n):
            current_row = []
            value = 1
            for position in range(row + 1):
                current_row.append(value)
                value = value * (row - position) // (position + 1)
            triangle.append(current_row)
    return triangle
