---
title: "Connecting to MSSQL Databases with Python"
slug: "connecting to MSSQL databases with python"
date: 2020-06-20T08:00:00-05:00
draft: false
publishdate: 2020-06-20T08:00:00-05:00
tags:
- programming
- python
- how-to
---

Yesterday I showed some boilerplate code to create a connection between Python and Oracle databases. I often work with Microsoft SQL Server as well. I used to connect to MSSQL via [pymssql][1]. I have had to change to [pyodbc][2] due to some conflicts with an older database version. I like pyodbc because it interfaces easily with many SQL systems so I can use it almost everywhere.

To install pyodbc open your terminal or favorite IDE and 

```
pip install pyodbc
```
If you have pandas installed the code below should work. Be sure to update the connection string and your query_string.

```
import pyodbc
import pandas as pd

def main():
    conn = connect_to_server()
    query_server(conn)
    conn.close()


def connect_to_server():
   conn = pyodbc.connect("DSN=server;UID=username;PWD=password")
    return conn
    

def query_server(conn):
    df_query = pd.read_sql(query_string, con=conn)
    df_query.to_csv("query.csv", sep = "\t", index = False,
              header = True, float_format="%.2f")


query_string f"""
    SELECT *
    FROM example_table
"""

main()
```

If you read yesterday’s post you can see that not much has changed.

The **main** function sets up a connection to the server, then sends a query to the newly created connection and then closes the connection.

The **connect_to_server** function establishes a valid connection string.

- Data Source Name (DSN) is the ip, host, or filename of your data source
- UID is your username
- PWD is your password

If you don't know this info then check with your network administrator.

The connection string is concatenated and returned.

The **query_server** function uses the database connection and makes an SQL query (as defined in the **query_string**). The data returned from the query is stored in a pandas dataframe and the dataframe is written to a .csv file.

[1]: https://pypi.org/project/pymssql/
[2]: https://pypi.org/project/pyodbc/
