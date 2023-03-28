def matrix_constant_multiply(c, m):
    """
    Multiplies the 2-dimensional matrix m (represented as a list of lists) 
    by a constant factor c and returns the result. m should not be modified.

    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matrix_constant_multiply(2, matrix)
    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
    """
    for row in m:
        for i in range(len(row)):
            row[i] *= c
    return m

def matrix_add(m1, m2):
    """
    Adds matrices m1 and m2 together and returns the result. m1 and m2 are 
    guaranteed to be the same size. Neither m1 nor m2 should be modified.

    >>> m1 = [[1, 2], [3, 4], [5, 6]]
    >>> m2 = [[2, 3], [4, 5], [6, 7]]
    >>> matrix_add(m1, m2)
    [[3, 5], [7, 9], [11, 13]]
    """
    m = []
    for i in range(len(m1)):
        m.append([])
    for r in range(len(m1)):
        for c in range(len(m1[0])):
            m[r].append(m1[r][c] + m2[r][c])
    return m