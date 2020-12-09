#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 02:02:20 2020

@author: nesko
"""

import csv
from inc import functions as f

formasPath = 'raw-data/Formas-categories.sv.csv'
table_name = 'swecris'
dbname = 'db/goals.sqlite'
organization = 'Formas'

# df = pd.read_csv(formasPath)
# df = pd.DataFrame(df, columns=['Dnr',
#                                'Formas1', 'Formas2',
#                                'Kateg1', 'Kateg2', 'Kateg3'])

with open(formasPath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
            sql_insert = """
                UPDATE {table}
                SET Formas1 = '{f1}',
                    Formas2 = '{f2}',
                    Self1 = '{k1}',
                    Self2 = '{k2}',
                    Self3 = '{k3}'
                WHERE diarienr = '{dnr}' AND
                      organization = '{org}'
                """.format(
                    table=table_name,
                    org=organization,
                    dnr=row[0],
                    f1=row[1],
                    f2=row[2],
                    k1=row[3],
                    k2=row[4],
                    k3=row[5]
                    )
            # print(sql_insert)
            f.updateSqliteTable(dbname, sql_insert)
            # isinstance(row[2], int)
            print('\t{}|{:>2d}|{:>2s}|{:>2s}|{:>2s}'.
                  format(row[0], int(row[1]), row[2], row[3], row[4]))
    print(f'Processed {line_count} lines.')
