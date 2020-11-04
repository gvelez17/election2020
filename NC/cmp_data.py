"""
load the results file for NC
compare to the registration file for NC
"""

import pandas as pd
import os
import re

RESULTS_FILE = '/edata/NC/results_pct_20201103.txt'

df = pd.read_csv(RESULTS_FILE, sep='\t')

pf = df.loc[df['Contest Name'] == 'US PRESIDENT']
#sf = df[df['Contest Name'] == 'US SENATE']
gf = df.loc[df['Contest Name'] == 'NC GOVERNOR']

# we want to compare these precinct numbers vs the turnout numbers
pf[pf['Choice'] == 'Donald J. Trump']['Total Votes']
pf[pf['Choice'] == 'Joseph R. Biden']['Total Votes']


# we don't have the turnout data from 2020

# Try comparing with the governor's race
mf = pf.merge(gf, on=['County','Precinct'], how='outer')

mf_dems = mf.loc[(mf['Choice Party_x'] == 'DEM') & (mf['Choice Party_y'] == 'DEM')]
mf_dems['ratio'] = mf_dems['Total Votes_x']/mf_dems['Total Votes_y']

mf_reps = mf.loc[(mf['Choice Party_x'] == 'REP') & (mf['Choice Party_y'] == 'REP')]
mf_reps['ratio'] = mf_reps['Total Votes_x']/mf_reps['Total Votes_y']

import pdb; pdb.set_trace()

# we do have older turnout data 
OLD_REG_FILE = '/edata/NC/ncvhis_Statewide.txt'
rf = pd.read_csv(OLD_REG_FILE, sep='\t')

