#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 02:02:20 2020

@author: nesko
"""

import csv
from inc import functions as f

formasPath = 'raw-data/Vinnova.clean.csv'
table_name = 'swecris'
dbname = 'db/goals.sqlite'
organization = 'Vinnova'

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
                SET Self1 = '{s1}'
                WHERE diarienr = '{dnr}' AND
                      organization = '{org}'
                """.format(
                    table=table_name,
                    org=organization,
                    dnr=row[0],
                    s1=row[1]
                    )
            # print(sql_insert)
            f.updateSqliteTable(dbname, sql_insert)
            # isinstance(row[2], int)
            print('\t{}|{:>2s}'.
                  format(row[0], row[1]))
    print(f'Processed {line_count} lines.')
