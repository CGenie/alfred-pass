# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).
See [Keep a CHANGELOG](http://keepachangelog.com/) for more details.

## [Unreleased]

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

