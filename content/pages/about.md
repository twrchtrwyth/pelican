---
Title: About this site
Date: 05/09/2022
Category: about
Tags: about
Status: published
Slug: about
Summary: Abandon all hope ye who enter here, etc.
Image: oki.png
---

After a number of false starts, this is my--hopefully--final attempt to host my own website. Each previous attempt has proved unsatisfactory for a number of reasons. Initially I tried using *Wordpress* but didn't like the feeling that I wasn't truly in control of my site data. Next came *Jekyll*, which involved boilerplate code in languages with which I am unfamiliar. When I ran into problems (which were, admittedly, almost certainly of my own making) I realised that I don't have the time or inclination to learn a new language just for a silly little hobby project. (Also, my Jekyll site is hosted through *Github*, which again feels somewhat like giving up control.) Finally, I discovered *Pelican* after stumbling across [LowTech Magazine's website](https://solar.lowtechmagazine.com/). Being somewhat familiar with Python, it seemed a good fit.

|![OKI]({static}/images/oki.png){width=250}|
|:-:|
|The website is hosted on `oki`, my little Raspberry Pi 3B+ server (named after the sentient diving suit AI from the wonderful [*In Other Waters*](https://www.fellowtraveller.games/in-other-waters/)), with the help of [Yunohost](https://yunohost.org/).|

I don't really know what to do with the site... It will probably serve as an *ad hoc* repository of things I learn, most likely largely relating to Linux and programming. I might chuck in some thoughts about computer games that I've enjoyed, too. And there will undoubtedly be vampire squid.

The theme is [Future Imperfect](https://html5up.net/future-imperfect) by HTML5 UP, which I have tweaked, but not properly implemented because I can't write HTML properly yet. I think I have changed the code block appearance from default and want to change it back, but can't remember how I did this. There used to be an image of the server at the top of this page, but it's disappeared. I don't know why.

I used to use GIMP to resize and dither (Image>Mode>Indexed, 1-bit Floyd-Steinberg) my images, but now I use [`didder`](https://github.com/makew0rld/didder):

```bash
didder --palette "black white" -i input.jpg -o output.png bayer 16x16
# or
didder -i input.png -o output.png --palette "black white" --recolor "black F273FF" --upscale 2 bayer 4x4
```
