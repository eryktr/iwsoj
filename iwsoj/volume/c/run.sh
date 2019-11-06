#!/usr/bin/env bash

set -e;
cd /runner;
gcc target.c -o ./exec;
chmod +x ./exec;
./exec < input.txt;