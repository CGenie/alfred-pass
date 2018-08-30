#!/bin/bash

set -e

QUERY=$1
PATH=/usr/local/bin:$PATH

# GPG agent
envfile="$HOME/.gnupg/gpg-agent.env"
if [[ -e "$envfile" ]] && kill -0 $(grep GPG_AGENT_INFO "$envfile" | cut -d: -f 2) 2>/dev/null; then
    eval "$(cat "$envfile"); export GPG_AGENT_INFO"
else
    eval "$(gpg-agent --daemon --write-env-file "$envfile")"
fi

# PASS
#pass otp "$QUERY" | awk 'BEGIN{ORS=""} {print; exit}' | pbcopy
pass otp -c "$QUERY"
osascript -e 'display notification "Copied OTP key to clipboard" with title "Unix pass"'
