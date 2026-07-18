---
Title: Ocular
Date: 2026-07-15
Author: Wil Ifan
Category: photography
Tags: unix, photography, selfhosting, yunohost
Slug: ocular-pelican
Status: published
Summary: How to set up rostiger's 'ocular' to work with a Pelican site
Image:
---

My Yunohost instance has somehow bodged its install of php, which means I can't install any of the photo hosting services I previously used.  Despite my best efforts I can't fix this, and I don't want to do a clean install and start everything from scratch.

My search for an alternative led me to rostiger's superb [ocular](https://codeberg.org/rostiger/ocular).  This is how I got it working on my preexisting Pelican site.

# Installing and configuring ocular

Clone the repo from the above link and follow the instructions.  I use the following non-default options in the config file:

```lua
return {
	TITLE = "lluniau",
	...
	AUTHOR = "lluniau",
	URL = "https://oki.nohost.me/babel/ocular/",
	LANGUAGE = "en-GB",
	WEBSITE = "https://oki.nohost.me/babel/",
	WEBSITE_NAME = "The Library of Babel",
	REMOTE_DST = "oki:/ar/www/pelican/content/ocular/",
	...
	PROFILE_BIO = "A haphazard collection of photographs.",
	...
}
```
On the Pelican side of things, I have added the following to pelicanconf.py:

```py
# Search content/ocular for HTML files
STATIC_PATHS = ['ocular']
# Exclude ocular directory from content processing (already HTML format)
ARTICLE_EXCLUDES = ['ocular']
PAGE_EXCLUDES = ['ocular']
```

Don't set a custom path for ocular with `EXTRA_PATH_METADATA` otherwise the relative links break.  There's probably a way around this.
