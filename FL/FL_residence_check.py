import pandas as pd
import pickle
import os
import datetime

county_queries=['STL', 'BRO', 'DAD']

def query(df, cut_length, filters = dict()):
    """
    filters should be dict ex: {column_name: value}
    """
    df = df[df['Residence Address Line 1'] != '*']
    filename = './residence_queries/by_res'
    for key, value in filters.items():
        filename += '_' + key + ': ' + value + '_'
        df = df[df[key] == value]
    df = df.iloc[:min(cut_length, df.shape[0])]
    df.to_csv(filename[:-1], index = False)

print('Loading data')
with open('/edata2/FL/full_data.pkl', 'rb') as f:
    full_data=pickle.load(f)
    
print('grouping')
by_res = full_data.drop_duplicates('Voter ID', keep='last').groupby(['Residence Address Line 1', 'Residence Address Line 2', 'Mailing City', 'County Code', 'Residence Zipcode', 'Party Affiliation']).count().sort_values('Voter ID', ascending=False)['Voter ID']

by_res = pd.DataFrame(by_res)
by_res.columns = ['count']
by_res = by_res.reset_index()

print('running queries')
print('general')
query(by_res, 200)
for i in county_queries:
    print('County query: '+ i)
    query(by_res, 20, {'County Code': i})