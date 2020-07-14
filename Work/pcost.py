# pcost.py
#
# Exercise 1.27
import csv


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


total_cost = portfolio_cost('Data/portfolio.csv')
print("Total cost ", total_cost)
