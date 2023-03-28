"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""

THRESHOLD = 3.5

def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    men, men_high, women, women_high = 0, 0, 0, 0
    with open(filename) as file:
        next(file)
        for line in file:
            data = line.split(',')
            if data[1] == 'W':
                women += 1
                if float(data[0]) > THRESHOLD:
                    women_high += 1
            else:
                men += 1
                if float(data[0]) > THRESHOLD:
                    men_high += 1
    men_pct_high = round(men_high / men * 100)
    women_pct_high = round(women_high / women * 100)
    print(f"{women_pct_high}% of reviews for women in the dataset are high.")
    print(f"{men_pct_high}% of reviews for men in the dataset are high.")

def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)

if __name__ == '__main__':
    main()