#!/bin/bash

echo "Starting the cloud server"

# Start the cloud server

aws cloudformation create-stack --stack-name StackOverflowed --template-body file://cloud.yaml --capabilities CAPABILITY_IAM

echo "Cloud server started"

aws cloudformation wait stack-create-complete --stack-name StackOverflowed

output=$(aws cloudformation describe-stacks --stack-name StackOverflowed --query "Stacks[0].Outputs[?OutputKey=='ALBDNSName'].OutputValue" --output text)

echo "DNS da Stack: $output"

echo "para acessar a aplicação, use o link acima"