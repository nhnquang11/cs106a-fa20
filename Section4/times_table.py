def make_times_table(m, n):
    """
    Makes and returns a list of m rows, each with n columns. 
    Each element is found by multiplying its row number by 
    its column number, where we start counting rows and columns 
    from 1. 

    >>> make_times_table(3, 4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12]]
    """
    result = []
    for i in range(m):
        result.append([])
    for r in range(len(result)):
        for c in range(1, n+1):
            result[r].append((r+1)*c)
    return result
    