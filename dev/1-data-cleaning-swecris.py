#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:08:25 2020

@author: nesko
"""

import pandas as pd
import matplotlib.pyplot as plt
from inc import functions as f
from inc import stop_words as sw
from inc import extra_stopwords as esw
from google_drive_downloader import GoogleDriveDownloader as gdd
from pathlib import Path
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud

pd.set_option('max_colwidth', 150)

table_name = 'swecris'
db_path = 'db/goals.sqlite'

if not Path(db_path).is_file():
    gdd.download_file_from_google_drive(
        file_id='1okGwPDZlVScKKa-pN-tJB-j0XgchjwXL',
        dest_path=db_path,
    )
    print('if:')
db_path = 'sqlite:///' + db_path
print(db_path)
engine = create_engine(db_path, echo=False)
data_df = pd.read_sql_table(table_name, engine)
data_df.set_index('title', inplace=True, drop=True)
# print(data_df)
# print(data_df.columns)

data_clean = pd.DataFrame(data_df.abstract.apply(f.lemmatizeText))
data_clean = pd.DataFrame(data_clean.abstract.apply(f.clean_text_round1))
data_clean = pd.DataFrame(data_clean.abstract.apply(f.clean_text_round2))

sw.STOP_WORDS = sw.STOP_WORDS.union(esw.common_stopwords)
sw.STOP_WORDS = sw.STOP_WORDS.union(esw.extra_stopwords)

# cv = CountVectorizer(stop_words=sw.STOP_WORDS, ngram_range=(1, 2), max_features=1000)
cv = CountVectorizer(stop_words=sw.STOP_WORDS, max_features=1000)

data_cv = cv.fit_transform(data_clean.abstract)
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
