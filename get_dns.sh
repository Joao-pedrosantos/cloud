#!/bin/bash
# get_dns.sh
# Example script to get the DNS
# Replace this with the actual command to retrieve your DNS

aws cloudformation describe-stacks --stack-name StackOverflowed --query "Stacks[0].Outputs[?OutputKey=='ALBDNSName'].OutputValue" --output text
