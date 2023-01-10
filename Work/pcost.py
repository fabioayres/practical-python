# pcost.py
stock_sum = 0
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        stock_sum += int(row[1])*float(row[2])
    
    print(f'Total cost: {stock_sum}')

# Exercise 1.27
