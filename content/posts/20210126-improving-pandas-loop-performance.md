---
title: "Improving Pandas Loop Performance"
slug: "improving pandas loop performance"
date: 2021-01-26T06:00:00-05:00
draft: false
publishdate: 2021-01-26T06:00:00-05:00
tags:
- programming
- Python
- pandas
---

I spent a lot of time optimizing a python script last week. The script takes a list of open orders for a manufacturing plant. It joins this table with a list of open purchase orders and manufacturing orders. Finally, it joins this with a table of bill of materials and stock levels. The resulting dataframe has approximately 3.5 million rows and is a little over 1.0 Gb in memory. The script then checks every order line for the most effective, “fastest” as in lead time, method to fulfill the order. Lines that can be fulfilled now are updated so that order planners can send those items to the floor immediately.

The initial script used the pandas iterrows() function to loop over the data. Two loops are necessary because customer orders may be fulfilled by manufacturing orders with their own bill of material. This resulted in an average run time of just over 15 minutes. Then I found this gem, [“How To Make Your Pandas Loop 71803 Times Faster”][1]. I have not been able to take full advantage of the pandas and numpy vectorization. I suspect I can make further improvements. However, the code now runs in 6 minutes.

I also received a nice article in my RSS feed this week regarding [Python f-strings][2]. It is a quick introduction and a fast read. I use f-strings almost exclusively. If you are not familiar with them or need a few pointers check out the link.

[1]: https://towardsdatascience.com/how-to-make-your-pandas-loop-71-803-times-faster-805030df4f06
[2]: https://realpython.com/python-f-strings/
