#!/bin/bash

echo "Destruindo a stack"

aws cloudformation delete-stack --stack-name StackOverflowed


echo "Esperando a stack ser destruida"

aws cloudformation wait stack-delete-complete --stack-name StackOverflowed

echo "Stack destruida"

echo "Prazer fazer negócio com você, Demay."