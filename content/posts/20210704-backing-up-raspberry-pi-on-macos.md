---
title: "Backing Up Raspberry Pi on MacOS"
slug: "backing up raspberry pi on macos"
date: 2021-07-04T11:00:00-05:00
draft: false
publishdate: 2021-07-04T11:00:00-05:00
tags:
- MacOS
- raspberry pi
- 3d printing
---

I’ve been fortunate to have never lost any data in my computing life. It is fortunate because it will happen. No matter how good your backup system is it will happen eventually. I have always been able to fall back on a second, third, or in some cases, forth copy of data. I use a lot of Raspberry Pis. They are all booting off of MicroSD cards. They are notorious for dying because the SD cards are not designed for significant read/write cycles. It is important to back them up. Even if you don’t save important information on them it will save you countless hours in setup time. It isn’t hard to do. Below are my steps on a Mac.

From terminal find the SD card.
```
>> diskutil list
```
You should have several devices (/dev/disk*) listed. Find the one that matches your SD card. Mine is /dev/disk2

Copy the SD card to your Mac.
```
>> sudo dd if=/dev/disk2 of=/users/name/backup-directory/backup-file.dmg
```
*if* is the input file. *of* is the output file. You can save this anywhere you like on your system. This can take several minutes to an hour depending on the size of the card. Don’t interrupt the process if it takes a long time. That is normal.

To restore to another SD, unarchive the file, run the same command, but reverse the input and output files.
```
>> sudo dd if=/users/name/backup-directory/backup-file.dmg of=/dev/disk2 
```
All my Pis use 32Gb drives. I don’t want a bunch of 32Gb files so I archive the backups in Finder after this process is completed.

I’m most concerned with backups for the systems that run my 3D printers. I run Octoprint and stream video on all my printers. I don’t want to go through the setup process if I lose a card. Last year I moved all these systems from Raspian to DietPi. DietPi is much smaller and allows for a RAMDisk with minimal logging. This is less taxing on the SD card. I have not lost an SD card since moving to DietPi. 

{{< rawhtml >}}
<a href="https://brid.gy/publish/twitter"></a>
{{< /rawhtml >}}
