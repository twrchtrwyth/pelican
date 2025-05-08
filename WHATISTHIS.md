######################
# HOW DOES THIS WORK #
######################

This is the source code for my Pelican-based website. Pelican is a Python-based framework that--with the help of Jinja--converts Markdown files to HTML.

(Note: after updating the app on Yunohost may need to run `sudo chown -R wil *` within the pelican root directory to restore ownership and avoid issues when generating the site. Might need to do this specifically for the hidden git repo and gitignore too.)


## STRUCTURE

The content used to generate the site is split across a number of directories. These are described below.


### content

This directory contains the articles and static pages that are displayed on the website. They are in Markdown format. Images to be displayed in articles, etc., are also stored here.


### future-imperfect

This directory is where the theme information is stored. (The name of the folder is not important, other than the fact that it needs to match the one referenced in `pelicanconf.py`). Within this directory are two subdirectories: `static` and `templates`. The former includes things like fonts, style sheets, avatar images, etc. The latter contains templates for each type of page within the site, which allows customising the layout of, for example, articles. The `includes` directory defines things that appear in the sidebar.


### Makefile

I've never touched this, not sure exactly how changing it will affect things.


### output

Contains the formatted website.


### pelicanconf.py

Many core settings are defined in this file, such as the name of the site, default author, and the URL. Also where links in contact section are defined, pagination, format of article summaries, etc.
