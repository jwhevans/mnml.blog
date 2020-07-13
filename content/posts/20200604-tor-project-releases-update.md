---
title: "Tor Browser 9.0 Released"
slug: "tor browser update released"
date: 2020-06-04T08:00:00-05:00
draft: false
publishdate: 2020-06-04T08:00:00-05:00
tags:
- security
---

The [Tor Project][1] has released version 9.0 of their privacy and anonymity focused Tor Browser. I do not use the Tor Browser often but have found it useful on some trips outside the United States. Downloading and installing the Tor Browser is no different than downloading any other software. If you download from the official website and have verified that the site is secured then everything should be ok. However, Tor is the type of application that bad actors like to get their hands on and it makes sense to take the extra step of verifying the is legitimate. On macOS you will need a copy of [GPGTools][2].

After installing GPGTools and downloading both files from the Tor webpage (.dmg and .asc), open your terminal and copy the following:

```
gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
```

This may take a little while. Just sit patiently and you will see something like this

```
gpg: key 4E2C6E8793298290: public key "Tor Browser Developers (signing key) <torbrowser@torproject.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1
pub   rsa4096 2014-12-15 [C] [expires: 2020-08-24]
      EF6E286DDA85EA2A4BA7DE684E2C6E8793298290
uid           [ unknown] Tor Browser Developers (signing key) <torbrowser@torproject.org>
sub   rsa4096 2018-05-26 [S] [expires: 2020-09
```

Now copy the following command to create a keyring file. Replace the items after 0x with the pub key from your return statement

```
gpg --output ./tor.keyring --export 0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290
```

Now check the key to ensure that it is valid. I saved the files in my local Downloads folder. Adjust the path as necessary.

```
gpgv --keyring ./tor.keyring ~/Downloads/TorBrowser-9.0-osx64_en-US.dmg.asc ~/Downloads/TorBrowser-9.0-osx64_en-US.dmg
```

If everything is ok you will receive a message like this

```
gpgv: Signature made 07/08/19 04:03:49 Pacific Daylight Time
gpgv:                using RSA key EB774491D9FF06E2
gpgv: Good signature from "Tor Browser Developers (signing key) <torbrowser@torproject.org>"
```

[1]: https://www.torproject.org/download/
[2]: https://gpgtools.org
