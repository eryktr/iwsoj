#!/usr/bin/env bash

set -e;
cd /runner;
export GOPATH=$(pwd);
go run target.go < input.txt;
