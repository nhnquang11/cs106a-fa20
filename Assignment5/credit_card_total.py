"""
File: credit_card_total.py
--------------------------
This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""


INPUT_FILE = 'bill2.txt'

def main():
    expenses = dict()
    with open(INPUT_FILE) as bill:
        for data in bill:
            store = data[data.find('[')+1:data.find(']')]
            expense = int(data[data.find('$')+1:])
            if not expenses.get(store):
                expenses[store] = 0
            expenses[store] += expense
    display_expenses(expenses)

def display_expenses(expenses):
    for store in expenses:
        print(f"{store}: ${expenses[store]}")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
