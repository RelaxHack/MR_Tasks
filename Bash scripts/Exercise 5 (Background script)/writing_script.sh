#!/bin/bash

#Creating an archive for future filling
time_watching=$2
echo "Hello to my script" >> Intro.txt
tar -cf archive.tar Intro.txt
rm Intro.txt
touch output.csv
file1=1
file2=2
file3=3
file4=4
file5=5
h=1
PID=$(echo $1 | awk 'BEGIN{FS=",";ORS=" "} i = 1 {while(i <= NF){print $i; i++}}')
#Main cycle
while [ 0 -ne 1 ]
do

#Checking for the size of the main file
size=$(wc -c output.csv | awk '{print $1}')
if [ $size -ge 500000 ]
then
mv output.csv save$h.csv
touch output.csv

#Check for five files
if (( $h % 5 == 0 ))
then
tar -uf archive.tar save$file1.csv save$file2.csv save$file3.csv save$file4.csv save$file5.csv
rm save$file1.csv
rm save$file2.csv
rm save$file3.csv
rm save$file4.csv
rm save$file5.csv
file1=$(( $file1 + 5 ))
file2=$(( $file2 + 5 ))
file3=$(( $file3 + 5 ))
file4=$(( $file4 + 5 ))
file5=$(( $file5 + 5 ))
fi
h=$(( $h + 1 ))
else
#Checking for executed PIDs
for check_of_pid in $PID
do
temp=$(ps -fp $check_of_pid -o pid | awk 'NR == 2{print $0}' | awk 'BEGIN{OFS=","} {print $1}')
if [ "" == "$temp" ]
then
echo "$check_of_pid completed or does not exist" >> err_log.txt
PID=$(echo $PID | sed "s/$check_of_pid//")
fi
done

if [ "" == "$PID" ]
then
echo "All of PIDs are completed" >> err_log.txt
exit $?
fi

#The main part of collecting information
for regular_pid in $PID
do
collector=$(date +%F)","$(date +%T)","
collector+=$(ps -fp $regular_pid -o pid,%cpu,%mem,time,stat | awk 'NR == 2{print $0}' | awk 'BEGIN{OFS=","} {print $1,$2,$3,$4,$5}')
parent=$(pgrep --parent $regular_pid | awk 'BEGIN{FS="/n"} {print NR}' | awk '{line=$0} END{print line}')
if [ "" == "$parent" ]
then
collector+=",0"
else
collector+=","$parent
fi
echo $collector >> output.csv
done
sleep $time_watching

fi

done

