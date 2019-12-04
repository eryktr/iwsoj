#!/usr/bin/env bash

set -e;
cd /runner;
python3 target.py < input1.txt;
echo __SPLIT_PLACEHOLDER__;
python3 target.py < input2.txt;
