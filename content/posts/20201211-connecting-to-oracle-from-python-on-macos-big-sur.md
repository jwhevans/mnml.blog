---
title: "Connecting to Oracle from Python on macOS Big Sur"
slug: "connecting to oracle from python on macos big sur"
date: 2020-12-11T01:00:00-05:00
draft: false
publishdate: 2020-12-11T01:00:00-05:00
tags:
- mac
- python
- programming
- oracle
---

After upgrading one of my machines to macOS Big Sur my Python scripts that were connected to an Oracle database broke. I was able to fix them as follows.

I use cx_Oracle to handle connections to the database. Within my oracle environment I installed cx_Oracle

```
python -m pip install cx_Oracle --upgrade
```

Previous versions of macOS worked with the Oracle Instant Client libraries 12.2. Newer versions are available. I was unable to connect using 12.2 or 18.1. I installed the 19.8 version from the [Oracle Downloads Site][1]. If you are only scripting from Python then the Basic Lite version is sufficient. I unzipped these files to ~/Oracle/

Previously I was able to use cx_oracle by exporting the LD_LIBRARY_PATH. Several online resources recommend this, e.g. at the command line run `export LD_LIBRARY_PATH=”~/Oracle/instantclient_19_8/"`. Doing this on Big Sur led to a connection error DPI:1047.

Instead I was able to solve the connection error by starting each script with a call to cx_Oracle.init_oracle_client()

```
#!/usr/local/bin/python3

import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir="/Users/your-name/Oracle/instantclient_19_8")
```

[1]: https://www.oracle.com/database/technologies/instant-client/macos-intel-x86-downloads.html
