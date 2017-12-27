#!/bin/bash

Xvfb :1 -screen 0 1024x768x24 &
export DISPLAY=:1

for j in 0 5 10 50 100 200 300 400 500 ; do
    for i in `ls gens/${j}/ | grep -v result | grep -v mp4` ; do
        echo $i
        file="gens/${j}/${i}"
        if ! [ -f "${file}.mp4" ] ; then
            ffmpeg -video_size 1024x768 -framerate 30 -f x11grab -threads 8 -i :1.0 ${file}.mp4 2>&1 > /dev/null &
            ./main.py $file 2>&1 > /dev/null
            pkill ffmpeg
        fi
    done
done

pkill Xvfb
