import os
import glob
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# path must be set to local path
#TODO: Figure out how to make a raw URL for multiple csv file import
path = r'/Users/ericrivetna/Desktop/BW_BeesKnees/csv_import'

df = pd.concat(map(pd.read_csv, glob.glob(path + '/*.csv')),
               sort=True, ignore_index=True).reset_index()

cols = ['state', 'year', 'quarter', 'starting_pop',
        'max_pop', 'pop_lost', 'percent_lost', 'pop_gained',
        'pop_renovated', 'percent_renovated', 'varroa_mites',
        'other_pests', 'diseases', 'pesticides', 'other', 'unknown']

df.replace(np.NaN, '2015', inplace=True)
df.replace('2015', 2015, inplace=True)
df.sort_values(['year', 'quarter'], inplace=True)
df.reset_index(inplace=True)
df = df.reindex(columns=cols)
df.to_csv("./HoneyBee.csv")
