---
Title: WHAT IS THIS
Date: 2022-09-05
Category: about
Tags: about
Status: published
Slug: about
Summary: Abandon all hope ye who enter here, etc.
Image: oki.png
Caption: Oki on the mantelpiece
---

After a number of false starts, this is my--hopefully--final attempt to host my own website. Each previous attempt has proved unsatisfactory for a number of reasons. Initially I tried using Wordpress but didn't like the feeling that I wasn't truly in control of my site data. Next came [Jekyll][], which involved boilerplate code in languages with which I am unfamiliar. When I ran into problems (which were, admittedly, almost certainly of my own making) I realised that I don't have the time or inclination to learn a whole new language just for a silly little hobby project. (Also, my Jekyll site is hosted through Github, which again feels somewhat like giving up control.) Finally, I discovered [Pelican][] after stumbling across [LowTech Magazine's website][lowtech]. Being somewhat familiar with Python, it seemed a good fit.

[jekyll]: https://jekyllrb.com/
[pelican]: https://getpelican.com/
[lowtech]: https://solar.lowtechmagazine.com/

The website is hosted on `oki`, my trusty little Raspberry Pi 3B+ server (named after the sentient diving suit from the wonderful [In Other Waters][iow]), with the help of [Yunohost][].  Nowadays I do much of the work on the site using my Dad's old Thinkpad X60s, which he very kindly gifted to me some years ago.  It's still pretty nippy despite its age (it was first released while I was still doing my GCSEs!) thanks to antiX Linux, an SSD and a RAM upgrade.

[iow]: https://www.fellowtraveller.games/in-other-waters/
[yunohost]: https://yunohost.org/

The theme is a modification of Pelican's "simple" theme, and represents a continuous (and somewhat Sisyphean) work in progress as I stumble my way through the morass that is CSS syntax.

I used to use [GIMP][] to resize and dither (Image> Mode> Indexed, 1-bit Floyd-Steinberg) my images, but now I use [didder][].

[gimp]: https://gimp.org
[didder]: https://github.com/makew0rld/didder

```bash
didder --palette "black white" -i input.jpg -o output.png bayer 16x16
# or
didder -i input.png -o output.png --palette "black white" --recolor "black F273FF" \
--upscale 2 bayer 4x4
```

The primary purpose of the site is help me record little tidbits of information that I've learned about Linux, in a somewhat *ad hoc* fashion.  However, I am supportive of the idea of a "small web", and believe that most modern website design is unwieldy, overcomplicated, dull and impersonal.  SEO had likely already sounded the death knell for a creative internet, but AI slop is only making things worse at an accelerated rate.  With this in mind, this site represents my pitifully small and undoubtedly entirely ineffectual way of fighting back, armed with nothing but my extremely rudimentary knowledge of HTML and CSS (the site intentionally does not use JavaScript).  In line with this--and with my morals in general--the site does not, nor will it ever, include any adverts, analytics, or any other such bullshit that has killed the modern web. 
