---
Title: Using Tmux
Date: 2022-09-27 09:55
Category: linux
Tags: command line, terminal
Status: published
Summary: A primer on using the tmux terminal multiplexer
---

Tmux is a terminal multiplexer: it allows running multiple terminal emulators in a single window. It is especially useful for me when SSHing into `oki`.

This post covers just a few basic tmux operations.

## Launching tmux

This is pretty easy... Just run `tmux`

## The status bar

From left to right, here is an explanation of the contents of the status bar.

1. Session name within square brackets (by default, these are numbered, but see below section on starting a named session)
2. Window numbers within the session. To the right of each colon is the currently running process. If no program is running, the name of the shell (e.g. `bash`) will be displayed
3. The asterisk indicates the session currently being viewed
4. Over on the right side of the bar is the hostname and the time and date

## Running tmux commands

Type `Ctrl+B` then quickly hit the desired key.

## Getting help

`Ctrl+B` then `?` will display the help page.

## Starting a named tmux session

To do this, use `tmux new -s name-of-session`

### Renaming a session

`Ctrl+B` then `$`

## Managing windows

### Closing the current window

Hit `Ctrl+B` then `x`. A confirmation prompt will appear.

### Adding new windows

Hit `Ctrl+B` then `c`

### Navigating between windows

Hit `Ctrl+B` then one of the following:

* `n` to display the next window
* `p` to display the previous window
* `0-9` to display windows numbered from 0 to 9

### Renaming windows

`Ctrl+B` then `,` will allow renaming of the current window.

### Listing all windows

To do this use `tmux ls`

### Showing a tree of all windows

Hit `Ctrl+B` then `w` These can be navigated using the vi keys.

### Splitting windows into panes

#### Horizontal

To do this, use `Ctrl+B` then `"` This only acts on the current window: any others within the session remain unaffected.

#### Vertical

Use `Ctrl+B` then `%`

#### Navigating between panes

To navigate between split windows, hit `Ctrl+B` then the arrow keys (vi keys do not work). Alternatively, use `Ctrl+B` then `o` to cycle through each in turn.

#### Showing the number of each pane

`Ctrl+B` then `q` will briefly display a number over each pane.

#### Moving panes

`Ctrl+B` then `{` or `}` will swap the pane with the previous or next one, respectively.

#### Closing panes

As with closing windows, use `Ctrl+B` then `x`

## Detaching and attaching sessions

### Detaching

Use `Ctrl+B` then `d` to detach the current session. The session will continue to run in the background, but is not visible and cannot be interacted with.

### Attaching

Use `tmux attach-session -t name-of-session`. The `-t` flag stands for the `target session` option. The detached session can then be interacted with.

## Managing sessions

Within a tmux session, use `Ctrl+B` then `s` to see a list of all tmux sessions. These can be navigated using the vi keys. Press right to open a tree of windows within a session. Press `Esc` to cancel.
