# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    'Determine cost to buy portfolio'
    with open(filename) as file:
        total_cost = 0.0
        # skip headers
        next(file)
        for line in file:
            values = line.split(',')
            total_cost += (int(values[1]) * float(values[2]))
    return total_cost


total_cost = portfolio_cost('Data/portfolio.csv')
print("Total cost ", total_cost)
