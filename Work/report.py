# report.py
import csv
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(lines)
        for line in lines:
            row = (line[0], int(line[1]), float(line[2]))
            portfolio.append(row)
            
    return portfolio
# Exercise 2.4
