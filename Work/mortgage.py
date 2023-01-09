# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input('X pay start month? '))
extra_payment_end_month = int(input('X pay end month? '))
extra_payment = float(input('X pay amount? '))
extra_payment += 2684.11
print(extra_payment)

while principal > 0:
    if month < extra_payment_end_month and month >= extra_payment_start_month:
        payment = extra_payment
    else:
        payment = 2684.11 
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    month += 1

print(f'Total paid: {total_paid} over {month} months.')
# Exercise 1.7
