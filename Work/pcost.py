# pcost.py
def portfolio_cost(filename):
    stock_sum = 0
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            stock_sum += int(row[1])*float(row[2])
        
        return stock_sum
    
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
# Exercise 1.27
