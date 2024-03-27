#!/bin/bash
# Sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | awk '/Content-Length:/ {print $2}' && [ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1
