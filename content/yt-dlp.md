---
Title: yt-dlp
Date: 2026-08-12 08:27
Author: Wil Ifan
Category: linux
Tags: command line, terminal, linux
Slug: yt-dlp
Status: published
Summary: How to download YouTube videos with yt-dlp
---

<<<<<<< HEAD
[yt-dlp][] is a superb tool which lets you download video and/or audio directly from YouTube via the command line.  I am yet to test this with YewTube.
=======
[yt-dlp][] is a superb command line tool which lets you download video and/or audio directly from YouTube.  I am yet to test this with [YewTube][].
>>>>>>> c9a9b00 (*)

For a basic no-frills download of a video (note that the additional cookies flag is required otherwise the download fails):

```bash
yt-dlp url --cookies-from-browser firefox
```

To download as a specific format:

```bash
yt-dlp -t mkv url --cookies-from-browser firefox
```

Or to just download audio:

```bash
yt-dlp -t mp3 url --cookies-from-browser firefox
```

To download a whole playlist:

```bash
yt-dlp -o yt-dlp -o %(playlist_index)s - %(title)s.%(ext)s https://music.youtube.com/playlist?list=PLE8333C6A8D37F371 --cookies-from-browser firefox
```

To crop audio from a longer video, use [ffmpeg][]:

```bash
# From beginning
ffmpeg -to time-in-seconds -i long-file.mp3 short-file.mp3
# From specific point
ffmpeg -ss start-time-in-sec -to end-time-in-sec -i long-file.mp3 short-file.mp3
```

<<<<<<< HEAD
[yt-dlp]: https://github.com/yt-dlp/yt-dlp
[ffmpeg]: https://ffmpeg.org/
=======
To edit metadata, either use [MusicBrainz Picard][picard] or [beets][]

To inspect metadata of the files (requires [mutagen][]):

```bash
mutagen-inspect filename.mp3
```

[yt-dlp]: https://github.com/yt-dlp/yt-dlp
[YewTube]: https://yewtu.be/
[ffmpeg]: https://ffmpeg.org/
[picard]: https://picard.musicbrainz.org/
[beets]: https://beets.readthedocs.io/en/stable/reference/cli.html
[mutagen]: https://mutagen.readthedocs.io/en/latest/
>>>>>>> c9a9b00 (*)
