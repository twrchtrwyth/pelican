---
Title: Grep
Date: 2024-01-28
Category: linux
Tags: linux, command line, bash
Status: published
Slug: grep
Summary: A brief overview of the grep command in bash.
---

The `grep` command is used to search files for a user-specified string.

## Search a file

Use the `i` flag to ignore case. The `v` flag displays only non-matching lines.

```shell
grep [-iv] search-string filename
```

## Searching directories recursively

Use a capital `R` to also follow symbolic links.

```shell
grep -r search-string directory
```

## Searching for whole words only

```shell
grep -w search-string filename
```

## Multiple search terms

```shell
grep -E [-w -i] "first-term|second-term" filename
```

## Searching with patterns

This matches any of the characters within the brackets.

```shell
grep -e first-term -e [tT]est filename
```

## Show only exactly matching lines

```shell
grep -x "exact search string" filename
```

## Show only lines that don't exactly match

This is useful for showing file contents without the comments. Can pipe to e.g. less, or just display in the command line.

```shell
grep -v "#" filename
```

## Just show matching text in output

```shell
grep -o search-string filename
```

## Count number of occurrences of search string

```shell
grep -c search-string filename
```

## Show line number of matches

```shell
grep -n search-string filename
```

## Limiting output

This will show the first five matching results.

```shell
grep -m5 search-string filename
```

## Showing some context around matches

This example uses the `x` flag which only returns matching lines, but this is not required to display context.

### Show lines after

Shows the next three lines after the match:

```shell
grep -A 3 -x "exact search string" filename
```

### Show lines before

Shows the three lines before the match:

```shell
grep -B 3 -x "exact search string" filename
```

### Show lines before and after

Shows the three lines before and after the match:

```shell
grep -C 3 -x "exact search string" filename
```

## Show file names containing match

```shell
grep -l "search-string" *.extension
```

## Show file names NOT containing match

```shell
grep -L "search-string" *.extension
```

## Only match start of line

This will show lines which have a space as the first character:

```shell
grep "^ " filename
```

## Only match end of line

This will show lines ending with `00`:

```shell
grep "00$" filename
```

## Piping grep example

This will return files last modified in August (or with "Aug" in their name), sorted by file size (the 4th column of the output of `ls-l`):

```shell
ls -l | grep "Aug" | sort +4n
```
