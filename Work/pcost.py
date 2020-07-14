# pcost.py
#
# Exercise 1.27
import csv
import sys


def portfolio_cost(filename):
    'Determine cost to buy portfolio'
    with open(filename) as file:
        total_cost = 0.0
        # use csv reader
        rows = csv.reader(file)
        # skip headers
        next(file)
        for row in rows:
            try:
                total_cost += (int(row[1]) * float(row[2]))
            except:
                print('Failed to parse, moving on...')
    return total_cost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

total_cost = portfolio_cost(filename)
print("Total cost ", total_cost)
