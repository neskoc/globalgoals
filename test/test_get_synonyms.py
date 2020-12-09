#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:45:28 2020

@author: nesko
"""

from inc import functions as f

word = "försök"

synonyms = f.fetchSynonyms(word)
print(synonyms)
