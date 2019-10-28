#!/usr/bin/env bash

cd /runner;
export GOPATH=$(pwd);
go run target.go;
