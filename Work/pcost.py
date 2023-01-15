# pcost.py
import csv
def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        headers = next(lines)
        print(headers)
        for lineno, line in enumerate (lines, start=1):    
            record = dict(zip(headers,line))     
            try:
                row = {
                    'name': record['name'], 
                    'share': int(record['shares']),
                    'price': float(record['price'])
                    }
                cost += row['share']*row['price']
            except ValueError:
                print(f'Could not convert line {lineno}: {line}')
        
        return cost

# portfolio_cost('Data/portfolio.csv')   s 
cost = portfolio_cost('Data/missing.csv')
print('Total cost:', cost)
# Exercise 1.27
