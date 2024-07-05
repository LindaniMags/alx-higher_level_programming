#!/bin/bash
# Displays the size of the URL body in bytes
curl -s "$1" | wc -c
