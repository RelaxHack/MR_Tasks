#!/bin/bash
echo "Entered password: " $1
alphabetic=$(echo $1 | awk '/[[:alpha:]]/{print $0}')
numeric=$(echo $1 | awk '/[[:digit:]]/{print $0}')
punct=$(echo $1 | awk '/[[:punct:]]/{print $0}')
length=$(echo $1 | awk '{ print length($0) }')
if [ $length -ge 8 ]
then

if [ $alphabetic == $1 ]
then

if [ $numeric == $1 ]
then

if [ "$punct" == "$1" ]
then
echo "Password is OK"
else
echo "Must contain at least one of the following non-alphabetic characters:"
echo "  @, #, $, %, &, *, +, -, ="
fi

else
echo "Must contain at least one numeric character"
fi

else
echo "Must contain at least one alphabetic character"
fi

else
echo "Minimum length of 8 characters"
fi
