#!/bin/bash
# Send a POST request with the contents of a file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
