def encrypt(plaintext):
    """
    Takes in plaintext as an input and returns 'ciphertext': the result 
    of substituting each letter in the plaintext by its corresponding 
    encrypted character in ENCRYPTION_DICT. 

    The plaintext comprises entirely of uppercase letters and non-alphabetic 
    characters like punctuation. Non-alphabetic characters needn't be encrypted, 
    but rather should appear in the plaintext in their original form. 

    >>> encrypt("HEY, HOW'S IT GOING?")
    "KUD, KXZ'S BV CXBFC?"
    >>> encrypt("I LOVE CS 106A!")
    'B WXLU ES 106T!'
    >>> encrypt("UNICORNS ARE THE MOST BEAUTIFUL ANIMALS IN EXISTENCE")
    'AFBEXPFS TPU VKU NXSV HUTAVBIAW TFBNTWS BF UYBSVUFEU'
    """
    ciphertext = ''
    for c in plaintext:
        ciphertext += ENCRYPTION_DICT[c]
    return ciphertext

def decrypt(ciphertext):
    """
    Uses ENCRYPTION_DICT to decrypt each of the alphabetic characters of
    ciphertext.

    >>> decrypt("KUD, KXZ'S BV CXBFC?")
    "HEY, HOW'S IT GOING?"
    >>> decrypt('B WXLU ES 106T!')
    'I LOVE CS 106A!'
    >>> decrypt('AFBEXPFS TPU VKU NXSV HUTAVBIAW TFBNTWS BF UYBSVUFEU')
    'UNICORNS ARE THE MOST BEAUTIFUL ANIMALS IN EXISTENCE'
    """
    plaintext = ''
    reverse_encyption_dict = create_reverse_encyption_dict()
    for c in ciphertext:
        plaintext += reverse_encyption_dict[c]
    return plaintext

def create_reverse_encyption_dict():
    """
    This helper function returns a dictionary that is the reverse of
    ENCRYPTION_DICT (keys and values are swapped).
    """
    reversed_dict = dict()
    for key, value in ENCRYPTION_DICT.items():
        reversed_dict[value] = key
    return reversed_dict
    