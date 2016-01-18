# Alfred 2 integration with Pass

This is Alfred 2 integration with [Pass - the standard Unix password manager](http://www.passwordstore.org/).
I took the idea for this from [passmenu](http://git.zx2c4.com/password-store/tree/contrib/dmenu/passmenu)
which is available for Linux.

## Setup

To make this work you need:
* [pass](http://www.passwordstore.org/) (obviously) -- needs to be set up with password store in
  `~/.password-store/`.
* `gpg-agent` -- install with `brew`
* `pinentry-mac` -- also install with `brew` (this is GUI frontend for `gpg-agent`).

Next configure `gpg-agent` to use `pinentry-mac` and not the bundled one, editing `~/.gnupg/gpg-agent.conf`:

```
pinentry-program /usr/local/bin/pinentry-mac
```

Basic Alfred commands:

## `pass <filter terms>`

This will search through your passwords using the filter terms you provided.

The password will be copied to clipboard and cleared after 45 seconds (this is the default
`pass -c` behavior).  You can change that time by modifying the env variable
`PASSWORD_STORE_CLIP_TIME`. Or in the `pass-show.sh` file you can change this line

```
pass show -c $QUERY
```

into this one

```
pass show $QUERY | awk 'BEGIN{ORS=""} {print; exit}' | pbcopy
```

to aviod auto-clearing of clipboard.

## Development

To generate the `pass.alfredworkflow` file (which you can import to Alfred), just use

```
make
```
