---
title: "Archive Email and Jump to Next in Outlook 2016 Using Applescript"
slug: "Archive Email and Jump to Next in Outlook 2016 Using Applescript"
date: 2018-12-20T20:26:10-05:00
draft: false
published date: "2018-12-20"
tags:
- programming
- applescript
---

Our exchange server stopped playing nice with Mail.app after macOS Mojave was released. I use Microsoft Outlook when I’m on my office desktop and it’s supported by the IT department so I installed it on my Mac as well. Outlook for Windows has a great feature set. When it is properly setup it is possible to triage email quickly. Outlook for Mac is missing almost everything that makes its Windows counterpart useful.

In particular, on Windows it is possible to open the first email in a folder, perform some action such as reply, forward, archive, delete and the next message in the folder will open as soon as this action is completed. All of this can be accomplished from the keyboard. Mix this with a utility such as [www.goodtodo.com][1] and you have the makings for a mean email productivity system.

I’ll write more about my method to manage email later. Reply and Forward are available with shortcut keys just as they are on Windows, but I can’t easily archive and delete while simultaneously moving to the next message. I’ll show how I used AppleScript to add some of the functionality that I’m missing. First, I needed a script to read, archive and move on.

    use AppleScript version "2.4" -- Yosemite (10.10) or later
    use scripting additions

    tell application "Microsoft Outlook" 
        set theMessages to every message in selected folder 
        set numMessages to count of theMessages 
    
        if numMessages > 1 then 
            set Message1 to item numMessages of theMessages 
            set Message2 to item (numMessages - 1) of theMessages 
            set is read of Message1 to true 
            move Message1 to folder "Archive" 
            close window 1 
            open Message2 
        else 
            set Message1 to item numMessages of theMessages 
            set is read of Message1 to true 
            move Message1 to folder "Archive" 
            close window 1 
        end if 
    end tell

After telling the script that we want to control “Microsoft Outlook” we grab all the messages in the current folder and count them. *I admit that this is not an optimal solution for many people. I keep my inbox very clean. If you keep a large number of emails in your inbox this script will hang your system. One solution is to modify the code to only pull the selected message and the next message.*

As long as there are multiple messages in the folder we get the current message Message1 and the next message Message2. *Note: I sort my folders by receipt date from oldest to newest. You may have to adjust the index to pull the correct message.* Then we mark Message1 as read and move it to the Archive folder. You can change this to meet your workflow. Finally, we close the window and open the next message.

If there is only one message in the folder then there is no need to open Message 2 and we can just quit. Deleting is even easier. Modify the above code. Replace:

    move Message 1 to folder “Archive"

with

    delete Message 1

Finally, I saved these scripts and added a keyboard shortcut using [FastScripts][2]. This is a quick and dirty solution. I’ll optimize it and add some other functionality later. [Let me know][3] if you have a better solution.

[1]: https://goodtodo.com/
[2]: https://red-sweater.com/fastscripts/
[3]: mailto:james@jwhevans.net
