"""
For each county in PA, check for dupes in the voter registration records
"""

import pandas as pd
import os
import re

DATA_DIR = '/edata/PA'

HEADER_FILE = '/edata/PA/headers.txt'

sample = ['/edata/PA/WESTMORELAND FVE 20201019.txt',]

with open(HEADER_FILE, 'r') as file:
    headers = file.read().split(',')

af = pd.DataFrame(columns=['precinct_code', 'reg_40_ratio_R', 'reg_40_ratio_D', 'reg_39_ratio_R', 'reg_39_ratio_D', '2020_ratio'])
for filename in os.listdir(DATA_DIR):
  try:
    if re.search('FVE', filename):
        df = pd.read_csv("{}/{}".format(DATA_DIR, filename), names=headers, sep='\t')

        for name, group in df.groupby('precinct_code'):
            row = {}
            row['precinct_code'] = name
            elect40_R = (group.elect40_party == 'R').sum()
            elect40_D = (group.elect40_party == 'D').sum()
            elect39_R = (group.elect39_party == 'R').sum() 
            elect39_D = (group.elect39_party == 'D').sum()
            row['reg_40_ratio_R'] = (group.party == 'R').sum() / elect40_R if elect40_R else None
            row['reg_40_ratio_D'] = (group.party == 'D').sum() / elect40_D if elect40_D else None
            row['reg_39_ratio_R'] = (group.party == 'R').sum() / elect39_R if elect39_R else None
            row['reg_39_ratio_D'] = (group.party == 'D').sum() / elect39_D if elect39_D else None
            row['2020_ratio'] = (pd.to_datetime(group.date_registered).dt.year == 2020).sum() / (len(group) or 1)
            row['precinct_tot'] = len(group)
            row['county'] = group.county.unique()[0]
            af = af.append(row, ignore_index=True)

        # drop rows with invalid precinct codes
        af = af[~af.precinct_code.astype('str').str.contains('/')]
        af['precinct_code'] = af.precinct_code.astype('int64')
        af['precinct_tot'] = af.precinct_tot.astype('int64')
  except Exception as e:
    print("ERROR: {}".format(str(e)))
    af.to_csv('partial_stats.csv')
    print("**** ERROR PROCESSING FILE {} ****".format(filename))
    
af.to_csv('stats.csv')

# sample of looking for extremes of things

pick = pd.DataFrame(af.loc[(af.precinct_tot > 100) & ~af.reg_40_ratio_R.isnull() & ~af.reg_40_ratio_D.isnull()])

pick['dr_ratio'] = pick.reg_40_ratio_R / pick.reg_40_ratio_D

pick.sort_values('dr_ratio')

af[af.precinct_tot > 100].sort_values('2020_ratio')
