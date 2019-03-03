#!/bin/bash
string='08 22 00 00 00 02 D4'
rm output.txt
for i in $string; do
printf "\x${i}" >> output.txt
done
cat output.txt > /dev/ttyUSB0
