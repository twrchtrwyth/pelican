Title: Markdown Syntax Testing
Date: 2022-09-11
Category: markdown
Slug: markdown
Status: hidden
Summary: This post will test how Pelican's Markdown rendering engine handles some of Markdown's advanced features.

## Strikethrough (doesn't work)

This bit of text ~~is wrong~~ is right.

## Links

[This is a generic link](https://duckduckgo.com)

[This is a generic link, but try hovering the mouse](https://duckduckgo.com "Look, a tooltip!")

[This is a reference style link][Put what you like here]

[Here is another using a number instead of text for the definition][1]

Here is another link where [this bit of text is the link].

In the unrendered document, below this line are the links to some of those specified above.

[put what you like here]: https://duckduckgo.com
[1]: https://duckduckgo.com
[this bit of text is the link]: https://guybrushthreepwood.noho.st/the-library-of-babel/index.html

## Images

Can use similar syntax to the reference-style links above.

![Jasper][jasper pic]

Here, in the unrendered document, the link to the above picture is visible:

[jasper pic]: https://guybrushthreepwood.noho.st/lychee/uploads/small/32e59f1be6c32bdda482b2f303ef8a04.JPG

## Footnotes

This is how you do footnotes[^1].

You can also use text instead of a number for the footnote[^hello].

See the bottom of the file for the footnotes.

[^1]: Here is the first footnote.
[^hello]: This might make it easier to keep track of them. Footnotes will always render as numbers.

## Tables

| Here | Is | My |
| ---- | --- | --- |
| Table | Of   | Stuff    | 

## Linking to a heading {#heading-id}

I

Will

Pad

Things

Out

A

Bit

Then

Try

Returning

To

The

Above

Heading

Using

A

[Link](#heading-id)

## Definition lists (kind of works)

Here is the Term
: And here is the definition.

## Checklists (doesn't work)

- [X] Test unusual markdown syntax
- [ ] Make sure it all works

## Highlighting (doesn't work)

This is not important, but ==this is==.

## Subscript (doesn't work)

H~2~O

## Superscript (doesn't work)

E = mc^2^

## Using HTML Tags

### Abbreviations

This is an <abbr title="Abbreviation">abbr</abbr>--try mousing over.

### Acronyms

Let's discuss <acronym title="Leukocyte Adhesion Deficiency">LAD</acronym> syndrome, which has been described as "living under a microbial Sword of Damocles." (Mouse over to see the tooltip.)

### Definitions

Here is an example of a <dfn title="Sausages">definition</dfn>. (Again, mouse over for the tooltip.)

### Highlighting (doesn't work)

To do this we <mark>use the mark element</mark>.

### Strikethrough

Natural is <s>best</s> just as dangerous as any group of chemicals.

### Small text (doesn't work)

I want to say the last part of this sentence <small>really quietly</small>.

### Subscript

C<sub>2</sub>H<sub>6</sub>O is a widely consumed psychoactive substance.

### Superscript

E = mc<sup>2</sup>
