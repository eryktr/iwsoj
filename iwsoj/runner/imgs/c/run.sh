#!/bin/bash

cd /runner
gcc target.c -o ./exec
chmod +x ./exec
./exec