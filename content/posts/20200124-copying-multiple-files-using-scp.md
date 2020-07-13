---
title: "Copying Multiple Files Using SCP"
slug: "Copying Multiple Files Using SCP"
date: 2020-01-24T22:26:10-05:00
draft: false
publishdate: "2020-01-24"
tags:
- how-to
- command-line
- raspberry pi
---

There are many ways to copy files between a local and remote server. I am very often working on a Macbook Pro connected to a Raspberry Pi. Since I am already in the terminal the secure copy (scp) utility is handy.

*Syntax to copy from the MacBook Pro to the Pi*

    scp file pi@raspberrypi.local:~/incoming

* scp is the secure copy utility
* file is the file on the local machine
* pi@raspberrypi.local is the name of your pi
* ~/incoming is where you are moving the file
  
*Syntax to copy from the Pi to the Macbook Pro*

    scp pi@raspberrypi.local:file ~/incoming

I've never been a command-line ninja, but it seemed that there must be a way to copy multiple files at once. As it turns out scp works just like cp.

    scp file1 file2 pi@raspberrypi.local:~incoming

This will copy both file1 and file2 from the local machine to the pi. Similarly,

    scp pi@raspberrypi.local:"file1 file2" ~/incoming

will copy file1 and file2 from the pi to the local machine. Notice that "" are required around the files. If you want to copy a directory and all files it is possible to invoke the recursive flag -r

    scp -r ~/dir1 pi@raspberrypi.local:~/incoming
    scp -r pi@raspberrypi.local:~/dir1 ~incoming

Finally, Linux doesn't play nice with blanks in file names. You can escape a blank using a backslash (e.g. "File 1.txt" becomes "File\ 1.txt").
