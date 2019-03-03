#!/bin/bash
string='08 22 02 00 00 00 D4'
rm output.txt
for i in $string; do
printf "\x${i}" >> output.txt
done
/dev/ttyUSB0 < output.txt
