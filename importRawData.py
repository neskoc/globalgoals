#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:27:05 2020

@author: nesko

1. Import raw Swecris data from csv-file,
2. Filter out abstracts in sv language by counting specific Swedish letters åöä
    2.a Threshhold for the counter is set by variable svThreshhold
    2.b Second filter is by minimum number of chars in the abstract: totalCharsThreshhold
3. The result is saved in the sqlite database (table name swecris)

"""

import pandas as pd
import numpy as np

swecrisPath = 'raw-data/swecris-data.csv'
swedishLetters = 'åöä'

df = pd.read_csv(swecrisPath)
df = pd.DataFrame(df, columns=['Dnr', 'title.sv', 'abstract.sv', 'end_date', 'organization'])
nrSwLettersList = []
nonSwedishIndexList = []
lenlist = []
svThreshhold = 5
totalCharsThreshhold = 50

def replaceNan(x):
    if not isinstance(x, str):
        return ''
    else:
        return x


df['abstract.sv'] = df['abstract.sv'].apply(replaceNan)
a_df = df.values

for ix, raw in enumerate(a_df):
    nrSwLetters = 0
    for letter in raw[2]:
        if letter in swedishLetters:
            nrSwLetters += 1
    nrSwLettersList.append(nrSwLetters)
    if nrSwLetters <= svThreshhold or len(raw[2]) < totalCharsThreshhold:
        nonSwedishIndexList.append(ix)
    else:
        lenlist.append(len(raw[2]))

lenlist.sort()
a_df_sv = np.delete(a_df, nonSwedishIndexList, 0)

df_sv = pd.DataFrame(a_df_sv[:, [0, 1, 2, 4]], columns=['diarienr', 'title', 'abstract', 'organization'])

from sqlalchemy import create_engine


table_name = 'swecris'
engine = create_engine('sqlite:///db/goals.sqlite', echo=False)  # if_exists='append'
df_sv.to_sql(name=table_name, con=engine)
