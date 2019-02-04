# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).
See [Keep a CHANGELOG](http://keepachangelog.com/) for more details.

## [Unreleased]
### Fixed
 - follow symlinks in the `password-filter.py` file [#18]

## [0.3.4] - 2018-02-04
### Added
- pass-otp support
### Changed
- we now use Alfred's transient clipboard (for `pass`, not for `po` yet), kudos
  to @bgshiller!
- recommended to use `pinentry.sh` instead of `pinentry-mac`

## [0.3.3] - 2018-06-18
### Added
- Notify when password is copied to clipboard

## [0.3.2] - 2018-05-09
### Fixed
- new Placeholder Title
- add Alfred 3 to README.md

### Added
- Icons

## [0.3.1] - 2017-10-31
### Fixed
 - fix searching for secrets with whitespaces in their name

## [0.3] - 2017-02-08
### Fixed
- remove use of rstrip as it can strip valid characters from password filename
- update README.md with basic installation instructions

### Added
- `pass generate` functionality

## [0.2.1] - 2016-01-18
### Added
- `LICENSE.md` file

## [0.2.0] - 2016-01-18
### Added
- Add `Makefile` to create `pass.alfredworkflow` by @sorbits
- Add UID to each item to enable Alfred's ranking by @sorbits
- Present password item's path as a subtitle by @sorbits
- Support progressive completion of password items by @sorbits

### Changed
- Use `pass -c` for copying to clipboard by @CGenie
- Remove `pass.alfredworkflow` from repo, use `Makefile` instead by @CGenie

### Fixed
- Sort items alphabetically (case-insensitively) and perform case-insensitive filtering by @sorbits

## [0.1.0] - 2016-01-15
### Added
- Initial working version (with `pass filter`) by @CGenie

