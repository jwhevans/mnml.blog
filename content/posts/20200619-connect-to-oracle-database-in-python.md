---
title: "Connecting to Oracle Databases with Python"
slug: "connecting to oracle databases with python"
date: 2020-06-19T08:00:00-05:00
draft: false
publishdate: 2020-06-19T08:00:00-05:00
tags:
- programming
- python
- how-to
---

At work we have have systems built on several databases. We also have a number of tools to grab the data for analysis and reporting. They work well for defined reports that must be pulled regularly and submitted in a specific format. There is always a need for ad-hoc one-off reports though. I often need to grab datasets from multiple databases and then combine them for further analysis.

My tool of choice for this work is Python. It has support for most major database systems.  One of our systems runs on Oracle. Oracle provides the [cx_Oracle package][1] on PyPI to manage connections to their servers. This is all that is needed to make a connection to versions of their database from version 9.2 through 19.

To install cx_Oracle open your terminal or favorite IDE and 

```
pip install cx_Oracle
```
If you have pandas installed the code below should work. Be sure to update the connection string and your query_string.

```
import cx_Oracle
import pandas as pd

def main():
    conn = connect_to_server()
    query_server(conn)
    conn.close()


def connect_to_server():
    ip   = r"XXX.XXX.XXX.XXX"
    port = r"XXXX"
    svc  = r"SERVICE_NAME"
    usr  = r"username"
    pwd  = r"password"

    dsn_tns = cx_Oracle.makedsn(ip, port, service_name = svc)
    conn = cx_Oracle.connect(user = usr, password = pwd, dsn = dsn_tns)
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

Let’s run through this code. First the cx_Oracle and pandas packages are imported. Pandas isn’t required, but I almost always use pandas for data analysis and very often import and export dataframes to .csv files.

The **main** function sets up a connection to the server, then sends a query to the newly created connection and then closes the connection.

The **connect_to_server** function establishes a valid connection string.

- ip is the IP address of the database server
- port is the listener port
- svc is the specific database service name
- usr is your username
- pwd is your password

With the exception of your username/password this data is typically stored in the tnsnames.ora file associated with your Oracle client. If you don't have the client then your network administrator may be able to give you the info.

The connection string is concatenated and returned.

The **query_server** function uses the database connection and makes an SQL query (as defined in the **query_string**). The data returned from the query is stored in a pandas dataframe and the dataframe is written to a .csv file.

[1]: https://oracle.github.io/python-cx_Oracle/
