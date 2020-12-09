#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 02:02:20 2020

@author: nesko
"""

import sqlite3
from inc import functions as f

originDBpath = 'db/goals.sqlite'
newDBpath = 'db/swecris.sqlite'
table_name = 'swecris'

connOrigin = sqlite3.connect(originDBpath)
curs = connOrigin.cursor()

connNew = sqlite3.connect(newDBpath)
selectCommand = 'SELECT * FROM swecris ORDER BY Formas1, Self1'

count = 0
for row in curs.execute(selectCommand):
    if not (row[5] is None) or not (row[6] is None):
        count += 1
print('Count: ', count)
