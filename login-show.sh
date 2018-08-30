#!/bin/bash

set -e

QUERY=$1
PATH=/usr/local/bin:$PATH

pass show "$QUERY" | /usr/bin/sed -E -n '/login|user/p' | /usr/bin/sed -E -e 's/(login: |user: )*//' | pbcopy
osascript -e 'display notification "Copied username to clipboard" with title "Unix pass"'
