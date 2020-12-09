#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 02:02:20 2020

@author: nesko
"""

import sqlite3
import re
from inc import functions as f

originDBpath = 'db/goals.sqlite'
newDBpath = 'db/categorised_swecris.sqlite'
table_name = 'swecris'

connOrigin = sqlite3.connect(originDBpath)
curs = connOrigin.cursor()

connNew = sqlite3.connect(newDBpath)
selectCommand = 'SELECT * FROM swecris ORDER BY Formas1, Self1'

ix = 0
for row in curs.execute(selectCommand):
    if not (row[5] is None) or not (row[6] is None):
        row3 = f.removeNewlines(row[3])
        row3 = re.sub(r'[‘’“”"…–|-]', '', row3)
        row2 = f.removeNewlines(row[2])
        row2 = re.sub(r'[‘’“”"…–|-]', '', row2)
        if row[5] is None:
            row5 = ''
        else:
            row5 = row[5]
        if row[6] is None:
            row6 = ''
        else:
            row6 = row[6]
        insertCommand = """
            INSERT INTO swecris(ix, diarienr, title, abstract, organization, Formas1, Self1)
                VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}");
            """.format(ix, row[1], row2, row3, row[4], row5, row6)
        f.writeToSQliteDB(newDBpath, insertCommand)
        ix += 1
