---
title: "Enable TouchID for sudo password in Terminal"
slug: "enable touchid for sudo password in terminal"
date: 2021-11-29T13:00:00-05:00
draft: false
publishdate: 2021-11-29T13:00:00-05:00
tags:
- command line
- macOS
---

TouchID on the newer macs is one of those features that I didn't know I needed and now can't live without. Any computer that doesn't have it now feels broken. One place where it wasn't available by default was the terminal. I do a fair amount of terminal work and I found that it is possible to enable TouchID support. This allows you to enter your sudo password via TouchID. To enable it edit /etc/pam.d/sudo with your favorite editor.

```
$ sudo vim /etc/pam.d/sudo
```

Then add the following line at the top of the file.

```
$ auth sufficient pam_tid.so
```

Restart your terminal and TouchID is available.
