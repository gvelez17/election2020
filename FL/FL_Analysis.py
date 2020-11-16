import pandas as pd
import pickle
import os
import datetime

HIST_DIR='/edata2/FL/hist'
DETAIL_DIR = '/edata2/FL/detail'
ALL_HIST = list(os.listdir(HIST_DIR))
ALL_DETAIL = list(os.listdir(DETAIL_DIR))

def register_dt_to_datetime(date_str):
    values=[int(i) for i in date_str.split('/')]
    return datetime.datetime(values[2], values[0], values[1])

def filter_late(earliest_year, earliest_month, f, reg_id_column, date_column):
    print("sorting")
    f=f.sort_values([reg_id_column, date_column])
    print("grouping")
    first_reg=f[[reg_id_column, date_column]].groupby(reg_id_column).head(1)
    print("finding first registrations")
    late_reg=first_reg[first_reg.apply(lambda row: (row[date_column].year>=earliest_year
                                                    and row[date_column].month>=earliest_month), axis=1)]
    late_reg_ids=set(late_reg[reg_id_column])
    return f[f[reg_id_column].isin(late_reg_ids)]

with open('/edata2/FL/full_data.pkl', 'rb') as f:
    full_data=pickle.load(f)

#for processing 
#late_registrations = filter_late(2020, 1, full_data, 'Voter ID', 'Registration Date')

with open('/edata2/FL/late_registrations.pkl', 'rb') as f:
    late_registrations=pickle.load(f)
    
print("{}% of registrants just registered this year".format(round(late_registrations.shape[0]/full_data.shape[0]*100, 3)))

by_party_late = late_registrations.groupby('Party Affiliation').count()['Voter ID']
by_party_total = full_data.groupby('Party Affiliation').count()['Voter ID']

print("{}% of late registrations were Democrats while {}% of all registraions are Democrats".format(round(by_party_late["DEM"]/late_registrations.shape[0]*100, 2), round(by_party_total["DEM"]/full_data.shape[0]*100, 2)))

print("{}% of late registrations were Republicans while {}% of all registrations are Republicans".format(round(by_party_late["REP"]/late_registrations.shape[0]*100, 2), round(by_party_total["REP"]/full_data.shape[0]*100, 2)))

late_reg_precinct = pd.DataFrame(late_registrations.groupby('Precinct').count()['Voter ID'])
      
late_reg_precinct = late_reg_precinct.merge(pd.DataFrame(late_registrations[late_registrations['Party Affiliation'] == 'DEM'].groupby('Precinct').count()['Voter ID']), on = 'Precinct', how = 'left')
late_reg_precinct = late_reg_precinct.merge(pd.DataFrame(late_registrations[late_registrations['Party Affiliation'] == 'REP'].groupby('Precinct').count()['Voter ID']), on = 'Precinct', how = 'left')

late_reg_precinct.columns = ['Total', 'DEM', 'REP']

late_reg_precinct['DEM_ratio'] = late_reg_precinct.apply(lambda row : row['DEM']/row['Total'], axis=1)
late_reg_precinct['REP_ratio'] = late_reg_precinct.apply(lambda row : row['REP']/row['Total'], axis=1)

print("Printing highest percent of DEM and REP ratios per precinct")
print(late_reg_precinct[late_reg_precinct['DEM_ratio'].notnull()].sort_values('DEM_ratio', ascending=False))
print(late_reg_precinct[late_reg_precinct['REP_ratio'].notnull()].sort_values('REP_ratio', ascending=False))

print("Printing highest percent of DEM and REP ratios per precinct that has registered population greater than or equal to 10")
print(late_reg_precinct[(late_reg_precinct['DEM_ratio'].notnull()) & (late_reg_precinct['Total']>=10)].sort_values('DEM_ratio', ascending=False))
print(late_reg_precinct[(late_reg_precinct['REP_ratio'].notnull()) & (late_reg_precinct['Total']>=10)].sort_values('REP_ratio', ascending=False))
      
