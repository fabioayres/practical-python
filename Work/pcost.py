# pcost.py
import csv
def portfolio_cost(filename):
    stock_sum = 0
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for line in lines:
            print(line)            
            try:
                row = (line[0], int(line[1]), float(line[2]))
                stock_sum += row[1]*row[2]
            except ValueError:
                print('Missing value!', line)
        
        return stock_sum

portfolio_cost('Data/portfolio.csv')    
cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
# Exercise 1.27
