#!/usr/bin/env bash

set -e


QUERY=$1
PATH=/usr/local/bin:$PATH

AUTOTYPE_field='autotype'
default_autotype="user :tab pass"
URL_field='url'
USERNAME_field='user'

allData="$(pass show $QUERY)"

function doType {
  echo "tell application \"System Events\" to keystroke \"$1\"" | osascript
}

function doStroke {
  echo "tell application \"System Events\" to key code $1" | osascript
}

declare -A stuff
pass_key_value=$(printf '%s\n' "${allData}" | tail -n+2 | grep ': ')
while read -r LINE; do
	_id="${LINE%%: *}"
	_val="${LINE#* }"
	stuff["${_id}"]=${_val}
done < <(printf '%s\n' "${pass_key_value}")

password="${allData%%$'\n'*}"
stuff["pass"]=${password}

if test "${stuff['autotype']+autotype}"; then
	:
else
	stuff["autotype"]="${USERNAME_field} :tab pass"
fi

pass_content="$(for key in "${!stuff[@]}"; do printf '%s\n' "${key}: ${stuff[$key]}"; done)"

for word in ${stuff["$AUTOTYPE_field"]}; do
	case "$word" in
		":tab") doStroke 48;;
		":space") doStroke 49;;
		":delay") sleep "${delay}";;
		":enter") doStroke 36;;
		*) doType "${stuff[${word}]}";;
	esac
done

