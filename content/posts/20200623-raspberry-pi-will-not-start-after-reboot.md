---
title: "Raspberry Pi Doesn’t Start After Reboot"
slug: "raspberry pi does not start after reboot"
date: 2020-06-23T08:00:00-05:00
draft: false
publishdate: 2020-06-23T08:00:00-05:00
tags:
- raspberry pi
- 3D printing
---

I was on vacation last week. As is the case for so many people this was a *staycation*. I spent a lot of time with my kids. We read books. We built Lego. We drew. We painted. We made stress balls out of water ballons and water absorbant beads. We swam almost every morning and evening. We also did some 3D printing.

The printing went well for the most part. Most of the prints were downloads from Thingiverse. My youngest is a Pokemon fan currently. My oldest loves all things Star Wars. I’m a terrible organic modeller so I steal with pride. We lost one print all week. I think some greasy fingers got on the build plate and we lost a Pokemon.

I ran into a problem one morning that I haven’t faced before. After grabbing my coffee I removed the previous night’s print. Everything was good so I logged onto my Octoprint server to start the next job. There were updates available so I ran them and then did a normal server reboot. I’m running DietPi on a Raspberry Pi 4

```
sudo shutdown -r now
```

My SSH connection terminated and I glanced over at the Pi to watch the LED status lights. The red LED came back on almost immediately. The green LED that normally blinks during startup was off. I gave the system about 5 minutes but nothing happened. I hate to pull the power to my Pi’s. The SD cards are notorious for going bad and mine are no exception. I could have loaded a backup card but I prefer to check that the existing card is truly dead before I go that route. I pulled the plug, waited a minute, and gave it power again. No luck. The problem persisted.

I sat back and thought about the problem for a bit. It didn’t make sense that the card was bad. I have far less issues with cards running DietPi than Raspbian. I have the system setup with no logs and push everything to RAM that I can. I’m checking the disk for bad sectors on a scheduled reboot weekly. The only thing that has changed in my setup since the last reboot of the Pi is a new set of drivers for the printer. I couldn’t imagine why this would matter but I pulled the USB cable and rebooted. The system started up with no problems.

I checked the disk again and it was in good shape. I made an image and backed it up to my Mac. Then I tried the whole process again. Sure enough I can’t reboot the Pi while it is plugged into the printer unless the printer is turned off. I have a first generation Pi 4 hooked up to the system and they do not perform well with certain power supplies. I am using a proper power supply but if the power is not maintained above 4.6 VDC during startup the system will fail to boot. I don’t know what has changed, but something in the Prusa 3.9 driver updates seems to pull some power on the USB when the system is on. It is sufficient to stop the Pi from booting.

If you run into the same problem, I’d be interested to know if this solution works for you. If you have a different solution I would also be interested to know. It isn’t a big deal but it is annoying.
