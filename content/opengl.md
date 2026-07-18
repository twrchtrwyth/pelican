---
Title: OpenGL on Arch Linux
Date: 2026-05-15
Author: Wil Ifan
Category: linux
Tags: linux, arch, opengl
Slug: opengl-arch
Status: published
Summary: How to fix errors with OpenGL on my Thinkpad X220 running Arch
Image:
---

When trying to load Factorio on my old Thinkpad X220, an error would display relating to `glxbadfbconfig`.

In order to fix this, run:

```
export LIBGL_ALWAYS_SOFTWARE=true
```

Or add this to `~/.profile` for it to be executed on startup.
