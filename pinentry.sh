#!/bin/bash
# choose pinentry depending on PINENTRY_USER_DATA
# requires pinentry-curses and pinentry-mac
# this *only works* with gpg 2
# see https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=802020

case $PINENTRY_USER_DATA in
gui)
  exec pinentry-mac "$@"
  ;;
*)
  exec pinentry "$@"
esac

