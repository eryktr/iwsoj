#!/usr/bin/env bash

set -e;
cd /runner;
g++ target.cpp -o ./exec;
chmod +x ./exec;
./exec < input1.txt;
echo __SPLIT_PLACEHOLDER__;
./exec < input2.txt;