import os, sys, glob, pickle, json, csv, sqlite3, sqlalchemy
import pandas as pd
import pandas.io.sql as psql
from pprint import pprint
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

path = r'/Users/ericrivetna/Desktop/BW_BeesKnees/Import Folder'
path_2016 = r'/Users/ericrivetna/Desktop/Bees_Knees/2016_Bees'
path_2017 = r'/Users/ericrivetna/Desktop/Bees_Knees/2017_Bees'
path_2018 = r'/Users/ericrivetna/Desktop/Bees_Knees/2018_Bees'
path_2019 = r'/Users/ericrivetna/Desktop/Bees_Knees/2018_Bees'

df = pd.concat(map(pd.read_csv, glob.glob(path +'/*.csv')),sort=True,ignore_index=True).reset_index()
print(df.columns.values.tolist())
cols = ['state','year', 'quarter', 'starting_pop', \
        'max_pop', 'pop_lost', 'percent_lost','pop_gained', \
        'pop_renovated', 'percent_renovated', 'varroa_mites', \
        'other_pests', 'diseases', 'pesticides', 'other', 'unknown']
df.replace(np.NaN,'2015',inplace=True)
df.replace('2015',2015,inplace=True)
df.sort_values(['year','quarter'],inplace=True)
df.reset_index(inplace=True)
df = df.reindex(columns=cols)
df.to_csv("./HoneyBee.csv")



