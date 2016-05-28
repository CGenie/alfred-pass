#!/bin/bash

set -e

QUERY=$1
PATH=/usr/local/bin:$PATH

pass generate "$QUERY" -n 20 -c 
