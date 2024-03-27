#!/bin/bash
# Script that takes an URL and shows the Allowed
curl -sI "$1" | grep -i Allow | cut -d " " -f 2 -
