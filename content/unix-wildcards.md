---
Title: Unix Wildcards
Date: 2024-03-03
Author: Wil Ifan
Category: linux
Tags: command line
Slug: unix-wildcards
Status: draft
Summary: An overview of wildcards in bash.
---

# Wildcards

| Wilcard | Meaning |
| ------- | ------- |
| `*`       | Matches any character |
| `?`       | Matches any single character |
| `[characters]` | Matches any character that is a member of the set *characters* |
| `[!characters]` | Matches any character that is *not* a member of the set *characters* |
| `[[:class]]` | Matches any character that is a member of the specified *class* |

# Character Classes

| Character Class | Meaning |
| --------------- | ------- |
| `[:alnum:]`       | Matches any alphanumeric character |
| `[:alpha:]`       | Matches any alphabetic character   |
| `[:digit:]`       | Matches any numeral                |
| `[:lower:]`       | Matches any lowercase letter       |
| `[:upper:]`       | Matches any uppercase letter       |

# Examples

