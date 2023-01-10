# pcost.py
import csv
def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for line in lines:
            print(line)            
            try:
                row = {
                    'name': line[0], 
                    'share': int(line[1]), 
                    'price': float(line[2])
                    }
                cost += row['share']*row['price']
            except ValueError:
                print('Missing value!', line)
        
        return cost

portfolio_cost('Data/portfolio.csv')    
cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
# Exercise 1.27
