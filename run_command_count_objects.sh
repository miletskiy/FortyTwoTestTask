#!/bin/bash

clear

SETCOLOR_SUCCESS="echo -en \\033[1;32m"
SETCOLOR_FAILURE="echo -en \\033[1;31m"
SETCOLOR_NORMAL="echo -en \\033[0;39m"
NAME_FILE=$(date +"%d_%m_%Y")

echo
echo -e '\t\t\tHi, '$USER!
echo -e '\t\tThis script will run the django-admin command count_objects.'
echo -e '\tThe command creates file with information about project models.
\tYou can find it with name '$NAME_FILE'.dat'
echo
echo -n 'Run? (yes/no) '

read

if [[ $REPLY == 'y'||$REPLY == 'yes' ]]; then
    python manage.py count_objects 2> $NAME_FILE.dat
    if [[ -e $NAME_FILE.dat ]]; then
        $SETCOLOR_SUCCESS
        echo 'File succefully created.'
        echo -e '\t\t\t[OK]'
        $SETCOLOR_NORMAL
    else
        $SETCOLOR_FAILURE
        echo 'Something went wrong'
        $SETCOLOR_NORMAL
    fi
else
    $SETCOLOR_FAILURE
    echo 'Run command was cancelled.'
    $SETCOLOR_NORMAL
fi
