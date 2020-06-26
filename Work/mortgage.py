# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
current_month = 0

while principal > 0:
    current_month += 1
    total_payment = payment
    if (current_month >= extra_payment_start_month and current_month <= extra_payment_end_month):
        total_payment += extra_payment
    principal = principal * (1 + rate / 12) - total_payment
    total_paid = total_paid + total_payment
    print(current_month, round(total_paid, 1), round(principal, 1))


print('Total Paid:', round(total_paid, 1))
print('Months:', current_month)
