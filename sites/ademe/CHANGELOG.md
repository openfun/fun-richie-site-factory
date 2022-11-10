# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.11.0] - 2022-11-10

### Changed

- Upgrade richie to 2.17.0

## [0.10.0] - 2022-10-03

### Added

- Add JOANIE settings configurable through environment variables

### Changed

- Upgrade richie to 2.15.1

### Fixed

- Fix course urls in Richie LMS backends configuration

## [0.9.1] - 2022-07-20

### Fixed

- Move factory-boy from dev requirements to base requirements

## [0.9.0] - 2022-07-04

### Added

- Enable "search" loc mem cache

### Changed

- Upgrade richie to 2.15.0

## [0.8.0] - 2022-03-07

### Changed

- Upgrade richie to 2.13.0

## [0.7.0] - 2022-01-04

### Changed

- Upgrade richie to 2.11.0

### Fixed

- Upgrade stylesheets to handle new modal styles.

## [0.6.0] - 2021-12-27

### Changed

- Upgrade richie to 2.10.0

## [0.5.0] - 2021-11-03

### Changed

- Increase max length of `course_description` placeholder to 2000 characters
- Upgrade richie to 2.9.1

## [0.4.0] - 2021-10-07

### Changed

- Upgrade richie to 2.8.2

## [0.3.0] - 2021-09-30

### Changed

- Upgrade richie to 2.8.1

## [0.2.0] - 2021-09-08

### Changed

- Configure Marsha video as LTI provider instead of "jisc.ac.uk" test platform
- Rename `LTI_TEST_*` settings to `LTI_*` as "TEST" does not make sense here
- Use 'burnt-orange' color instead of 'pumpkin-orange'
- Change 'Help' button to 'Contact us'
- Adjust font size on search filters in course list
- Replace TTF fonts with Woff and Woff2 formats
- Replace 'Contact' button by course run in course detail
- Adjust large banner hero for homepage with new background
- Make english language non public

### Fixed

- Fix staging and preprod domains for CloudFront proxying
- Fix font-family on all buttons to use 'Gotham'

## [0.1.0] - 2021-08-16

### Added

- First `ademe` image

[unreleased]: https://github.com/openfun/richie-site-factory/compare/ademe-0.11.0...HEAD
[0.11.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.10.0...ademe-0.11.0
[0.10.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.9.1...ademe-0.10.0
[0.9.1]: https://github.com/openfun/richie-site-factory/compare/ademe-0.9.0...ademe-0.9.1
[0.9.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.8.0...ademe-0.9.0
[0.8.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.7.0...ademe-0.8.0
[0.7.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.6.0...ademe-0.7.0
[0.6.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.5.0...ademe-0.6.0
[0.5.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.4.0...ademe-0.5.0
[0.4.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.3.0...ademe-0.4.0
[0.3.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.2.0...ademe-0.3.0
[0.2.0]: https://github.com/openfun/richie-site-factory/compare/ademe-0.1.0...ademe-0.2.0
[0.1.0]: https://github.com/openfun/richie-site-factory/releases/tag/ademe-0.1.0
