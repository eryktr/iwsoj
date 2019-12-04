#!/usr/bin/env bash

set -e;
cd /runner;
javac target.java;
java Main < input1.txt;
echo __SPLIT_PLACEHOLDER__;
java Main < input2.txt;