---
title: "Connecting mnml to the IndieWeb"
slug: "connecting mnml to the IndieWeb"
date: 2021-06-28T08:00:00-05:00
draft: true
published date: 2021-06-28T08:00:00-05:00
tags:
- how-to
- indieweb
- twitter
- python
- hugo
---

I started this blog as a weekend project to learn about webservers. I’ve always been interested in posting my own content but mainly I enjoy learning new things and tinkering. I got the idea to host my own webserver on an extra Raspberry Pi and I moved the site inside for a while so that I could play with a solar cell and battery pack I had bought. It was a fun experiment and worked well. During covid I posted much more than ever before and I became more interested in making this a *semi*-permanent repository. 

I also started a Twitter account during covid. It was the first and only social network that I’ve created an account on. I’m quite happy with Twitter. I curate my timeline brutally. I mainly follow 3D printing and Green Bay Packers content. There are some nice people and I’ve found lots of great content.

I stumbled across Micro.blog through an episode of John Gruber’s “The Talk Show”. This was my first introduction to IndieWeb ideas and Manton Reece. I was impressed with his thoughtful posts regarding the problems with internet silos and the large information aggregators. This jives with my privacy concerns. The people on Micro.blog were also great and the climate of the site is wonderful. 

Because of these positive experiences and my desire to make this site my main internet repository, I decided to connect mnml.blog to the IndieWeb. I have spent weeks reading and playing. Last weekend I was ready to take on the challenge. I went full nerd mode for a couple days. I don’t develop for the web professionally. My skillset lies elsewhere but I pulled it off because there are a lot of talented people out there that were willing to share. This is what I did. If I did it, you can to. I hope this helps.

## Level 1 - Join the IndieWeb

