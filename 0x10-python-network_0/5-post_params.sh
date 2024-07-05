#!/bin/bash
# Post request that is sent two variables
curl -s -X POST --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
