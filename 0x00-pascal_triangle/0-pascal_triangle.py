#!/usr/bin/python3
'''A module for Pascal's triangle'''


def pascal_triangle(n):
    '''
    Generates Pascal's Triangle up to a given number of rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of list of int: A list of lists where each inner list
        represents a row in Pascal's Triangle.
        If the input is not a positive integer, an empty list is returned.
    '''

    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle

    for row_index in range(n):
        current_row = []
        for col_index in range(row_index + 1):
            if col_index == 0 or col_index == row_index:
                current_row.append(1)
            else:
                current_row.append(
                    triangle[row_index - 1][col_index - 1] +
                    triangle[row_index - 1][col_index]
                )
        triangle.append(current_row)

    return triangle
