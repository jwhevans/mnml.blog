---
title: "AppleScript to Save Open Tabs to Reading List"
slug: "applescript to save open tabs to reading list"
date: 2020-10-09T12:00:00-05:00
draft: false
publishdate: 2020-10-09T12:00:00-05:00
tags:
- applescript
- programming
---

I am not good at keeping my Safari windows clean. It is not unusual for me to have three or four windows upen with tabs that look like this.

![Safari](/img/safari_bar.jpg)

Maybe this isn’t the best way to work, but it’s how I work. I only have two problems. The first is the utter catastrophe when I accidentally Cmd-Q. [John Gruber has a nice Applescript to solve this problem][1]. The second problem is more an annoyance. Sometimes I need to restart my computer. There are cases where the system will reload open windows. There are cases where it won’t. In general I don’t trust the system to open all my tabs after a restart.

The reading list is a good place to save the open tabs but adding them manually is a waste of time. AppleScript lets us automate this process.

```
tell application "Safari"
	
	set windowCount to number of windows
	
	repeat with x from 1 to windowCount
		set tabcount to number of tabs in window x
		
		repeat with y from 1 to tabcount
			set tabName to name of tab y of window x
			set tabURL to URL of tab y of window x
			add reading list item tabURL with title tabName
		end repeat	
	end repeat
end tell
```

After running this script all the open tabs from every window are safely stored in the Safari reading list and can be opened again after the system reboots.

[1]: https://daringfireball.net/2020/01/quit_confirmation_for_safari_on_macos
