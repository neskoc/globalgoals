#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:08:25 2020

@author: nesko
"""

from inc import functions as f
from inc.sv import stop_words as sw
import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

pd.set_option('max_colwidth', 150)

table_name = 'Goals'
engine = create_engine('sqlite:///db/goals.sqlite', echo=False)
data_df = pd.read_sql_table(table_name, engine)
data_df.set_index('Name', inplace=True, drop=True)
# print(data_df)
# print(data_df.columns)


data_clean = pd.DataFrame(data_df.Description.apply(f.clean_text_round1))
data_clean = pd.DataFrame(data_clean.Description.apply(f.clean_text_round2))

# print(sw.STOP_WORDS)
extra_stopwords = ['är', 'både', 'samt', 'ge', 'se', 'ta',
                   'år', 'synnerhet', 'sätt', 'först', 'öka', 'minska']
sw.STOP_WORDS = sw.STOP_WORDS.union(extra_stopwords)
cv = CountVectorizer(stop_words=sw.STOP_WORDS, ngram_range=(1,2), max_features=1000)

data_cv = cv.fit_transform(data_clean.Description)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index
data_dtm = data_dtm.transpose()

# print(data_dtm)

# Find the top 30 words within each goal
top_dict = {}
for c in data_dtm.columns:
    top = data_dtm[c].sort_values(ascending=False).head(30)
    top_dict[c] = list(zip(top.index, top.values))

# print(top_dict)

# Print the top 15 words within each goal
for name, top_words in top_dict.items():
    print()
    print(', '.join([word for word, count in top_words[0:14]]))
    print('---')

wc = WordCloud(stopwords=sw.STOP_WORDS, background_color="white",
               colormap="Dark2", max_font_size=150, random_state=42)

plt.rcParams['figure.figsize'] = [30, 12]

names = data_clean.index.values.tolist()

# Create subplots for each Global Goal
for index, name in enumerate(data_dtm.columns):
    wc.generate(data_clean.Description[name])

    plt.subplot(5, 4, index+1)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(names[index])

plt.show()
