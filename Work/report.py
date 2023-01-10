# report.py
import csv
from pprint import pprint
def read_prices(filename):
     portfolio = {}
     with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(f)
        for line in lines:
            try:   
                portfolio[line[0]] = float(line[1])
            except IndexError:
                print('Value missing!')
            print(line)
        
        return portfolio




def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for line in lines:
            holding={
                'name': line[0],
                'share' : int(line[1]),
                'price' : float(line[2])
            }
            portfolio.append(holding)
            
    return portfolio
# Exercise 2.4
