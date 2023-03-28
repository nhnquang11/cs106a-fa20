"""
File: test_simulator.py
-----------------------
This program simulates the medical test based on the number of people,
test accuracy and infection rate of the disease.
"""

import random

def simulate_tests(num_people, test_accuracy, infection_rate):
    """
    num_people: the number of people getting the test
    test_accuracy: how accurate the test is
    infection_rate: the proportion of the population with the disease
    """
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0

    for i in range(num_people):
        correct_diagnosis = random.random() <= test_accuracy
        infected = random.random() <= infection_rate
        if correct_diagnosis and infected:
            true_positives += 1
        elif correct_diagnosis and not infected:
            true_negatives += 1
        elif not correct_diagnosis and not infected:
            false_positives += 1
        else:
            false_negatives += 1

    print(f"True positives: {true_positives}")
    print(f"False positives: {false_positives}")
    print(f"False negatives: {false_negatives}")
    print(f"True negatives: {true_negatives}")

    incorrect_positives_pct = false_positives / (false_positives + true_positives)
    print(f"{incorrect_positives_pct * 100}% of positive tests were incorrect")


def main():
    num_people = int(input("Number of people: "))
    test_accuracy = float(input("Test accuracy: "))
    infection_rate = float(input("Infection rate: "))
    simulate_tests(num_people, test_accuracy, infection_rate)

if __name__ == "__main__":
    main()
