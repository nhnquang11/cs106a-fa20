def first_list(strs):
    """
    Given a list of strings, create and return a dictionary whose 
    keys are the unique first characters of the strings and whose 
    values are lists of words beginning with those characters, in 
    the same order that they appear in strs.

    >>> first_list(['banter', 'brahm', 'aardvark', 'python', 'antiquated'])
    {'b': ['banter', 'brahm'], 'a': ['aardvark', 'antiquated'], 'p': ['python']}
    """
    first = dict()
    for word in strs:
        if not first.get(word[0]):
            first[word[0]] = []
        first[word[0]].append(word)
    return first
