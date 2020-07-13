---
title: "How-To Install Security Updates: Ubuntu and Debian"
slug: "how to install security updates ubuntu and debian"
date: 2020-06-29T08:00:00-05:00
draft: false
publishdate: 2020-06-29T08:00:00-05:00
tags:
- command-line
- hobbies
- how-to
- raspberry pi
---

I run a few systems with Debian based distros. It is normal to log on to the system and see that updates are available. When this happens I run the typical

```
sudo apt-get update && sudo apt-get upgrade
```
Ocassionally, the security updates do not install. When this happens the unattended-upgrades package is beneficial. Most Debian based distros have this package already. If it is not available it can be installed with the following command.

```
sudo apt-get install unattended-upgrades
```
Once available security updates can be installed.

**Silent**

```
sudo unattended-upgrades
```
**Verbose Logging**

```
sudo unattended-upgrades -d
```
There are several ways to ensure that security updates are applied to your systems without your intervention. Ubuntu offers the canonical livepatch service. This is a paid service and has the added benefit of not requiring as many system reboots. I prefer to schedule the unattended-upgrades as a cron job. I am already rebooting my systems regularly. Uptime is not my biggest concern.
