#!/usr/bin/env bash

cd /runner;
gcc target.c -o ./exec;
chmod +x ./exec;
./exec < /runner/input.txt;