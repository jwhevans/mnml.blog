---
title: "Copy CSV File Into Postgresql Table"
slug: "copy csv file into postgresql table"
date: 2021-01-15T06:00:00-05:00
draft: false
publishdate: 2021-01-15T06:00:00-05:00
tags:
- postgresql
- command line
---

Often data is passed around in “comma separated files” (.csv). Postgresql has a function that copies this data into existing tables. Let’s imagine you have a set of employee data that you need to copy into a table.

First create the table. For the purposes of this exercise our table looks like this

```
CREATE TABLE employee (
  id SERIAL,
  first_name    VARCHAR(50),
  last_name     VARCHAR(50),
  date_of_birth DATE,
  email         VARCHAR(255),
  date_of_hire  DATE
  PRIMARY KEY (id)
);
```
The CSV file looks like this
```
FIRST NAME, LAST NAME, DATE OF BIRTH, EMAIL, DATE OF HIRE
John, Doe, 1970-03-31, john.doe@example.com, 2006-07-05
Jane, Doe, 1986-06-03, jane.doe@example.com, 2018-03-01
```
To import the file run the following while connected to your database
```
COPY employee
FROM ‘path_to_csv’
DELIMITER ‘,’
CSV HEADER;
```
It is best to use absolute paths in the FROM clause. You can change the DELIMITER if your file uses a different delimiter. For example, we often delimit file with ‘|’ because other standard delimiters are present in some of our fields. If your CSV does not include a HEADER you can omit that line.

Postgres will inform you that it completed the task above by printing `COPY 2`.
