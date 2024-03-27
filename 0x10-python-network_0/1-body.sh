#!/bin/bash
# Sends a GET request to the URL, and displays the body 
curl -s -o /dev/stdout -w "%{http_code}" "$1" | awk 'NR==1 && $1==200 {next} {print}'
