#!/usr/bin/env bash

set -e;
cd /runner;
javac target.java;
java Main < input.txt;