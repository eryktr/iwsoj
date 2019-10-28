#!/usr/bin/env bash

cd /runner;
g++ target.cpp -o ./exec;
chmod +x ./exec;
./exec;