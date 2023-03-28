"""
File: contract_tracing.py
-------------------------

Uses the information in locations.txt to get a list of everyone that came in
contact with the target throughout the day.
"""

TARGET = 'Rosalind'
LOCATION_FILE = 'locations.txt'


def find_contacts(target, location_file):
    """
    Computes and returns a list of people that the target came in contact with
    by processing the location file.

    Arguments
    ---------
    target (str) -- The name of the person to compare everyone against.
    location_file (str) -- The name of the file that contains the location
        information for people throughout the day.
    
    Doctests
    --------
    >>> find_contacts('Parth', 'locations.txt')
    ['Leonida', 'Vashti', 'Alexis', 'Salvador', 'Elnora', 'Brahm', 'Cecily', 'Misty', 'Serina', 'Eddy', 'Jesusa', 'Deidre', 'Blondell', 'Yuonne', 'Forest', 'Russell', 'Sheilah', 'Kai', 'Tori', 'Hayley', 'Sebrina', 'Henry', 'Etta', 'Lia', 'Particia', 'Elena', 'Leanna', 'Latrisha', 'Juliette', 'Chuck', 'Eboni', 'Glennie', 'Stacee', 'Rosalind', 'Neva', 'Lona', 'Blake', 'Mehran', 'Jolyn', 'Kathe', 'Monserrate', 'Tabitha', 'Buford', 'Lacy', 'Meggan', 'Reita', 'Parth', 'Jolie', 'Marisela', 'Jeri']
    >>> find_contacts('Kara', 'locations.txt')
    ['Leonida', 'Elnora', 'Brahm', 'Barabara', 'Garrett', 'Kenyatta', 'Wade', 'Nakia', 'Lashay', 'Blondell', 'Lou', 'Devora', 'Pia', 'Kai', 'Hayley', 'Etta', 'Particia', 'Chris', 'Latoya', 'Juliette', 'Ina', 'Chuck', 'Will', 'Peter', 'Johnny', 'Kara', 'Lilia', 'Eboni', 'Stacee', 'Delmy', 'Rosalind', 'Refugia', 'Blake', 'Buddy', 'Kathe', 'Angelyn', 'Tabitha', 'Mauricio', 'Madelyn', 'Kylie', 'Trinity', 'Bradley', 'Jolie', 'Sylvia', 'Marisela']
    """
    location_dict = parse_location_data(location_file)
    contacts = []
    for name in location_dict:
        if in_contact(location_dict[name], location_dict[target]):
            contacts.append(name)
    return contacts

def in_contact(name, target):
    for time in name:
        if time in target and name[time] == target[time]:
            return True
    return False

def parse_location_data(location_file):
    location_dict = {}
    with open(location_file) as f:
        for line in f:
            data = [x.strip() for x in line.split(',')]
            name = data[0]
            time = data[1]
            location = data[2]
            if name not in location_dict:
                location_dict[name] = {}
            location_dict[name][time] = location 
    return location_dict

def main():
    print(find_contacts(TARGET, LOCATION_FILE))


if __name__ == '__main__':
    main()