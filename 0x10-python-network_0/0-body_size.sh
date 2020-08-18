#!/bin/bash
# Display the body size of URL response
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
