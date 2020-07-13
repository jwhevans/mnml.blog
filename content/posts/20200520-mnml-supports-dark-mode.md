---
title: "mnml Now Supports Dark Mode"
slug: "mnml supports dark mode"
date: 2020-05-20T10:49:44-05:00
draft: false
publishdate: 2020-05-20T10:00:00-05:00
tags:
- article
---

I've been planning to add dark mode to the site for a while but hadn't taken the time to parameterize my html code. I didn't like the initial results. The contrast was striking and images were too bright for the new background. I did some reading and found that adjusting the opacity and rollover effects for the images would help. Dialing back the text color also helped. 

One issue fought me for several weeks. On new page loads the screen flashed white for a split second and then loaded properly. It was such an annoyance that I could not bear to roll it out. I looked all over the web for a solution that did not include javascript. I wanted a pure css solution. Several people on StackOverflow recommend adding a style tag to the html header 

    <html>
      <head>
        <style>html{visibility:hidden;opacity:0}</style>
        ...
        *load stylesheet here*
        <style>html{visibility:visible;opacity:1}</style>
      </head>
    ...
    
This solution did not work for me. It stopped the flash but also stopped all content from rendering. There were several solutions that required variations on the style tag in the header. None of these worked.

Since I'm generating a static site I could not understand why there would be a flicker. It seemed that this should only happen if the browser is waiting to render. My pages are very small and they are static html. Rendering should start almost immediately. I opened the web inspector on my live site and quickly found the problem. I forgot that I had added a google analytics key to my config file. My site is not fully static. A piece of javascript is inserted into each page when I create the html. I had not noticed it on the development site. In development I run in "Fast Render Mode". The files are live and updated as changes are saved. The analytics connection is never created but there is a delay while Hugo decides what to do with the code.

The solution was to move my stylesheet before the javascript injection. Flicker problem solved! So now mnml has a dark mode. There is not a manual toggle. It is implemented using 

    @media (prefers-color-scheme: dark)

If your system supports dark mode then you will see the dark mode version whenever your system dark mode is enabled and light mode otherwise. 
