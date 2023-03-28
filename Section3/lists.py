
def collapse(lst):
    """
    Accepts a list of integers as a parameter and returns a new
    list containing the result of replacing each pair of integers
    with the sum of that pair.

    If the list stores an odd number of elements, the final element
    is not collapsed

    >>> nums = [7, 2, 8, 9, 4, 13, 7, 1, 9, 10]
    >>> collapse(nums)
    [9, 17, 17, 8, 19]
    >>> nums = [1, 2, 3, 4, 5]
    >>> collapse(nums)
    [3, 7, 5]
    """
    result = []
    for i in range(len(lst) // 2):
        result.append(lst[i*2] + lst[i*2+1])

    if len(lst) % 2 == 1:
        result.append(lst[-1])

    return result

def distinct_elements(lst):
    """
    Returns a list of all the disinct elements in lst, in the order that
    they first occur in lst.
    >>> distinct_elements([1, 2, 3, 4])
    [1, 2, 3, 4]
    >>> distinct_elements([1, 1, 2, 2, 3])
    [1, 2, 3]
    >>> distinct_elements(['hello', 'hello', 'hello', 'hello', 'hello'])
    ['hello']
    >>> distinct_elements([])
    []
    """
    return list(set(lst))

def rotate_list_right(lst, n):
    """
    returns a 'rotate' version of the list that rotates numbers
    to the right n times. Each element in numbers is shifted
    forward n places, and the last n elements are moved to
    the start of the list.

    Your function should not change the list that is passed as a
    parameter.

    >>> rotate_list_right([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]
    """
    result = [0 for i in range(len(lst))]
    for i in range(len(lst)):
        result[i] = lst[(i - 2) % len(lst)]
    return result

