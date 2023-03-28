def map_students_to_dorms(all_housing_assignments):
    """
    Given a list of length-2 tuples whose first elements are student
    names and whose second elements are dorm names, create and return 
    a dictionary which associates each student with a list of all the 
    dorms they lived in throughout their time at Stanford. 

    all_housing_assignments contains information about undergraduates 
    in every year, so some students might only have one residence whilst 
    others might have multiple.
    """
    d = {}
    for name, dorm in all_housing_assignments:
        if name not in d:
            d[name] = []
        d[name].append(dorm)
    return d 

def main():
    all_housing_assignments = [
        ("Brahm", "Larkin"), 
        ("Brahm", "Roble"),
        ("Brahm", "Mirrielees"),
        ("Brahm", "Mars"), 
        ("Brahm", "Jerry"),
        ("Chris", "FroSoCo"),
        ("Chris", "Kimball"),
        ("Chris", "Toyon"),
        ("Chris", "Roble"),
        ("Mehran", "Paloma"),
        ("Mehran", "Roble"),
        ("Mehran", "Loro"),
        ("Mehran", "Soto")
    ]
    print(map_students_to_dorms(all_housing_assignments))

if __name__ == "__main__":
    main()
