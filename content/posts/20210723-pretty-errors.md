---
title: "Pretty Errors"
slug: "pretty errors"
date: 2021-07-23T21:00:00-05:00
draft: false
publishdate: 2021-07-23T21:00:00-05:00
tags:
- python
- programming
---

I ran across a nice python package recently. [Pretty_Errors](https://pypi.org/project/pretty-errors/) formats python exception messages so that they are more legible. Installing it universally also enables the package to make syntax errors more legible. This is one of those packages that I wish I had years ago and I will automatically install for every project going forward.

```
$ python -m pip install pretty_errors
$ python -m pretty_errors 
```
Running these commands will install the package and then add it to your python startup procedure. If it is not setup universally then it must be imported into each project `import pretty_errors`. I prefer the universal method.
