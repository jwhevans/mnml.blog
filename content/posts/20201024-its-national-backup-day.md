---
title: "It’s National Backup Day"
slug: "its national backup day"
date: 2020-10-24T08:00:00-05:00
draft: false
publishdate: 2020-10-24T08:00:00-05:00
tags:
- raspberry pi
- 3D printing
---

Just kidding. If you haven’t backed up your raspberry pi lately, today is a good day to do it. I just backed up and then upgraded DietPi to version 6.33.3.

If you haven’t done this in a while. Go to the Finder.

```
diskutil list
```

Find your SD card. It should be something like /dev/disk2. It may be comprised of some logical drives as well, e.g. disk2s1, etc. *Don’t blindly copy and paste the code below. Check your disk names!*

```
sudo dd if=/dev/rdisk2 of=~/printserver-backup.dmg
```

or

```
sudo dd if=/dev/rdisk2 | gzip >printserver-backup.gz
```

You can do this in reverse to restore a backup but you have to remember to unmount the card. I prefer to write my backups to the card using Balena Etcher.
