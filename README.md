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
