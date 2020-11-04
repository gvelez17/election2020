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

af = pd.DataFrame()
for filename in os.listdir(DATA_DIR):
    if re.search('FVE', filename):
        df = pd.read_csv("{}/{}".format(DATA_DIR, filename), names=headers, sep='\t')
        af = af.append(df[df.duplicated(['first_name', 'last_name','dob'], keep=False)].sort_values(['last_name','first_name','suffix','house_number','street_name'])[['voter_ID_number','last_name','first_name','middle_name','suffix','dob','date_registered','house_number','street_name','city','party']])

af.to_csv('first_last_only_dupes.csv')
import pdb; pdb.set_trace()

