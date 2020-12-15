#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 2020

@author: nesko
"""

import sqlite3
import random
import pandas as pd
import pprint
import string
import re
import requests
import stanza
from spacy_stanza import StanzaLanguage

try:
    from BeautifulSoup import BeautifulSoup, SoupStrainer
except ImportError:
    from bs4 import BeautifulSoup, SoupStrainer
from urllib import parse
from sqlalchemy import create_engine

pd.set_option('max_colwidth', 150)

svStanzaDownloaded = False
snlpInitialized = False
nlpStanza = {}

pp = pprint.PrettyPrinter(indent=2, width=200)

categories = []

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


def fetchSynonyms(word):
    urlencoded_word = parse.quote_plus(word)
    page_link = "https://www.synonymer.se/sv-syn/" + urlencoded_word
    synonyms = []
    page = fetchHtmlContent(page_link)
    soup = BeautifulSoup(page, 'lxml')
    div_dict_default = soup.find('div', {'id': 'dict-default'})
    div_body = div_dict_default.find('div', {'class': 'body'})
    a_tags = div_body.ul.li.ol.find_all('a')
    for a in a_tags:
        synonyms.append(a.text)
    return synonyms


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

def updateSqliteTable(dbname, sql):
    try:
        sqliteConnection = sqlite3.connect(dbname)
        print("Connected to SQLite")
        cursor = sqliteConnection.cursor()
        cursor.execute(sql)
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
    """
    Update table Goals with Descriptions.

    First pass didn't store Descriptions which is corrected here
    Parameters
    ----------
    dbname : str
        sqlite db name to be updated.
    goal_links : list
        List with all links to collect descriptions from.

    Returns
    -------
    None.

    """

    for ix, goal_link in enumerate(goal_links):
        print(goal_link)
        description = fetchGoal(goal_link)
        sql_insert = """
        UPDATE Goals SET Description = '{}' where id = '{}'
        """.format(description, ix + 1)
        # print(sql_insert)
        updateSqliteTable(dbname, sql_insert)


def removeNewlines(text):
    text = re.sub(r'\\r\\n', ' ', text)
    text = re.sub(r'\\n', ' ', text)
    return ' '.join(text.split())


def mergeMultipleSpaces(text):
    text = re.sub(r'\r\n', ' ', text)
    text = re.sub(r'\n', ' ', text)
    return text


def clean_text_round1(text):
    """First round of cleaning.

    Make text lowercase, remove text in square brackets,
    remove punctuation and remove words containing numbers.
    """
    text = text.lower()
    text = re.sub(r'|[.*?]|', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text


def clean_text_round2(text):
    """Second round of cleaning.

    Get rid of some additional punctuation and non-sensical text
    that was missed the first time around.
    """
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[‘’“”…–|-]', '', text)
    text = re.sub(r'\s\s+', ' ', text)
    return text

def getGGTrainData():
    train_data = ''
    return train_data

def addLables(textcat):
    # textcat.add_label(category)

    table_name = 'Goals'
    engine = create_engine('sqlite:///db/goals.sqlite', echo=False)
    data_df = pd.read_sql_table(table_name, engine)
    data_df.set_index('Name', inplace=True, drop=True)

    for data in data_df:
        textcat.add_label(data.Name)
        categories.append(data.Name)
    pp.pprint(categories)
    return textcat

def load_data(limit=0, split=0.8):
    """Load data from db/csv."""
    # Partition off part of the train data for evaluation
    train_data = getGGTrainData()
    random.shuffle(train_data)
    train_data = train_data[-limit:]
    texts, labels = zip(*train_data)
    # cats = [{"POSITIVE": bool(y), "NEGATIVE": not bool(y)} for y in labels]
    cats = [categories[label - 1] for label in labels]
    split = int(len(train_data) * split)
    return (texts[:split], cats[:split]), (texts[split:], cats[split:])


def downloadStanza(lang):
    # download sv stanza (to avoid downloading it for every doc)
    global svStanzaDownloaded
    if not svStanzaDownloaded:
        stanza.download(lang)
        svStanzaDownloaded = True

def initStanzaPipeline(lang):
    downloadStanza(lang)
    global snlpInitialized
    global nlpStanza
    if not snlpInitialized:
        snlp = stanza.Pipeline(lang=lang)
        nlpStanza['snlp'] = StanzaLanguage(snlp)
        snlpInitialized = True


def lemmatizeText(text):
    text = removeNewlines(text)

    initStanzaPipeline('sv')

    doc = nlpStanza['snlp'](text)

    lemmatized_text = ''
    for token in doc:
        if token.lemma_ == 'all':
            token.lemma_ = 'alla'
        lemmatized_text += token.lemma_ + ' '
    text = lemmatized_text
    return text