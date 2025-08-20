# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## 3.0.1 - 2025-08-20
### Fixed
- Fixed a bug in the `droid-metapatch` that did not correctly name reserved parameters such as `else` to `else_`.

## 3.0.0 - 2025-08-17
### Changed

- Completely rewritten the logic for the circuits.
  I am now using pydantic instead of pure dataclass models
  
- The `droid-metapatch` CLI command can now correctly parse the compressed patch format.

## 2.3.0 - 2025-08-15
### Changed
- Minimum supported python version is now 3.12

## 2.2.0 - 2024-10-12
### Changed
- Circuits have been re-generated for DROID Blue 6

## 2.1.0 - 2024-07-04
### Added
- Circuits have their memory consumption stored. This could allow for analysis to be added later.

### Changed
- The transform function `input` and `output` parameters have been renamed to
  `new_input` and `new_output`. This may break your code if you use that
  function! The `add_circuits()` instance function has not been changed.
  
- The circuit.json parsing has been refactored and greatly improved.

## 2.0.2 - 2024-05-05

### Fixed
- Fixed a bug with processing empty circuits
- Fixed a bug that would make booleans always return True

## 2.0.1 - 2024-04-29

### Changed
- Updated and improved documentation and other metadata.

## 2.0.0 - 2024-04-29

This is a major overhaul that adds support for native Droid circuits, overhauls and completely changes the CLI utility and much more.

## 1.2.0 - 2024-04-08

### Changed
- If no presets have been defined, a default preset will be created.

## 1.1.0 - 2024-04-07

### Added
- Added a small helper script that can convert droid patches to python code. This script is added as `droid-metapatch`.

## 1.0.3 - 2024-04-07

### Fixed
- Sections are now correctly grouped together.

## 1.0.2 - 2024-04-07

### Fixed 
- Add section now correctly sets the current section if the section was already defined.

## 1.0.1 - 2024-04-04

### Fixed
- Fixed synospsis output

## 1.0.0 - 2024-04-04

Initial 1.0.0 release



