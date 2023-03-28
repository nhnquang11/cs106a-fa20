def count_by_consonants(filename):
    """
    Reads in the file whose name is filename and returns a dictionary
    that contains counts of words that share the same consonants in order.
    """
    consonant_counter = dict()
    with open(filename) as file:
        for line in file:
            word = line.strip()
            consonant_only = make_consonant(word)
            if not consonant_counter.get(consonant_only):
                consonant_counter[consonant_only] = 0
            consonant_counter[consonant_only] += 1
    return consonant_counter


def make_consonant(word):
    """
    Returns a consonnant version of the given word.
    """
    consonant_only = ''
    for char in word:
        if char not in 'aeiouy':
            consonant_only += char
    return consonant_only

def main():
    filename = 'consonants.txt'
    print(count_by_consonants(filename))

if __name__ == '__main__':
    main()
