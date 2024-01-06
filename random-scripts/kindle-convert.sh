#!/bin/bash
# Convert all jpgs in current dir to kindle PW3 format

resultdir=converted

mkdir -p $resultdir

for filename in *
do
  basename="${filename%.*}"
  suffix="${filename##*.}"
  if [[ "${suffix,,}"  == 'jpg' ]]
  then
    echo "Converting file '$filename'"
    convert "$filename" -rotate 90 -resize 1072x1448 -colorspace Gray "$resultdir/${basename}.png"
  else
    echo "Ignoring file '$filename'"
  fi
done
