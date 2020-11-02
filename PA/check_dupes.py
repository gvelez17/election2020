"""
For each county in PA, check for dupes in the voter registration records
"""

import pandas as pd
import os
import re

DATA_DIR = '/edata/PA'

HEADER_FILE = '/edata/PA/headers.txt'

with open(HEADER_FILE, 'r') as file:
    headers = file.read().split(',')

for filename in os.listdir(DATA_DIR):
    if re.search('FVE', filename):
        df = pd.read_csv("{}/{}".format(DATA_DIR, filename), names=headers, sep='\t')
        import pdb; pdb.set_trace()

