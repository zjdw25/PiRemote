#!/bin/bash
string='08 22 0d 00 00 1f aa'
rm output.txt
for i in $string; do
printf "\x${i}" >> output.txt
done
cat output.txt > /dev/ttyUSB0
