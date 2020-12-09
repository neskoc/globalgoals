#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 02:13:23 2020

@author: nesko
"""

# import lemmy.pipe as lp
from transformers import pipeline
import pprint
from inc import functions as f

pp = pprint.PrettyPrinter(indent=2, width=200)

# make swedish lemmatizer pipe component
# lemmyPipe = lp.load('sv')

nlp = pipeline('ner', model='KB/bert-base-swedish-cased-ner', tokenizer='KB/bert-base-swedish-cased-ner')
# nlp.add_pipe(lemmyPipe, after='tagger')

# nlp('Idag släpper KB tre språkmodeller.')

text = 'Engelbert tar Volvon till Tele2 Arena för att titta på Djurgården IF ' +\
        'som spelar fotboll i VM klockan två på kvällen.'

# pipeline has limitation: max 512 tokens
# text = """Ingen fattigdom


# Fattigdom omfattar fler dimensioner än den ekonomiska. Fattigdom innebär även brist på frihet, inflytande, hälsa, utbildning och säkerhet. Det brukar kallas för multidimensionell fattigdom. Idag lever 1,3 miljarder människor i multidimensionell fattigdom och av dessa är hälften under 18 år.
# Brist på mat, sjukvård, säkerhet och rent vatten dödar tusentals människor varje dag, men det blir bättre och sedan 1990 har den extrema fattigdomen halverats. Mål 1 handlar om att avskaffa fattigdom i alla dess former och ge alla människor i världen chans till ett värdigt och tryggt liv.

# 1.1 Utrota den extrema fattigdomen
# 1.2 Minska fattigdomen med minst 50 %
# 1.3 Inför sociala trygghetssystem
# 1.4 Lika rätt till egendom, grundläggande tjänster, teknologi och ekonomiska resurser
# 1.5 Bygg motståndskraft mot ekonomiska, sociala och miljökatastrofer
# 1.A Mobilisera resurser till implementering av politik för fattigdomsbekämpning
# 1.B Skapa policyramverk med fattigdoms- och jämställdhetsperspektiv
# """

cleandText = f.removeNewlines(text)

result = nlp(cleandText)

rebuilt = []
for token in result:
    if token['word'].startswith('##'):
        rebuilt[-1] += token['word'][2:]
    else:
        rebuilt += [token['word']]
print('rebuilt')
pp.pformat(rebuilt)

print('result')
pp.pprint(result)
