#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:45:28 2020

@author: nesko
"""

import functions as f

dbname = 'db/goals.sqlite'

goal_links = [
    "https://www.globalamalen.se/om-globala-malen/mal-1-ingen-fattigdom/",
    "https://www.globalamalen.se/om-globala-malen/mal-2-ingen-hunger/",
    "https://www.globalamalen.se/om-globala-malen/mal-3-halsa-och-valbefinnande/",
    "https://www.globalamalen.se/om-globala-malen/mal-4-god-utbildning-alla/",
    "https://www.globalamalen.se/om-globala-malen/mal-5-jamstalldhet/",
    "https://www.globalamalen.se/om-globala-malen/mal-6-rent-vatten-och-sanitet/",
    "https://www.globalamalen.se/om-globala-malen/mal-7-hallbar-energi-alla/",
    "https://www.globalamalen.se/om-globala-malen/mal-8-anstandiga-arbetsvillkor-och-ekonomisk-tillvaxt/",
    "https://www.globalamalen.se/om-globala-malen/mal-9-hallbar-industri-innovationer-och-infrastruktur/",
    "https://www.globalamalen.se/om-globala-malen/mal-10-minskad-ojamlikhet/",
    "https://www.globalamalen.se/om-globala-malen/mal-11-hallbara-stader-och-samhallen/",
    "https://www.globalamalen.se/om-globala-malen/mal-12-hallbar-konsumtion-och-produktion/",
    "https://www.globalamalen.se/om-globala-malen/mal-13-bekampa-klimatforandringarna/",
    "https://www.globalamalen.se/om-globala-malen/mal-14-hav-och-marina-resurser/",
    "https://www.globalamalen.se/om-globala-malen/mal-15-ekosystem-och-biologisk-mangfald/",
    "https://www.globalamalen.se/om-globala-malen/mal-16-fredliga-och-inkluderande-samhallen/",
    "https://www.globalamalen.se/om-globala-malen/mal-17-genomforande-och-globalt-partnerskap/"
    ]


f.populateGoalNames(dbname, goal_links)
f.uppdateGoalDescriptions(dbname, goal_links)
