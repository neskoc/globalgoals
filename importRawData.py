#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:27:05 2020

@author: nesko
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
    if nrSwLetters <= 5 or len(raw[2]) < 50:
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
