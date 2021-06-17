---
title: "Data Munging in Postgresql"
slug: "data munging in postgresql"
date: 2021-02-03T09:00:00-05:00
draft: false
publishdate: 2021-02-03T09:00:00-05:00
tags:
- postgresql
---

We recently moved a data repository from MSSQL to Postgresql. The canonical data is stored in Oracle 10g and encoded as UTF-8. MSSQL was storing in LATIN1, unbeknownst to me. It worked somehow. Postgres was setup UTF-8. The migration was simple and all python based reports worked with a simple update to the database connection string. Excel reports began throwing errors on import. The errors were related to UTF-8 characters not being supported by WIN1252 (cp1252) encoding.

After searching there were a few possible solutions.

1. Use UNICODE postgres drivers instead of ANSI
2. Send data to .csv files first and then import to Excel with UTF-8 encoding turned on.
3. Update the encoding of the local repository.

Option 1 was the easiest. We tried this but found that regardless of the driver support, Excel (Office 365) would not properly import certain UTF-8 characters. In particular U2265, U215b, and a hex character 0x9d. So, choice of driver did not matter.

Sending data to .csv works. However, there are additional steps necessary for this workflow. We need a cron job to write out the .csv files. Then we are storing the data twice. Excel handles updates to an existing .csv connection well but initial imports typically need work. In particular, column types must be updated. Technically savvy users handle this well but most people don’t want the hassle.

We knew that changing the encoding of the database would move the problem from Excel to the import script but that problem would be ours and be visible. We chose that route.

Changing the encoding did introduce import errors in our python script but they were easily caught and handled.

We first updated the Postgresql encoding

```
\encoding WIN1252
```

Then we added exception handling to the import threads to catch UnicodeExceptions

```
try:
    *import thread*
    
exception UnicodeEncodeError: 
    *log error*
    *email bug tracker*
```

As was expected the issue existed in only a few tables and columns of the replicated data. Open ended text fields for notes were the main culprit. After identifying the sources and specific characters causing the problem we updated our import scripts to catch these characters before import.

The old entries were cleaned up using postgres’s REGEXP_MATCHES and REGEXP_REPLACE function. For example

```
SELECT REGEXP_MATCHES(my_column,regex,flag) from my_table;

UPDATE my_table 
SET my_column = REGEXP_REPLACE(my_column,regex,replacement_string,flag);
```

In this case regex was U&’2265’, U&’215b’, and E’\x9d’. 