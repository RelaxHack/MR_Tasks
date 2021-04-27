#!/bin/bash

if [[ "$1" == "-h" ]]; then
echo "The input parameters for the script: list of PIDs of processes that"
echo "we want to monitor and the interval at which the measurements"
echo "would be taken in seconds."
echo "Without interval!! Only key's or list of PIDs through "","" and time"
echo "Exit from script through key --exit "
exit $?
fi

if [[ "$1" == "--exit" ]]; then
del=$(ps -eo cmd,pid | grep -i writing_script | awk '{print $3}')
kill $(echo $del | awk '{print $1}')
exit $?
fi

count=1
PID=""
for var in $(echo $1 | awk 'BEGIN{RS=","} {print $1}')
do
if [ $(./check_validity.sh $var) == "NOOK" ]
then
echo $var" incorrect PID" >> err_log.txt
else
if [ "$count" == "1" ]
then
PID+=$var
else
PID+=","$var
fi
count+=1
fi
done

if [ "$PID" == "" ]
then
echo "All of PID's is incorrect" >> err_log.txt
./main_script.sh -h
exit $?
fi

if [ -n "$3" ]; then
  echo "Incorrect input parameters" >> err_log.txt
./main_script.sh -h
exit $?
fi

./writing_script.sh $PID $2 &

