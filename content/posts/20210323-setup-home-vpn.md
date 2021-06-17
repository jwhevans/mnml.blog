---
title: "Setting up home VPN on TP-Link Routers"
slug: "setting up home vpn on tp link routers"
date: 2021-03-23T22:00:00-05:00
draft: false
publishdate: 2021-03-23T22:00:00-05:00
tags:
- how-to
- network
- vpn
---

I added a new 3D printer to my workspace last week. This week I added a [Raspberry Pi][1] and connected it to [Octoprint][2]. I was previously connecting to my other pinter from outside my home network through port forwarding on my modem/router and haproxy. It was better than leaving the Octoprint instance open to the internet but wasn't ideal.

With multiple printers I thought it would be best to give each its own dedicated Raspberry Pi and Octoprint instance. I also wanted to separate the authentication layer on my network from the print servers. TP-Link has Wi-Fi 6 capable routers that are affordable and well reviewed by The Wirecutter. They have several advanced functions including the option to setup a VPN server on the router. I bought an [AX1500][3] and setup an OpenVPN server.

My internet service provider is AT&T. They are the only option in my area. One good thing about their service is that I can have a static ip address at no extra charge. I don't believe the address is actually static. They accomplish this through some sort of networking magic that I don't understand but it makes the VPN setup easier. If you have AT&T then these steps will work for you as well.

First, setup the TP-Link router according to its installation instructions. After setup, log on to your modem. An AT&T modem is normally accessible by navigating to 192.168.1.254 from a web browser. If this does not work, consult your installation documents for the modem.

The modem configuration screen should have a navigation bar similar to this

![AT&T Navigation Bar](/img/vpn-setup-1.png)

Navigate to the Firewall Tab and then to IP Passthrough. You will need your device Access Code to enter this area. This is a good time to mention that if you aren't using a password manager get one. I use 1Password. Pick what you want but get one.

![AT&T Firewall Settings](/img/vpn-setup-2.png) 

You are going to change the Allocation Mode to **Passthrough**, the Passthrough Mode to **DHCPS-fixed** and then select your Router from the Device List dropdown box. Save these settings. Then restart your modem.

Now we need to setup the OpenVPN connection on the router. Log on to the router at tplinkwifi.net. There is a menu bar similar to this

![TP-Link Navigation Bar](/img/vpn-setup-3.png)

Click on the Advanced Tab. Now select VPN Server from the Sidebar and Select OpenVPN.

![TP-Link Sidebar](/img/vpn-setup-4.png)

Click on the **Enable** checkbox. Select UDP or TCP. Select a service port and adjust the Subnet and mask if needed. **There isn't really a need to change anything here.** Select your access type. Home Network only will give you access to file and folder shares but no internet. Internet and Home Access also allows internet access. This is useful if you travel and need to get around location restrictions.

Now click **Generate** to create a certificate and profile. This will take a few seconds to a few minutes depending on your system. When it is complete a message will appear stating that the process completed successfully. Now **Export** the certificate/profile. This will download the file to your system as a .ovpn file. Save the file. It must be imported into your OpenVPN client.

There are many clients that work with OpenVPN. I prefer OpenVPN connect. It is available on the [iOS App Store][4] and can be [downloaded directly][5] for other platforms. Follow the installation instructions and then import your .ovpn file into the app. 

[1]: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
[2]: https://octoprint.org
[3]: https://www.walmart.com/ip/TP-Link-Archer-AX1500-Wi-Fi-6-Dual-Band-Wireless-Router-up-to-1-5-Gbps-Speeds-1-5-GHz-Tri-Core-CPU/584566855
[4]: https://apps.apple.com/us/app/openvpn-connect/id590379981
[5]: https://openvpn.net/download-open-vpn/
