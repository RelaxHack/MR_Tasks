#!/bin/bash
echo "PID or process name: "
echo "PID - 1"
echo "Process name - 2"
echo -n "Choice: " ; read choice
echo -n "Enter your data: " ; read input_1
echo -n "Time: " ; read input_2
echo "CPU,MEM" > process_watch_file.csv
case "$choice" in
1)
for ((a = $input_2;a > 0; a--))
do
ps -fp $input_1 -o %cpu,%mem | awk 'NR == 2{print $0}' | awk 'BEGIN{OFS=","} {print $1,$2}' >> process_watch_file.csv
sleep 1
done
;;
2)
for ((a = $input_2;a > 0; a--))
do
ps -eo %cpu,%mem,cmd --sort=-%cpu | grep -i $input_1 |
awk 'NR == 1{print $0}' |
awk 'BEGIN{OFS=","} {print $1,$2}' >> process_watch_file.csv
sleep 1
done
;;
esac
