#!/usr/bin/env bash

set -e;
cd /runner;
gcc target.c -o ./exec -lm;
chmod +x ./exec;
./exec < input.txt;