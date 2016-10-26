[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

# ig-bot 

## Python3 Instagram grey hat bot (for demonstration purposes only). It is not meant to be used 

This is an instagram bot for demonstration purposes, it does the following:

### Likes and Follows

- select a favourite hashtag
- search for medias with that hashtag
- for each found recent media (unless ~20 people are followed)
	- if the author has less than FOLLOWERS_THRESHOLD followers
		- like its most recents medias (~10)
		- follow that user
- sleep an hour circa

### Image Posting


the bot will post an image on each scheduled time, the description will be the original page title plus the chosen hashtag plus some related hashtag

### Log on Twitter

The bot will tweet whenever it follows an user, sleep after some follows, post an image or when it crash.


<div align="center" markdown="1"> 
<img src="doc/dawg.jpg" alt="I heard you like bots"/>
</div>


# Usage

phase 1:

- choose images to post with the chrome extension, right click on it -> Gram It Later -> select the hashtag

phase 2:

- run python bot/main.py
- check your twitter account or your terminal

# Setup

- hashtags files: you need a file 'hashtags' and 'relatedhashtags' in this directory, containing one hashtag for line.

- put the relative exports in your .profile for instagram credentials, twitter tokens, and the gram it later folder.

- open the movefiles workflows with Automator and set the Chrome's download folder and the gramitlater folder (if you aren't on MacOS, create a script to move gramitlater files after download or set the gramitlater folder as your chrome's download folder).

# Requirements

- python3
- tweepy
- Instagram-API-Python

# Why?

because I love coding and automating things.

# License

MIT

# Terms and conditions

- This bot is for demonstration purposes only.
- Instagram-API-Python doesn't meant to be used as bots.
- You will NOT use this bot for marketing purposes (spam, massive sending...).
- We do NOT give support to anyone that wants this bot to send massive messages or similar.
- We reserve the right to block any user of this repository that does not meet these conditions.

## Legal

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Instagram or any of its affiliates or subsidiaries. This is an independent and unofficial API. Use at your own risk.

