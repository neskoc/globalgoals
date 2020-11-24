#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 02:13:23 2020

@author: nesko
"""

import lemmy.pipe as lp
from transformers import pipeline
import pprint

pp = pprint.PrettyPrinter(indent=2, width=200)

# make swedish lemmatizer pipe component
lemmyPipe = lp.load('sv')

nlp = pipeline('ner', model='KB/bert-base-swedish-cased-ner', tokenizer='KB/bert-base-swedish-cased-ner')
nlp.add_pipe(lemmyPipe, after='tagger')

# nlp('Idag släpper KB tre språkmodeller.')

text = 'Engelbert tar Volvon till Tele2 Arena för att titta på Djurgården IF ' +\
       'som spelar fotboll i VM klockan två på kvällen.'

l = []
for token in nlp(text):
    if token['word'].startswith('##'):
        l[-1]['word'] += token['word'][2:]
    else:
        l += [ token ]

pp.pprint(l)
