---
title: LaTex
---

## Installation

Termux texlive [docs](https://wiki.termux.com/wiki/TeX_Live).

```bash
# Termux
pkg install texlive-installer

# Install texlive
termux-install-tl

# You will now be shown texlive's install-tl text gui.
# You can customize settings, but you have to use the
# default TEXDIR and custom binaries or else texlive
# is unable to find and run the binaries.
#
# Press 'c' to continue
#
# Don't change anything and pres 'c', then 'I' and enter :-)

# Wait bazilion years for installation.

# Some scripts need to be fixed before they will work in termux.
#     The script termux-patch-texlive will now be run to try to fix
#     known problems. If your texlive breaks in the future after running
#     tlmgr update --all
#     then you might be able to fix it by running this script.

# To build pdf from LaTex `.tex` file use
pdflatex <filename>.tex
```
> I had an issue, where my `HISTSIZE=` in `~/.bashrc` for unlimited history file caused texlive install to crash. I have fixed it by temporarily setting `HISTSIZE=1000000` and sourcing `~/.bashrc`.
