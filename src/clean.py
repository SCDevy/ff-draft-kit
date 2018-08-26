# clean.py
# strips out numbers from football positions i.e. WR7 -> WR, etc

import csv

KEY_INDEX = 3
POSITIONS = ['QB', 'RB', 'WR', 'TE', 'K', 'DST']

MASTER_CSV = 'data/2018-08-25-adp-fp-espn.csv'
RESULTS_CSV = 'results/2018-08-25-adp-fp-espn-CLEAN.csv'

with open(MASTER_CSV, 'r') as master:
    with open(RESULTS_CSV, 'w') as results:    
        reader = csv.reader(master)
        writer = csv.writer(results)

        for row in reader:
            for pos in POSITIONS:
                if pos in row[3]:
                    row[3] = pos

            writer.writerow(row)