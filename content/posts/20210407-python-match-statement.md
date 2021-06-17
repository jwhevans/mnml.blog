---
title: "Python 3.10 Will Support Switch Style Statements"
slug: "python will support switch statement"
date: 2021-04-07T08:00:00-05:00
draft: false
publishdate: 2021-04-07T08:00:00-05:00
tags:
- python
- programming
---

Python has never supported switch statements. Instead long if...else chains are the norm. In [Python 3.10 this is changing][1]. Later this year a new statement, ```match```, will be added to the language. ```match``` has many of the characteristics  of ```switch``` statements but is not as simple as the C version. C switch statements compare integers. They are fast. Python match statements compare patterns. This is very powerful but comes with a performance hit. I'm not overly concerned. Python is not known for its performance and I use it for ease of development. If I need speed I'll switch to C.

Adam Zeloof has a nice writeup with examples on [HackADay][2].

[1]: https://www.python.org/dev/peps/pep-0622/
[2]: https://hackaday.com/2021/04/02/python-will-soon-support-switch-statements/
