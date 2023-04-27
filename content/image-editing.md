---
Title: Image Editing via the Command Line
Date: 2023-03-28 19:20
Category: linux
Tags: linux, photos
Slug: image-editing
Status: published
Author: Wil Ifan
Summary: A short guide to the imagemagick suite of tools.
---

# Imagemagick

This is a very quick guide covering how to use the `imagemagick` set of tools in Unix. This may need to be installed via your distro's package manager.

## Converting between formats

```shell
convert image.png [-quality 95] image.jpg
```

## Resizing images

Will try to preserve aspect ratio by altering image to fit within the area specified, but may not end up as the exact area. To force a specific size, add an exclamation mark after the dimensions.

```shell
convert image.png -resize 200x100[!] image.png
```

Alternatively can just specify width or height and `imagemagick` will resize the image whilst preserving aspect ratio.

```shell
# height
convert image.png -resize 200 image.png
# width
convert image.png -resize x100 image.png
```

## Rotating an image

Need to specify new image name, otherwise imagemagick saves the rotated image over the original image file.

```shell
convert image.png -rotate 90 image-rotated.png
```

## Batch processing

```shell
for file in *.png; do convert $file -rotate 90 rotated-$file; done
```