#### personal domain - own your data
First you want to get your own domain. If you are reading this you have probably already taken this step. If you don’t yet have your own domain register for one. It is inexpensive and makes the site truly yours. There are many options. I like [Hover](https://www.hover.com/). I have no financial interest in them. They just offer a good experience and great customer service. [More Info...](https://indieweb.org/personal-domain)

#### web signin - one site to rule them all
Next you need to make sure your can use IndieAuth to use your website as your web sign in. This step may require a small change to your sites’ homepage. You need to link your social profiles to your site by adding with rel=me links. On my site I have a link to my social profiles in the footer section. I updated these links like this:

```
<a href=https://twitter.com/jwhevans rel=me>twitter</a>
<a href=https://github.com/jwhevans rel=me>github</a>
<a href=https://micro.blog/jwhevans rel=me>micro.blog</a>
```
Make sure that your profiles reference your website. [More Info...](https://indieweb.org/How_to_set_up_web_sign-in_on_your_own_domain) 

## Level 2 - Publish to the IndieWeb

## microformats - marking stuff up
Getting on the IndieWeb is pretty easy. If you are using Wordpress, Hugo, or other software your theme may support level one out of the box. Less templates have built in support for publishing. This requires that your html is marked up with [microformats](http://microformats.org/). I have found a few templates that are designed to support microformats. One very good one is [IndieFeed](https://github.com/microdotblog/indiefeed). I used IndieFeed to better understand the proper place to add microformats to my Hugo templates.

#### h-card  - who am I
Adding microformats allows other IndieWeb sites and software to parse and understand your site. It also allows level three social functions. First you will want to add an h-card to your site. This is kind of like your business card. It lets sites know who you are. I want sites to easily find my h-card on every page, but I don’t want to show it on the page directly. Again, I added the info to my standard footer template.

```
<div class="u-author h-card" style=display:none>
  <img src=https://mnml.blog/img/profile/headshot-grey.png class=u-photo width=40>
  <a href=https://mnml.blog/ class="u-url p-name">James Evans</a>
  <p class=p-note style=display:none>In a society that profits from your self doubt, liking yourself is a rebellious act.</p>
</div>
```
I implemented this a partial in Hugo so that it can be easily integrated anywhere on the site. That was important because I found that the easiest way for me to make list pages work properly was to include the h-card within each entry. The microformat markup is fairly simple. A `<div>` contains the card. You denote that this is an h-card by referencing the h-card class. u-author is another microformat denotes the author of the page or article. I don’t fully understand but it seems that microformat parsers need u-author before h-card in order to attribute the person on the card as the author. My card `h-card` contains a link to my photo `u-photo` my website `u-url` and a note `p-note`. [More Info...](http://microformats.org/wiki/h-card)

#### h-entry - my stuff
The next step is to markup your posts. By posts I mean your content. Whatever you publish is denoted with the h-entry class. This required a couple more changes to my site templates. I use Hugo so I had to change single.html and my list.html layouts.

Before changes
```
<article class="post">
  <header>
    <div class="p-name">
      <h1>{{ .Title }}</h1>
    </div>
  </header>
  <div class="content">
    {{ .Content }}
  </div>
  {{ partial "articleInfoFull.html" . }}
</article>
```
After changes
```
<article class="post h-entry">
  <header>
    <div class="p-name">
      <h1>{{ .Title }}</h1>
    </div>
  </header>
  <!-- h-card for webmentions -->
  {{ partial "myCardHidden.html" .}}
  <div class="content e-content">
    {{ .Content }}
  </div>
  {{ partial "articleInfoFull.html" . }}
</article>
```
Notice the addition of `h-entry`, `p-name`, and `e-content`. These classes denote to the parser that this is an entry (article), with a name (.Title), containing content (.Content). I also have a type of content on my site for short form notes. These don’t have titles so I add the `p-name` class to content. e.g `<div class="content e-content p-name"`

We are almost there. We need to tell others when our content was published. I already show the publish date on my site. I needed to modify the articleInfoFull.html file to include the proper microformat. The date needs to be in the ISO8601 format. Hugo doesn’t support this directly so I had to find some help to properly format the string. [tl;dr](https://ar.al/2018/06/17/formatting-an-iso-8601-date-stamp-in-hugo/). The [nitty gritty](https://gohugohq.com/howto/hugo-dateformat/).

Before changes
```
<div class="article-date">
  {{ .Params.date.Format "2006-01-02" }}
</div>
```
After changes
```
<div class="article-date">
  <time class="dt-published" datetime="{{ dateFormat "2006-01-02T15:04:05Z07:00" .Params.Date }}">
    {{ .Params.date.Format "2006-01-02" }}
  </time>
</div>
```
Using time allows for the datetime class to publish the necessary ISO8601 format while allowing you to display a different format on your site. [More Info...](http://microformats.org/wiki/h-entry)

## Level 3 - Socialize with the IndieWeb

## Resources
https://aaronparecki.com/2018/06/30/11/your-first-webmention
https://github.com/microdotblog/indiefeed
https://indiewebify.me/
https://github.com/bear/python-twitter/blob/master/examples/get_all_user_tweets.py
https://github.com/bear/python-twitter
https://indieweb.org
 
1. Indiewebify the site
- move canonical site to github
- h-card
- h-entry
- indiewebme
- - https://indiewebify.me/validate-h-entry/?url=https%3A%2F%2Fmnml.blog%2F2021%2F06%2Fapple-private-relay-is-tor-for-safari%2F
- site that helped me
- - https://aaronparecki.com/2018/06/30/11/your-first-webmention
- - https://github.com/microdotblog/indiefeed
2. Backport the silos
- save all tweets as json from bear
- then save only new tweets to the json file
- download all new tweets and format as shortcode in hugo
3. Add webmentions
- webmention.io
- micro.blog book ?
- .js for how it is done
4. Publish here and syndicate elsewhere
- implementing webpub
- what tools I use

[Python-Twitter by Bear][2]
[Backup all tweets][1]
Modified to only pull in new items.



[1]: https://github.com/bear/python-twitter/blob/master/examples/get_all_user_tweets.py
[2]: https://github.com/bear/python-twitter
