"""
load the results file for GA
compare to the registration file for GA or to 2016 results
For GA this has to be done per county

Data files also need to be pre-processed, as they are in a mixed format with headers in between sections of fixed-field-length data

Generally the headers will be

['County', 'Registered Voters', 'Election Day Votes',
       'Advanced Voting Votes', 'Absentee by Mail Votes', 'Provisional Votes',
       'Choice Total', 'Election Day Votes.1', 'Advanced Voting Votes.1',
       'Absentee by Mail Votes.1', 'Provisional Votes.1', 'Choice Total.1',
       'Election Day Votes.2', 'Advanced Voting Votes.2',
       'Absentee by Mail Votes.2', 'Provisional Votes.2', 'Choice Total.2',
       'Total', 'Unnamed: 18']

where 'Choice Total' is total votes for the R
      'Choice Total.1' is total votes for D 


"""

import pandas as pd
import os
import re

DATA_DIR = '/edata/GA'

col_map = { 
            'County': 'precinct',
            'Registered Voters': 'voters',

            'Election Day Votes': 'r_eday',
            'Advanced Voting Votes': 'r_adv',
            'Absentee by Mail Votes': 'r_mail',
            'Provisional Votes': 'r_prov',
            'Election Day Votes.1': 'd_eday',
            'Advanced Voting Votes.1': 'd_adv',
            'Absentee by Mail Votes.1': 'd_mail',
            'Provisional Votes.1': 'd_prov',

            'Choice Total': 'r_total',
            'Choice Total.1': 'd_total',
            'Choice Total.2': 'l_total',

            'Total': 'total'
          }

for filename in os.listdir(DATA_DIR):
    if re.search(r'clean\.txt$', filename):
        df = pd.read_csv("{}/{}".format(DATA_DIR, filename), sep='\t')
        df = df.rename(col_map, axis=1) 
        df['d_ratio'] = df['d_total']/df['voters']
        df['r_ratio'] = df['r_total']/df['voters']
        import pdb; pdb.set_trace()


