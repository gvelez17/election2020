import pandas as pd
import pickle
import os
import datetime
import matplotlib.pyplot as plt

def gen_party_graph(full, party_name):
    figure = plt.figure(figsize=(5, 10))
    figure.suptitle(party_name)
    ax = figure.add_axes([0,0,1,1])
    ax.xaxis.label.set_color("yellow")
    ax.yaxis.label.set_color("yellow")
    party_turnout = full[full['Party Affiliation']==party_name]
    ax.barh(party_turnout['Precinct_x'], party_turnout['turnout_percent'])

turnout = pd.read_csv('/edata/FL/turnout/stlucie.csv')

with open('/edata2/FL/full_data.pkl', 'rb') as f:
    full_data=pickle.load(f)

reg_data = full_data[full_data['County Code']=="STL"]
del full_data

hist = pd.read_csv('/edata2/FL/hist/STL_H_20201027.txt', names=['count','Voter ID', 'HistVoteDate', 'Etype', 'how'], sep='\t')
joined = reg_data.merge(turnout, how="right",  left_on="Voter ID", right_on="RegNum")
voters12 = hist[hist.HistVoteDate == '11/06/2012']['Voter ID'].tolist()
#100K voters

voters16 = hist[hist.HistVoteDate == '11/08/2016']['Voter ID'].tolist()
#132K voters

#in 2020, there were 172K voters

nvote = joined[~joined['Voter ID'].isin(voters12) & ~joined['Voter ID'].isin(voters16)]

nvote['VoterID'] = nvote['Voter ID'].fillna(0).astype('int64')
want_columns = ['VoterID', 'Name First', 'Name Middle', 'Name Last', 'Name Suffix', 'Residence Address Line 1', 'Residence Address Line 2', 'Residence City (USPS)', 'Residence State', 'Residence Zipcode']

# here are the ones who voted on election day that we didn't already look at, R, N, I
nvote[~nvote['VoterID'].isin(a_ids) & (pd.to_datetime(nvote.VoteDate).dt.date == pd.Timestamp(2020,11,3)) & (nvote['Party Affiliation'].isin(['REP','NPA','IND'])) & (pd.to_datetime(nvote['Registration Date']).dt.year==2020)][want_columns]



# 2020 voters who didn't vote in 2012 or 2016
# 62581

# when did they register
"""
(Pdb) pd.to_datetime(nvote['Registration Date']).dt.year.value_counts()
2020.0    11884
2018.0     8392
2019.0     8137
2017.0     5118
2016.0     3965
2012.0     1936
2008.0     1914
2004.0     1844
"""

# how did they vote
"""
(Pdb) pd.to_datetime(nvote['VoteDate']).dt.date.value_counts()
2020-11-03    13328
2020-10-20     3604
2020-10-21     3081
2020-10-30     2972
2020-10-28     2908
2020-10-27     2805
2020-10-26     2800
2020-10-31     2778
2020-10-23     2711
"""

# what is the distribution of reg year for election day voters
pd.to_datetime(nvote[pd.to_datetime(nvote['VoteDate']).dt.date == datetime.date(2020,11,3)]['Registration Date']).dt.year.value_counts()
"""
2020.0    2741
2018.0    1672
2019.0    1638
2017.0     984
2016.0     908
2008.0     473
2012.0     447
"""

# and for non-election day voters
"""
Registration Date']).dt.year.value_counts()
2020.0    9143
2018.0    6720
2019.0    6499
2017.0    4134
2016.0    3057
2012.0    1489
2004.0    1471
2008.0    1441
"""

# Of everyone who voted in 2020, what was the breakdown
"""
(Pdb) joined['Party Affiliation'].value_counts()
DEM    68440
REP    62524
NPA    37832
IND     2137
LPF      276
GRE       63
CPF       23
REF       15
PSL       10
ECO        9
"""

already = pd.read_csv('FL_since_june_ed_R.csv')
a_ids = already['Voter ID'].tolist()

