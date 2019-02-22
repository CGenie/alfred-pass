# An Alfred 2/3 Workflow for Pass

[Pacmax Page](https://pacmax.org/pac/cgenie-alfred-pass/)

[Alfred forum page](https://www.alfredforum.com/topic/8471-pass-the-standard-unix-password-manager/)

This is an Alfred 2/3 workflow for [Pass - the standard Unix password manager](https://www.passwordstore.org/). It's based on [passmenu](http://git.zx2c4.com/password-store/tree/contrib/dmenu/passmenu), which is available for Linux.

## Setup

To make this work you need:
* [Pass](https://www.passwordstore.org/) (obviously) -- needs to be set up with password store in
  `~/.password-store/`.
* `gpg-agent` -- install with `brew`
* `pinentry-mac` -- also install with `brew` (this is GUI frontend for `gpg-agent`).
* (optionally) the `fuzzywuzzy` and (also optionally) `python-Levenshtein`
  Python modules (install with `pip install --user fuzzywuzzy python-Levenshtein`)

Next configure `gpg-agent` to use `pinentry-mac` and not the bundled one, editing `~/.gnupg/gpg-agent.conf`:

```
pinentry-program /usr/local/bin/pinentry-mac
```

If you prefer to keep the terminal version of `pinentry` you can use the
`pinentry.sh` wrapper from this repository as the `pinentry-program`. This will
use the ncurses version when in console and the GUI version for Alfred etc.

You can also take a look at [this blog post from @bshiller](https://brianschiller.com/blog/2016/08/31/gnu-pass-alfred).

### GPG tweaking

You can tweak some of the `gpg-agent` settings in `~/.gnupg/gpg-agent.conf`:

```
max-cache-ttl 7200
```

After 7200 seconds, GPG will forget your master password.

## Installation

After your system is set up as described above, download the latest package from
[Pacmax](https://pacmax.org/pac/cgenie-alfred-pass/). Locate the file in Finder, right-click
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

## `po <filter terms>`

This will search through your OTP passwords (requires `pass-otp`) using the filter terms you provided.

## Development

To generate the `pass.alfredworkflow` file (which you can import to Alfred), just use

```
make
```
