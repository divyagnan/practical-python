# bounce.py
#
# Exercise 1.5

current_height = 100
rebound_value = 3/5
num_bounces = 10

for i in range(num_bounces):
    current_height *= rebound_value
    # add 1 to the day since we are zero indexed
    print(i + 1, round(current_height, 4))
