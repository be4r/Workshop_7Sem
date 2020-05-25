#!/bin/bash

if [ "$1" = '' ] || [ "$2" = '' ] || [ "$3" = '' ]; then
	echo -e "\nYour input should look like:\n\n\t$0 <filename> <dir> <time>"
	echo -e "where:\n\t<filename>\t- name of python script u wanna run"
	echo -e "\t<dir>\t\t- path to directory where script output is collected"
	echo -e "\t<time>\t\t- expected duration of program in seconds\n"
	exit
fi

(time ( bash -c 'echo "Downloads/aac" | python3 '$1' &>/dev/null' &>/dev/null) 2>&1 &)

slp=$(python3 -c "print($3/50.0)")
for((i = 0; i <= 50; i ++)); do
    echo -en "\r"
    echo -n '['
    for((j = 0; j < i; j ++)); do
        echo -n '#'
    done
    for((j = i; j < 50; j++)); do
        echo -n '|'
    done
    echo -n ']'
    sleep $slp
done
echo -en "\r\x00\x00"
for((i = 0; i <= 52; i ++)); do echo -en ' '; done
echo -en "\r"
killall -9 "python3"
sleep 1
echo "Converted $(ls -R $2 | grep 'npy' -c) files"
