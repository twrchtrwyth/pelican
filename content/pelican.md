---
Title: Customising a Pelican Site
Date: 2025-06-07
Author: Wil Ifan
Category: pelican
Tags: pelican, website
Slug: pelican
Status: published
Summary: Moving away from Pelican's boring default site design.
Image:
Caption:
---

# Changing the home page

By default, Pelican uses the `index.html` template as the home page of the site.  To override this, create a markdown file (e.g. `home.md`) in the `pages` directory of the `content` folder and include the following in the YAML frontmatter at the top of the file (note how URL is blank):

```yaml
URL:
save_as: index.html
```

A different URL which points to the `index.html` template can be specified.  This means it's still possible to access the running list of articles via this new URL.  For example, I have changed it by adding the following to `pelicanconf.py`:

```python
INDEX_SAVE_AS = "articles.html"
```

Relevant part of [Pelican Docs][home-page].

[home-page]: https://docs.getpelican.com/en/latest/faq.html#how-can-i-use-a-static-page-as-my-home-page

# Adding new templates

Pelican only allows direct linking to certain HTML template pages by default.  For example, I wanted to allow direct access to my `pages` template, which generates an up-to-date list of all pages on my site each time the site is generated, which avoids me having to manually maintain a page which does this (though to be honest, this probably wouldn't be the hardest thing in the world).  In order to do so, after creating the file `pages.html` in the `templates` directory, I added `pages` to the end of the following list in `pelicanconf.py` so that the list now looks as follows (the other items in the list are Pelican's defaults):

```python
DIRECT_TEMPLATES = ['index', 'authors', 'categories', 'tags', 'archives', 'pages']
```

Relevant part of [Pelican Docs][templates].

[templates]: https://docs.getpelican.com/en/stable/settings.html#template-pages

# External

Lots of information on Pelican's variables, etc., on [this site][cat].

[cat]: https://www.thedigitalcatonline.com/blog/2021/03/25/how-to-write-a-pelican-theme-for-your-static-website/
