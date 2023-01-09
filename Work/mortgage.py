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
    month += 1
    if month <= extra_payment_end_month and month >= extra_payment_start_month:
        payment = extra_payment
    else:
        payment = 2684.11
    
    if  principal * (1+rate/12) - payment <= 0:
        payment = principal * (1+rate/12)

    principal = principal * (1+rate/12) - payment

    total_paid = total_paid + payment        

    print(f'{month:<4} {round(total_paid,2):^10} {round(principal,2)}')
    

print(f'Total paid {round(total_paid, 2)}.')
print(f'Months {month}')
# Exercise 1.7
