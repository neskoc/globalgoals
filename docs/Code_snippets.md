
## SQL code for calculating frequency

### Formas

#### Ordered by class

```sql
-- Formas classified (categorised) data
SELECT CAST(Formas1 AS INTEGER)  AS class, count(Formas1) AS freq FROM clean_swecris WHERE  Formas1 != '' AND Formas1 != '0' GROUP BY class ORDER BY class ASC;
```
|__class__ | __freq__|
|---------:|--------:|
|2 | 130|
|3 | 55|
|4 | 14|
|6 | 41|
|7 | 33|
|8 | 5|
|9 | 39|
|10 | 4|
|11 | 77|
|12 | 114|
|13 | 52|
|14 | 37|
|15 | 115|
|16 | 10|
|17 | 13|

#### Ordered by frequency

```sql
-- Formas classified (categorised) data
SELECT count(Formas1) AS freq, CAST(Formas1 AS INTEGER)  AS class
FROM clean_swecris WHERE  Formas1 != '' GROUP BY class ORDER BY freq ASC;
```


| __freq__ | __class__ |
|---------:|--------:|
|4 | 10|
|5 | 8|
|7 | 0|
|10 | 16|
|13 | 17|
|14 | 4|
|33 | 7|
|37 | 14|
|39 | 9|
|41 | 6|
|52 | 13|
|55 | 3|
|77 | 11|
|114 | 12|
|115 | 15|
|130 | 2|

### Vinnova

#### Ordered by class

```sql
-- Vinnovas classified (categorised) data exept for empty
SELECT CAST(Self1 AS INTEGER)  AS class, count(Self1) AS freq
    FROM clean_swecris WHERE  Self1 != '' GROUP BY class ORDER BY class ASC;
```

|__class__ | __freq__|
|---------:|--------:|
|1 | 7|
|2 | 35|
|3 | 511|
|4 | 73|
|5 | 58|
|6 | 45|
|7 | 90|
|8 | 193|
|9 | 1403|
|10 | 180|
|11 | 542|
|12 | 963|
|13 | 256|
|14 | 105|
|15 | 95|
|16 | 242|
|17 | 378|

#### Ordered by frequency

```sql
-- Vinnovas classification through self assessment
SELECT COUNT(Self1) AS freq, Self1 AS class FROM clean_swecris
    WHERE  Self1 != '' GROUP BY class ORDER BY freq ASC;
```

| __freq__ | __class__ |
|---------:|--------:|
|7 | 1|
|35 | 2|
|45 | 6|
|58 | 5|
|73 | 4|
|90 | 7|
|95 | 15|
|105 | 14|
|180 | 10|
|193 | 8|
|242 | 16|
|256 | 13|
|378 | 17|
|511 | 3|
|542 | 11|
|963 | 12|
|1403 | 9|

### Formas + Vinnova

| __Vinnova__ | __Formas__ | __Sum__ | __class__ |
|------------:|-----------:|--------:|--------:|
|7 | 0 | 7 | 1|
|180 | 4 | 184 | 10|
|193 | 5 | 198 | 8|
|? (447) | 7 | 454 ? | 0|
|242 | 10 | 252| 16|
|378 | 13 | 391 | 17|
|73 | 14 | 87 | 4|
|90 | 33 | 123 | 7|
|105 | 37 | 142 | 14|
|1403 | 39 | 1442 | 9|
|45 | 41 | 86 | 6|
|256 | 52 | 308 | 13|
|511 | 55 | 566 | 3|
|542 | 77 | 619 | 11|
|963 | 114 | 1077 | 12|
|95 | 115 | 210 | 15|
|35 | 130 | 165 | 2|

### SQL queries

```sql

-- select at most 99 Formas rows of specific class (1)
SELECT abstract, Formas1 AS class FROM clean_swecris WHERE Formas1 == '1' ORDER BY RANDOM() LIMIT 99;

-- select random at most (99 - count) Vinnova rows of specific class (9)
SELECT abstract, Self1 AS class FROM clean_swecris WHERE Self1 == '9' ORDER BY RANDOM() LIMIT 99 -
 | (SELECT count(Formas1) AS count FROM clean_swecris WHERE Formas1 == '9');

-- select all Formas1 except for empty and '0'
SELECT abstract, Formas1 AS class FROM clean_swecris WHERE Formas1 != '' AND Formas1 != '0';

-- Ordered by frequency
-- Formas classified (categorised) data
SELECT count(Formas1) AS freq, CAST(Formas1 AS INTEGER)  AS class  FROM clean_swecris
WHERE  Formas1 != '' GROUP BY class ORDER BY freq ASC;
```
