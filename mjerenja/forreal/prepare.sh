#!/bin/bash

scp pi@10.42.0.62:/home/pi/Documents/Seminar/python-lis3dh/$1 .
tail -n +19 $1 > $1_nice
python plotter.py < $1_nice
