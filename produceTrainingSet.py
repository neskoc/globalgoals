#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:40:23 2020

@author: nesko
"""


import sqlite3
import numpy as np


def fetchTrainingData(db, sqlCmd):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(sqlCmd)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        return result

    except sqlite3.Error as error:
        print("Failed to run sqlite command", error)
    finally:
        if (conn):
            conn.close()


db_path = 'db/categorised_swecris.sqlite'

for ix in range(2,18):
    sqlCmd = f'''
        SELECT abstract, Formas1 AS class FROM clean_swecris
            WHERE class == '{ix}' ORDER BY RANDOM() LIMIT 99
        '''
    result = np.array(fetchTrainingData(db_path, sqlCmd))
    if (ix == 2):
        training_data_Formas = np.copy(result)
    elif (result.size > 0):
        training_data_Formas = np.vstack((training_data_Formas, result))


for ix in range(2,18):
    sqlCmd = f'''
        SELECT abstract, Self1 AS class FROM clean_swecris
            WHERE Self1 == '{ix}' ORDER BY RANDOM()
            LIMIT 99 - (SELECT count(Formas1) AS count FROM clean_swecris WHERE Formas1 == '{ix}');
        '''
    result = np.array(fetchTrainingData(db_path, sqlCmd))
    if (ix == 2):
        training_data_Vinnova = np.copy(result)
    elif (result.size > 0):
        training_data_Vinnova = np.vstack((training_data_Vinnova, result))

# print(training_data_Formas)

# data_df = pd.read_sql_table(table_name, engine)
# data_df['class'] = data_df['Formas1'] if data_df['Formas1'] is not  data_df['Self1']
# data_df['class'] = data_df['Formas1', 'Self1'].apply(lambda x: x['Formas1'] if   x['Formas1'] != '' else  x['Self1'])

# columns = ['abstract', 'Formas1']
# training_data_Formas = pd.DataFrame(data_df, columns=columns)

# training_data_Formas = training_data_Formas[training_data_Formas['Formas1'] != '']

# data_df.loc[data_df['Formas1'] != '', 'class'] = data_df['Formas1']
# data_df.loc[data_df['Formas1'] == '', 'class'] = data_df['Self1']
# training_data = pd.DataFrame(data_df, columns=columns)
