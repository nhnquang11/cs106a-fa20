SAMPLE_INPUT = {
    'Alice': ['Bob', 'Catherine'],
    'Daniel': ['Alice', 'Eve'],
    'Catherine': ['Frank'],
    'Eve': ['Grace']
}

def find_grandchildren(parents_dictionary):
    """
    >>> find_grandchildren(SAMPLE_INPUT)
    {'Alice': ['Frank'], 'Daniel': ['Bob', 'Catherine', 'Grace']}
    """
    d = {}
    for parent in parents_dictionary:
        grandchildren = []
        for child in parents_dictionary[parent]:
            if child in parents_dictionary:
                grandchildren.extend(parents_dictionary[child])
        if grandchildren:
            d[parent] = grandchildren
    return d
