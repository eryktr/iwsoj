#!/usr/bin/env bash

set -e;
cd /runner;
export GOPATH=$(pwd);
go run target.go < input1.txt;
echo __SPLIT_PLACEHOLDER__;
go run target.go < input2.txt;