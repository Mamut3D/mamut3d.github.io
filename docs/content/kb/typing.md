+++
title = "Typing"
+++

## Typing speed improvement

I was looking for a tool which would help  me increase my typing speed, long story short. The best one I found is [wpm](https://pypi.org/project/wpm/) written in python.

```bash
# installation
pip3 install wpm

# usage
wpm
```

## Single hand practice

To practice single hand typing you need a list of words for single hands and import it to wpm ideally as json. In this repo there is a simple python script which can generate a wpm file for a hand of your choice pre-filled with

```bash
# write out help from script
./python/wmp_single_hand_gen.py -h

# generate right hand file for wpm
./python/wmp_single_hand_gen.py -H right > right.json

# use right hand file with wpm
wpm --load-json right.json
```
