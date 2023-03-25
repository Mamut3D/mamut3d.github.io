+++
title = "Imagemagick"
+++

## Installation and usage


ImageMagick is a free, open-source software suite, used for editing and manipulating digital images. It has lot of cli utilities bundled in. This page serves as a kb for ones, which I found useful.

```bash
# install imagemagick for termux
pkg install imagemagick

# rotate image
mogrify -rotate 90 image.jpg

# resize image
mogrify -resize 50% image.jpg
mogrify -resize 256x256 image.jpg

# change format
mogrify -format png image.jpg
```
