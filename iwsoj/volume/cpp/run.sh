#!/usr/bin/env bash

set -e;
cd /runner;
g++ target.cpp -o ./exec;
chmod +x ./exec;
./exec < input.txt;