#!/bin/bash
rm output.txt
string='08 22 0a 00 05 00 c7'
for i in $string; do
printf "\x${i}" >> output.txt
done
cat output.txt > /dev/ttyUSB0
