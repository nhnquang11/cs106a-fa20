"""
File: compute_interest.py
-------------------------
This program helps a user compute how much interest their bank account will accrue over time.
"""

def main():
    """
    Asks user for an intial account balance, starting year and month, 
    ending year and month, interest rate.
    Prints out monthly balance projection and 
    repeats asking user for new interest to calculate until hitting a 0.
    """
    initial_balance = float(input("Initial balance: "))
    start_year = int(input("Start year: "))
    start_month = int(input("Start month: "))
    end_year = int(input("End year: "))
    end_month = int(input("End month: "))
    if not is_valid_time(start_year, start_month, end_year, end_month):
        print("Starting date needs to be before the ending date.")
    else:
        interest_rate = float(input("Interest rate (0 to quit): "))

        while interest_rate != 0:   
            print_monthly_balance_projection(initial_balance, start_year, start_month, end_year, end_month, interest_rate)
            interest_rate = float(input("Interest rate (0 to quit): "))

def is_valid_time(start_year, start_month, end_year, end_month):
    """
    Checks if the start time is before the end time.
    """
    return not ((start_year > end_year) or (start_year == end_year and start_month > end_month))

def print_monthly_balance_projection(initial_balance, start_year, start_month, end_year, end_month, interest_rate):
    """
    Traverses through each month from start to end.
    Each step calculates and prints out the balance in that month.
    """
    current_year = start_year
    current_month = start_month
    num_months = 0
    while not (current_year == end_year and current_month == end_month):
        balance = calculate_balance(initial_balance, interest_rate, num_months)
        print(f"Year {current_year}, month {current_month} balance: {balance}")
        num_months += 1
        if current_month == 12:
            current_year += 1
            current_month = 1
        else:
            current_month += 1

    balance = calculate_balance(initial_balance, interest_rate, num_months)
    print(f"Year {current_year}, month {current_month} balance: {balance}")

def calculate_balance(initial_balance, interest_rate, num_months):
    return initial_balance * ((1 + interest_rate) ** num_months)

if __name__ == '__main__':
    main()
