# Alfred 2 and 3 integration with Pass

[Packal page](http://www.packal.org/workflow/pass-0)

[Alfred forum page](http://www.alfredforum.com/topic/8471-pass-the-standard-unix-password-manager/)

This is Alfred 2 and 3 integration with [Pass - the standard Unix password manager](http://www.passwordstore.org/).
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

## Installation

After your system is set up as described above, download the latest package from
[Packal](http://www.packal.org/workflow/pass-0). Locate the file in Finder, right-click
on it and choose 'Open With -> Alfred'. You will be prompted to install the workflow, so go ahead.
Next fire up the Alfred console (`Alt-Space` by default) and type one of the commands described below.

## Usage

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

## `pg <id>`
Calls `pass generate` to add a new password with default length of 20 chars.

## Development

To generate the `pass.alfredworkflow` file (which you can import to Alfred), just use

```
make
```
