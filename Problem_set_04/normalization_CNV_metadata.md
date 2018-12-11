# Descriptions of data normalization for cnv.csv.


Original data sheet contains 200575 rows and 13 columns.

This large table can be divided into 2 tables (reads and stats), to reduce redundancy and increase readability. So, it is a good idea to create a table named "reads" which has all the information about the reads, and "stats" table which has the statistic information of all reads.

Table reads:


|Column name | Data type|
|------------|------------|
| IDR | INTEGER PRIMARY KEY NOT NULL.
|chromosome | VARCHAR
| start | INTEGER
|end |INTEGER
|test |INTEGER
|ref |INTEGER
|L|INTEGER
|rposition| INTEGER 


Table stats:


|Column name | Data type|
|------------|------------|
| ID | INTEGER PRIMARY KEY NOT NULL.
|position | INTEGER FOREIGN KEY.
| log2 | INTEGER
|pvstat |INTEGER
|copynumbervariants |INTEGER
|copynumbervariantssize |VARCHAR
|copynumbervariantlog2|VARCHAR
|copynumbervariantpvstat| VARCHAR 