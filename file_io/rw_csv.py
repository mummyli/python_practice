import csv
from collections import namedtuple

with open("./testfiles/stocks.csv") as f:
    # 默认逗号分隔， 也可以指定分隔符：csv.reader(f, delimiter='\t')
    f_csv = csv.reader(f)
    header = next(f_csv)
    for row in f_csv:
        print(row)

print ("\n", "-" * 100, "\n")

with open("./testfiles/stocks.csv") as f:
    f_csv = csv.reader(f)
    header = next(f_csv)
    Row = namedtuple("Row", header)

    for row in f_csv:
        r = Row(*row)
        print(r)

print ("\n", "-" * 100, "\n")


with open("./testfiles/stocks.csv") as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Symbol'])

print ("\n", "-" * 100, "\n")

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
        'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]

with open("./testfiles/stocks2.csv", "w") as f:
    f_csv = csv.DictWriter(f, header)
    f_csv.writeheader()
    f_csv.writerows(rows)
