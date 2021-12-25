---
title: "Shortcuts for Text Translation"
slug: "shortcuts for text translation"
date: 2021-11-03T14:00:00-05:00
draft: false
publishdate: 2021-11-03T14:00:00-05:00
tags:
- apple
- mac
- shortcuts
- automation
---

Earlier this year I posted an [Automator workflow](https://mnml.blog/content/posts/using-automator-for-quick-google-translate-queries/) that sent text to Google Translate. As I mentioned then, I work for a company with global offices and I have to make quick translations often. I used the workflow regularly. It rarely fails and has saved me a considerable amount of time. I can also translate text on my iOS devices but it requires more steps. I’m now running Apple Silicon Macs exclusively and macOS Monterrey includes the shortcuts app. It was relatively simple to build a translation shortcut that is cross platform. 

![Translate Shortcut](/img/translate-shortcut.png)

The shortcut is fairly basic. It only uses built-in commands.

1. Take selected text as input. Make it available in Share Sheet (iOS) and Quick Actions (macOS available in Services menu).
2. Save the text to a variable.
3. Use the built-in Microsoft translation function.
4. Save the translated text to a variable.
5. Save the translated text in the clipboard for later use if needed.
6. Output the original text and the translated text.

![Translated Text Example](/img/translated-text.png)

I created a generic version that allows for a choice of translated language and a version for quick translation to English and German. These are my most frequently used languages.

![Services Menu](/img/translate-services-menu.png)

Thanks to the cross platform support this is now also readily available on iOS in the share sheet which eliminates several steps and app changes.

![Share Sheet](/img/translate-share-sheet.png)
