"""
For each county in PA, check for dupes in the voter registration records
"""

import pandas as pd
import os
import re

DATA_DIR = '/home/ubuntu/edata/PA'

HEADER_FILE = '/home/ubuntu/edata/PA/header.txt'

with open(HEADER_FILE, 'r') as file:
    headers = file.read().split(',')

for filename in os.listdir(DATA_DIR):
    if re.search('FVE', filename):
        df = pd.read_csv(filename, names=headers)
        import pdb; pdb.set_trace()

