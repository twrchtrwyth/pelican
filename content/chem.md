---
Title: The chem preprocessor
Date: 2023-06-26
Author: Wil Ifan
Category: linux
Tags: chemistry, groff
Slug: chem
Status: published
Summary: Some examples of chemical structures drawn using groff's chem preprocessor.
Image: morphine.png
Caption: Morphine, so named for Morpheus, Ancient Greek god of dreams
---

Here are some moderately complex chemical structures created using groff's `chem` preprocessor. [Groff]({filename}groff.md) is a document formatting system included with most Linux distros.

I will show the structure above the block of code from which it was generated. To generate the images, as per the `chem` manpage I ran the following command, adding the redirect to a postscript file:

```shell
chem filename | groff -p > filename.ps
```

I then used [imagemagick]({filename}image-editing.md) to convert them to the `png` format.

## Benzylpenicillin

![benzylpenicillin]({static}/images/benzylpenicillin.png)

```groff
.fam C
.\" Benzylpenicillin.
.cstart
.\" Creates the 5-sided heterocyclic ring.
R1: ring5 pointing right put N at 3 put S at 5
.\" Creates the beta-lactam ring.
bond left length 0.264 from R1.N
double bond -135 ; O
bond left length 0.324 at R1.V4 ; BP
bond down length 0.3
.\" Start of wedge bond.
.\" Angle of nw is 315, or -45.
.\" Really this should probably be slightly further clockwise.
front bond nw length 0.22 from BP
N
.\" This then continues the molecule from the nitrogen atom.
bond 250 ; BP
bond 295
bond 250
R2: ring double 2,3 4,5 6,1
double bond 180 from BP ; O
.\" Adds the methyl groups to the heterocyclic ring.
bond 55 from R1.V1
bond 125 from R1.V1
.\" Creates the acetyl group.
back bond 145 from R1.V2 ; BP
double bond 90 ; O
bond 215 from BP ; HO
.\" This comes last to avoid the bond from the earlier N originating at the H.
H at N + (0, 0.12)
.\" Adds the molecule name at the specified position.
.fam P
"Benzylpenicillin" at N - (0, 1.2)
.cend
```
