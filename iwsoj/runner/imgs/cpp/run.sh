#!/bin/bash

cd /runner
g++ target.cpp -o ./exec
chmod +x ./exec
./exec