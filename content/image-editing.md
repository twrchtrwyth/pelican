---
Title: Image Editing via the Command Line
Date: 2023-03-28 19:20
Category: linux
Tags: photos, imagemagick, command line, terminal
Slug: image-editing
Status: published
Author: Wil Ifan
Summary: A short guide to the imagemagick suite of tools.
---

This is a very quick guide covering how to use the `imagemagick` set of tools in Unix. This may need to be installed via your distro's package manager.

## Getting info about an image

The `identify` command will print some information about an image to stdout, including its dimensions.

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

## Cropping an image

To crop an image in the simplest sense use the following (probably not the most useful example ):

```shell
$ identify image.jpg
image.jpg JPEG 1280x960 1280x960+0+0 8-bit sRGB 209774B 0.000u 0:00.000 
$ convert image.jpg -crop 1280x800+0+0 image-cropped.jpg  # This crops from the bottom
```

The values after the image dimensions are used to tell imagemagick where to begin cropping (and in which direction?). These values can be negative.

To quickly crop an image, use the `shave` command. This example will crop 100 pixels from top and bottom (to crop from the sides, change the integer before the `x`):

```shell
magick image.png -shave 0x100 image-shaved.png
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
