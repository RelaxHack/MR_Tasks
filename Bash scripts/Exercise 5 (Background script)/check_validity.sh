#!/bin/bash

alphabetic=$(echo $1 | awk '/[[:alpha:]]/{print $0}')
numeric=$(echo $1 | awk '/[[:digit:]]/{print $0}')
punct=$(echo $1 | awk '/[[:punct:]]/{print $0}')

if [ "$alphabetic" != "$1" ]
then

if [ "$punct" != "$1" ]
then

if [ $numeric == $1 ]
then
check="OK"

else
check=="NOOK"
fi

else
check="NOOK"
fi

else
check="NOOK"
fi

echo $check
