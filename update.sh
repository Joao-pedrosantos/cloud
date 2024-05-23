#!/bin/bash


echo "Updating the stack"

aws cloudformation update-stack --stack-name StackOverflowed --template-body file://cloud.yaml --capabilities CAPABILITY_IAM

aws cloudformation wait stack-update-complete --stack-name StackOverflowed

echo "Stack updated!"