#!/usr/bin/env bash

set -e;
cd /runner;
python3 target.py < input.txt;
