---
Title: Groff
Date: 2024-11-24
Category: linux
Tags: linux, command line, text, writing
Status: published
Slug: groff
Summary: An overview of GNU roff, a typesetting system.
---

<center>![Gnu]({static}/images/gnu.png){width=200}</center>

Groff (GNU roff) is a typesetting system which converts plain text input into output such as PostScript, PDF, and HTML.  This is achieved through the use of formatting commands peppered through each plain text file.  There are several different sets of macros that can be used with groff to format documents---I am most familiar with the _mom_ set of macros.

# Generating PDF Output
Output from a groff/mom file can be generated in several ways.  Most simply, assuming an extension of `.mom` for the plain text file then the `pdfmom` wrapper can be used to compile a PDF
```shell
pdfmom plaintext.mom > output.pdf  # Compile output.pdf from plaintext.mom
```

# Generating PostScript Output
Alternatively, to generate a PostScript file:
```shell
pdfmom -Tps plaintext.mom > output.ps  # Compile output.ps from plaintext.mom
```

# Missing Fonts Workaround
Recently, and for reasons I don't understand, the Palatino font has disappeared from the fonts available when compiling a PDF.  Groff's fonts are located at `/usr/share/groff/<version>/fonts/` and each output type appears to have its own fonts, located within discrete directories.  However, simply copying the Palatino font directories from the PostScript directory `devps` to the PDF directory `devpdf` doesn't fix the issue, because the resulting PDFs don't render the font correctly.

The "solution'' is to first generate PostScript output (which still works as intended where the Palatino font is used), and then to convert this PostScript file into a PDF using `ps2pdf` like so:
```shell
pdfmom -Tps plaintext.mom > output.ps  # Compile output.ps from plaintext.mom
ps2pdf output.ps output.pdf  # Convert the PostScript file to PDF
```

# External
[Mom documentation](https://www.schaffter.ca/mom/momdoc/toc.html)
