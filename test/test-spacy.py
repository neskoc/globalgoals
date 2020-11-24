#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:20:20 2020

@author: nesko
"""


from spacy.tokens import Doc
from spacy.lang.sv import Swedish


def city_getter(doc):
    """
    Test of Doc.set_extension.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return any(city in doc.text for city in ("New York", "Paris", "Berlin"))


nlp = Swedish()
Doc.set_extension("has_city", getter=city_getter, force=True)
doc = nlp("I like New York")
if doc._.has_city:
    print('There is a city in the text object')
else:
    print('There is no city in the text object')
