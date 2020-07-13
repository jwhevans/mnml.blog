---
title: "Your Privacy Is Important to Me"
slug: "your privacy is important to me"
date: 2020-06-16T08:00:00-05:00
draft: false
publishdate: 2020-06-16T08:00:00-05:00
tags:
- privacy
- security
- thoughts
---

A few weeks ago I added a [dark theme][1] to the site. In that post I mentioned that I was using Google Analytics. It is extremely easy to add Google Analytics to a Hugo site. It is a cut and paste operation in two files.

I don’t know why I added analytics. A few days ago I was checking how fast my pages load. More than half of the page load time and 80% of the cpu cycles were from Google Analytics. The pages did not load slow. mnml is truly minimal in structure and it is a statically served site. Still, it bothered me. More than the unnecessary overhead, which is truly meaningless, was the fact that I was feeding your data to someone else. I am privacy conscious. I did not feel right sending your data to someone without your consent.

I decided to ensure that you can read this site freely without any undue concern for your privacy. First, I have removed Google Analytics from the site. Second, I have stopped writing access logs. I write this site for me. If you like something here and want to share, you can do it on your terms. Third, I am currently learning how to improve my security headers and content security policy to better protect anyone that browses this site.

[1]: https://mnml.blog/2020/05/mnml-supports-dark-mode/
