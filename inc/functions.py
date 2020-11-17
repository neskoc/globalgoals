#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 2020

@author: nesko
"""

import sqlite3
import pandas as pd
import pprint
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
import requests
import re
import string

pp = pprint.PrettyPrinter(indent=2, width=200)


def readSQliteDB(dbname, sql):
    """
    Read data from the sqlite database.

    Parameters
    ----------
    dbname : str
        Name of the sglite db.
    sql : str
        sql commnd for fetching data from dn.

    Returns
    -------
    df : DataFrame
        Contains fetched table.

    """
    df = pd.DataFrame()
    conn = sqlite3.connect(dbname)
    df = pd.read_sql_query(sql, conn)
    return df


def writeToSQliteDB(dbname, sql):
    """
    Write data to the sqlite database.

    Parameters
    ----------
    dbname : str
        Name of the sglite db.
    sql : str
        sql commnd for writing data to db.

    Returns
    -------

    """
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def fetchHtmlContent(link):

    try:
        f = requests.get(link)
    except requests.ConnectionError as e:
        print(e)
        return False

    return f.text


def populateGoalNames(dbname, goal_links):
    goals = []
    for ix, goal_link in enumerate(goal_links):
        print(goal_link)
        # print(fetchGoal(goal_link))
        page = fetchHtmlContent(goal_link)
        soup = BeautifulSoup(page, 'lxml')
        tags = soup.select('h1.goal-title')
        goals.append(tags[0].text)
        sql_insert = 'INSERT INTO Goals VALUES ("{}", "{}", "")'.format(ix + 1, tags[0].text)
        print(sql_insert)
        writeToSQliteDB(dbname, sql_insert)


def fetchGoal(link):
    page = fetchHtmlContent(link)
    soup = BeautifulSoup(page, 'lxml')

    description = ''

    # Huvudmål
    tags = soup.select('h1.goal-title')
    for tag in tags:
        description += tag.text + '\n\n'

    # Lång beskrivning
    tags = soup.select('div.single-goal-long-description-text')
    for tag in tags:
        description += tag.text
    description += '\n'

    # Delmål
    tags = soup.select('div.container div.row div.col-8 h4')
    for tag in tags:
        description += tag.text + '\n'
    description += '\n'

    # Beskrivningar av delmål
    tags = soup.select('div.container div.row div.col-8 div.target-description')
    for tag in tags:
        description += tag.text
    description += '\n'

    # Snabba tips
    tags = soup.select('div.single-tip-inner h4')
    for tag in tags:
        description += tag.text + '\n'

    # additional tips
    tags = soup.select('div.single-additional-tip-content h4')
    for tag in tags:
        description += tag.text + '\n'
    description += '\n'

    # Snabba tips descriptions
    tags = soup.select('div.single-tip-inner div.tip-description p')
    for tag in tags:
        description += tag.text + '\n'

    # Additional tips descriptions
    tags = soup.select('div.single-additional-tip-content p')
    odd = False
    for tag in tags:
        if (odd):
            description += tag.text + '\n'
        odd = not odd

    return description

def updateSqliteTable(dbname, sql_insert):
    try:
        sqliteConnection = sqlite3.connect(dbname)
        print("Connected to SQLite")
        cursor = sqliteConnection.cursor()
        sql_update_query = sql_insert
        cursor.execute(sql_update_query)
        sqliteConnection.commit()
        print("Record Updated successfully ")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def uppdateGoalDescriptions(dbname, goal_links):
    for ix, goal_link in enumerate(goal_links):
        print(goal_link)
        description = fetchGoal(goal_link)
        sql_insert = """
        UPDATE Goals SET Description = '{}' where id = '{}'
        """.format(description, ix + 1)
        # print(sql_insert)
        updateSqliteTable(dbname, sql_insert)


def clean_text_round1(text):
    """First round of cleaning.

    Make text lowercase, remove text in square brackets,
    remove punctuation and remove words containing numbers.
    """
    text = text.lower()
    text = re.sub('|[.*?]|', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text


def clean_text_round2(text):
    """Second round of cleaning.

    Get rid of some additional punctuation and non-sensical text
    that was missed the first time around.
    """
    text = re.sub('\n', ' ', text)
    text = re.sub('[‘’“”…–|-]', '', text)
    text = re.sub('\s\s+', ' ', text)
    return text
