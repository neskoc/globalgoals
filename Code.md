# About the code

This document is describing how to use code in the project.

__Snapshot of the files and folders__

.  
├── 1-data-cleaning.ipynb  
├── 1-data-cleaning.py  
├── Code.md  
├── README.md  
├── Untitled.ipynb  
├── db  
│.......├── goals.sqlite  
│.......└── goals.sqlite.sql  
├── img  
│.......├── Figure\ 2020-11-17\ 014459.png  
│.......├── Figure\ 2020-11-17\ 014701.png  
│.......└── WordCloud_2020.11.18.png  
├── inc  
│....... ├── __init__.py  
│....... ├── examples.py  
│....... ├── functions.py  
│....... └── sv  
│.................├── __init__.py  
│.................├── lex_attrs.py  
│.................├── morph_rules.py  
│.................├── stop_words.py  
│.................├── syntax_iterators.py  
│.................├── tag_map.py  
│.................└── tokenizer_exceptions.py  
└── parse_url.py  

- __1-data-cleaning.py__: current main file
    * Reads collected global goals data from the sqlite db,
    * cleans up,
    * removes stop_words,
    * does some word counting (CountVectorizer),
    * draws a word cloud of the result.
- __inc/functions.py__: different help functions
- __parse_url.py__: used for parsing urls for global goals and storing data in sqlite db
- __inc/sv/__: files used for nlp of swedish language
- __db/__: contains sqlite database(s) with collected data,
    currently there is only one db, but could be more in the future
