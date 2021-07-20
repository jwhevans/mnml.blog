---
title: "Using Automator for Quick Google Translate Queries"
slug: "using automator for quick google translate queries"
date: 2021-01-06T20:00:00-05:00
draft: false
publishdate: 2021-01-06T20:00:00-05:00
tags:
- apple
- mac
- automation
- applescript
---

I work for a company with global offices. Many of my colleagues speak German as their primary language. We often need to translate words and documentation between languages. Google translate is still not a substitute for a professional translation, but it is helpful. I find myself cutting and pasting words and phrases to it all the time.

Today I decided that I should automate the task. <!--more-->The Automator application on macOS allows for the creation of “services” that run automation from any app. I created an automation that takes selected text as an input and then sends that text to Google Translate directly. This saves several steps.

![Automator Workflow](/img/automator-google-translate.jpg)

First I created a new “Quick Action” within Automator. Then from the “Utilities” Library I added an action to “Run Applescript”. The script takes the selected text as an input. I create a variable called “site” that uses the input parameter to properly format the Google Translate URL. Translating between other languages is as easy as updating the letters following ?sl= and &tl=. For example, German to English is `?sl=de&tl=en` while English to German is `?sl=en&tl=en`.

After saving and installing the workflow should be available anywhere in the system by selecting some text, then right clicking and opening the “Services” context menu. A new Safari window will open to translate.google.com with your word already translated.
