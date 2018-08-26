# merge.py
# takes a candidate CSV with two columns [key, value] and merges it to a master CSV [key, ...]

import csv
import datetime

KEY_INDEX = 0

MASTER_CSV = 'data/2018-08-25-adp-fp-espn.csv'
CANDIDATE_CSV = 'data/2018-08-25-boris.csv'
RESULTS_CSV = 'results/' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') + '-combined.csv'

with open(CANDIDATE_CSV, 'r') as candidate:
    candidate_indices = dict((r[KEY_INDEX], i) for i, r in enumerate(csv.reader(candidate)))

with open(MASTER_CSV, 'r') as master:
    with open(RESULTS_CSV, 'w') as results:    
        reader = csv.reader(master)
        writer = csv.writer(results)

        writer.writerow(next(reader, []) + ['BORIS'])

        for row in reader:
            match = candidate_indices.get(row[KEY_INDEX])

            if match is not None:
                value = match
            else:
                value = ''

            writer.writerow(row + [value])
