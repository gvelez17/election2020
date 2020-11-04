"""
load the results file for NC
compare to the registration file for NC
"""

import pandas as pd
import os
import re

RESULTS_FILE = '/edata/NC/results_pct_20201103.txt'

df = pd.read_csv(RESULTS_FILE, sep='\t')

pf = df[df['Contest Name'] == 'US PRESIDENT']
sf = df[df['Contest Name'] == 'US SENATE']

# we want to compare these precinct numbers vs the turnout numbers
pf[pf['Choice'] == 'Donald J. Trump']['Total Votes']
pf[pf['Choice'] == 'Joseph R. Biden']['Total Votes']

# we don't have the turnout data from 2020

# we do have older turnout data 
OLD_REG_FILE = '/edata/NC/ncvhis_Statewide.txt'
rf = pd.read_csv(OLD_REG_FILE, sep='\t')

import pdb; pdb.set_trace()
