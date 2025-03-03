# report.py
import csv
from pprint import pprint
def read_prices(filename):
     prices = {}
     with open(filename, 'rt') as f:
        lines = csv.reader(f)
        next(f)
        for line in lines:
            try:   
                prices[line[0]] = float(line[1])
            except IndexError:
                print('Value missing!')
            print(line)
        
        return prices




def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        lines = csv.reader(f)
        headers = next(lines)
        for line in lines:
            record = dict(zip(headers,line))
            holding={
                'name': record['name'],
                'share' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(holding)
            
    return portfolio


def make_report(portfolio, prices):
    report=[]
    for holding in portfolio:
        if holding['name'] in prices:
            change = holding['price'] - prices[holding['name']]
            report_line =(holding['name'], holding['share'], holding['price'], change) 
            report.append(report_line)
        else:
            print('{name} not in prices'.format_map(holding))
    return report

def read_report (report):
    headers = ('Name','Shares','Price','Change')
    for word in headers:
        print(f'{word:>10s}', end=' ')

    print('')

    for word in headers:
        print(10*'-', end =' ')
    
    print('')

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')