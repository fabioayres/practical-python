# pcost.py
def portfolio_cost(filename):
    stock_sum = 0
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            try:
                shares = int(row[1])
                price = float(row[2])
                stock_sum += shares*price
            except ValueError:
                print('Missing value!', line)
        
        return stock_sum
    
cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
# Exercise 1.27
