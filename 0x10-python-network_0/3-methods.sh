#!/bin/bash
# Script that takes an URL and shows the Allowed OPTIONS
url -sI "$1" | grep -i Allow | cut -d " " -f 2 -
