#!/usr/bin/env python3

# remove the the columns that we don't need:
import pandas as pd
import numpy as np
df=pd.read_csv("/ufrc/zoo6927/share/moeinraja/project_02/sequencing_data.csv")
my_cols = set(df.columns)
my_cols.remove('chromosome') # removing the 'chromosome' column
my_cols.remove('start')			# removing the 'start' column
my_cols.remove('end')			# removing the 'end' column			
my_cols = list(my_cols)
df2 = df[my_cols]
df.head()
df2.head()

# add new columns to calculate the sum and average:
df2['sum'] = df2[df2.columns].sum(axis=1)
df2['avg'] = df2['sum'] / (len(df2.columns) - 1)
df2.head()

# calculate correlation between 2 columns:

def get_corrs(df2):
    col_correlations = df2.corr()
    col_correlations.loc[:, :] = np.tril(col_correlations, k=-1)
    cor_pairs = col_correlations.stack()
    return cor_pairs.to_dict()

my_corrs = get_corrs(df2)

# defining the correlation fucntion:
def print_correlation():
    print('The correlation between avg & ref is ',(my_corrs[('avg','ref')]))
    print('The correlation between avg & test is ',(my_corrs[('avg','test')]))
    print('The correlation between test & ref is ',(my_corrs[('ref','test')]))

print_correlation()

# Checking if we are going the right way or not:

while True:
    my_corrs[('ref','ref')] == 0.0 and my_corrs[('test','test')] == 0.0 and my_corrs[('avg', 'avg')] == 0.0 and my_corrs[('avg', 'ref')] >= 0.9 and my_corrs[('avg', 'test')] >= 0.9
    break
if my_corrs[('ref','ref')] != 0.0 or my_corrs[('test','test')] != 0.0 or my_corrs[('avg', 'avg')] != 0.0 or my_corrs[('avg', 'ref')] <= 0.9 or my_corrs[('avg', 'test')] <= 0.9:
    print('The wrong way, come back and correct it')
else:
    print('Done!')


# End of script





































	
