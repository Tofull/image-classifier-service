#!/bin/bash

## Get the path of the script
SCRIPT=`realpath -s $0`
SCRIPTPATH=`dirname $SCRIPT`

## Insert new alias into bashrc file
echo "alias classify_path=\"python3.5 $SCRIPTPATH/messed_path_to_classify.py\""  >> ~/.bashrc

## Update the configuration
source ~/.bashrc

echo "created alias"
