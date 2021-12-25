---
title: "Connecting to Oracle from Python on M1 Mac"
slug: "connection to oracle from python on m1 mac"
date: 2021-12-03T11:00:00-05:00
draft: false
publishdate: 2021-12-03T11:00:00-05:00
tags:
- mac
- python
- programming
- oracle
- M1
---

[I've written previously about using the cx_Oracle package to connect Python scripts to an Oracle database.](https://www.mnml.blog/2020/12/connecting-to-oracle-from-python-on-macos-big-sur/) After moving to an M1 Mac I encountered errors with my connection again.

cx_Oracle currently has no ARM compatible version. It will install without error alongside Python and other packages that are compiled for ARM. It will throw an error at runtime stating that the version x86_64 is not compatible the system architecture.

If anyone knows of a cx_Oracle binary that was compiled for the M1 I would appreciate a pingback. For now the simplest solution was to install an x86_64 version of Python. Create a virtual environment using Python x86_64. Then run all my scripts in this environment.

I use Homebrew. Homebrew installs in ```/opt/Homebrew``` by default on M1 Macs and will install ARM versions of software when available. I created a second Homebrew install specifically for x86_64.

This requires Rosetta 2. It is possible that it already installed. It will automatically install the first time you try to run an x86_64 application but will not automatically install if you perform installations via the terminal. To install,

```
$ software-update --install-rosetta
```

Agree to the license and then install Homebrew for x86_64

```
$ arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

This will create another Homebrew installation in the typical ```/usr/local/Homebrew``` directory. To install x86_64 packages here just pass the architecture flag to brew install

```
$ arch -x86_64 brew install *package_name*
```

After installing Python I created a virtual environment with the necessary package dependencies and then everything worked fine.

```
$ /usr/local/bin/python3.9 -m venv *environment_name*
$ source ./*environment_name*/bin/activate
$ pip install *package*
```