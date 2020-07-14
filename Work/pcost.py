# pcost.py
#
# Exercise 1.27
file = open('Data/portfolio.csv', 'rt')
# skip headers
headers = next(file)
total_cost = 0.0
# iterate through the file
for line in file:
    values = line.split(',')
    total_cost += (int(values[1]) * float(values[2]))
file.close()
print('Total cost ', total_cost)
