#!/bin/bash
# Sends a POST request with email and subject variables
curl -sd "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X "POST" "$1"
