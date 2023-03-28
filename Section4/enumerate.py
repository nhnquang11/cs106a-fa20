def enumerate(lst):
    """
    returns a nested list where each element is a list containing 
    the index of an element in the original list and the element itself. 
    These lists should appear in increasing order of indices.

    >>> enumerate(['cs106a', 'is', 'super', 'fun'])
    [[0, 'cs106a'], [1, 'is'], [2, 'super'], [3, 'fun']]
    >>> enumerate(['hello'])
    [[0, 'hello']]
    >>> enumerate([])
    []
    """
    return [[i, lst[i]] for i in range(len(lst))]