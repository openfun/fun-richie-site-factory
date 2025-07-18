# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.29.1] - 2025-07-09

### Fixed

- Update S3 bucket names to match those provisioned on Scaleway

## [1.29.0] - 2025-06-25

### Changed

- Change settings to migrate media storage from AWS to Scaleway

## [1.28.2] - 2025-05-22

### Fixed

- Upgrade richie to 3.1.2

## [1.28.1] - 2025-05-21

### Fixed

- Upgrade richie to 3.1.1

## [1.28.0] - 2025-05-19

### Changed

- Upgrade richie to 3.1.0
- Migrate to new STORAGES settings

## [1.27.1] - 2023-08-30

### Fixed

- Upgrade richie to 2.24.1

## [1.27.0] - 2023-08-29

### Changed

- Upgrade richie to 2.24.0

## [1.26.0] - 2023-08-10

### Changed

- Upgrade richie to 2.23.0

## [1.25.0] - 2023-04-28

### Changed

- Upgrade richie to 2.22.0

## [1.24.1] - 2023-04-05

### Fixed

- Upgrade richie to 2.21.1

## [1.24.0] - 2023-04-04

### Changed

- Upgrade richie to 2.21.0

## [1.23.0] - 2023-02-22

### Changed

- Upgrade richie to 2.20.1

## [1.22.0] - 2023-02-03

### Changed

- Upgrade richie to 2.19.0

## [1.21.0] - 2023-01-16

### Changed

- Upgrade richie to 2.18.0

## [1.20.0] - 2022-07-28

### Added

- Add JOANIE settings configurable through environment variables

### Changed

- Upgrade richie to 2.15.1

## [1.19.1] - 2022-07-20

### Fixed

- Move factory-boy from dev requirements to base requirements

## [1.19.0] - 2022-07-04

### Added

- Enable "search" loc mem cache

### Changed

- Upgrade richie to 2.15.0

## [1.18.0] - 2022-03-07

### Changed

- Upgrade richie to 2.13.0

## [1.17.0] - 2022-01-04

### Changed

- Upgrade richie to 2.11.0

### Fixed

- Upgrade stylesheets to handle new modal styles.

## [1.16.0] - 2021-12-27

### Changed

- Upgrade richie to 2.10.0

## [1.15.0] - 2021-11-03

### Changed

- Upgrade richie to 2.9.1

## [1.14.0] - 2021-10-07

### Changed

- Upgrade richie to 2.8.2

## [1.13.0] - 2021-09-30

### Added

- Set Django Check SEO up

### Changed

- Upgrade richie to 2.8.1
- Rename `LTI_TEST_*` settings to `LTI_*` as "TEST" does not make sense here

## [1.12.1] - 2021-06-08

### Fixed

- Upgrade richie to 2.7.1 to fix LTI consumer when logged-in OpenEdX

## [1.12.0] - 2021-06-04

### Changed

- Upgrade richie to 2.7.0

## [1.11.1] - 2021-06-02

### Fixed

- Allow setting demo site domain otherwise so it is not set to localhost:8080

## [1.11.0] - 2021-05-03

### Changed

- Upgrade richie to 2.6.0

## [1.10.0] - 2021-04-22

### Changed

- Upgrade richie to 2.5.0

## [1.9.0] - 2021-04-07

### Changed

- Upgrade richie to 2.4.0
- Rename `fallback` cache to `memory_cache`

## [1.8.0] - 2021-03-25

### Changed

- Upgrade richie to 2.3.3

### Fixed

- Add missing stylesheet to patch CMS
- Add missing stylesheet for the LTI consumer plugin

## [1.7.0] - 2021-03-23

### Changed

- Upgrade richie to 2.3.0

## [1.6.0] - 2021-03-05

### Added

- Use custom views to handle errors (400, 403, 404, 500)
- Enable LTIConsumerPlugin on `course_teaser` placeholder

## [1.5.0] - 2021-02-05

### Changed

- Upgrade richie to 2.1.0
- Set `CMS_PAGETREE_DESCENDANTS_LIMIT` setting to control pagetree search node
  foldability according to its child node count

## [1.4.0] - 2021-01-14

### Changed

- Upgrade richie to 2.0.1

### Fixed

- Fix Sentry SDK initialization environment and release parameters

### Added

- Use a custom RedisCacheWithFallback cache to prevent denial of service
  when Redis is down

## [1.3.1] - 2020-12-09

### Fixed

- Include version in CMS cache prefix to bust cache when deploying new version
- Set default language to english (also makes generating the demo site work)

## [1.3.0] - 2020-12-07

### Fixed

- Add missing factory-boy dependency to allow generating the demo site

### Changed

- Upgrade richie to 2.0.0-beta.22

## [1.2.0] - 2020-11-30

### Changed

- Upgrade richie to 2.0.0-beta.21
- Unpin Django now that django-admin-style 2.0.2 supports
  the latest version 3.1.3

## [1.1.2] - 2020-11-15

### Fixed

- Pin Django to 3.1.1 because the `/admin/cms/page` layout is broken with
  Django>=3.1.2

## [1.1.1] - 2020-11-12

### Fixed

- Fix AWS media storage backend after upgrade to DjangoCMS 3.8.0

## [1.1.0] - 2020-11-12

### Added

- Add expiration lifecycle rule on s3 bucket for demo site

### Changed

- Upgrade richie to 2.0.0-beta.20

## [1.0.0] - 2020-10-08

### Added

- Add middleware from richie.core to limit the browser cache TTL
- Add step in the social auth connection pipeline to force user
  having is_staff set to true to also have is_superuser set to true.

### Changed

- Upgrade richie to 2.0.0-beta.15

### Removed

- Remove monkey patch that enabled cms page cache for non-staff users
- Remove Django cache middlewares from the settings

## [2.0.0-beta.14.5] - 2020-09-08

### Fixed

- Define missing EDX_USER_PROFILE_TO_DJANGO setting

## [2.0.0-beta.14.4] - 2020-09-08

### Fixed

- Add missing courses API url pattern

### Changed

- Bump lodash from 4.17.14 to 4.17.20

## [2.0.0-beta.14.3] - 2020-09-08

### Fixed

- set SOCIAL_AUTH_REDIRECT_IS_HTTPS to True in settings

## [2.0.0-beta.14.2] - 2020-09-04

### Fixed 

- Activate SSO connection with Open edX Hawthorn

## [2.0.0-beta.14.1] - 2020-09-04

### Fixed

- Declare missing social urls.

## [2.0.0-beta.14] - 2020-09-04

### Changed

- Upgrade richie to 2.0.0-beta.14 (LMS bridge and language dropdown)
- Set public english language

### Fixed

- Add i18n messages compilation in the DockerFile so translations are ready

## [2.0.0-beta.11] - 2020-08-20

### Changed

- Upgrade richie to 2.0.0-beta.11
- Enable Django CMS page cache for non-staff users
- Enable cache for content and sessions

### Fixed

- Fix translation overrides by configuring the specific "locale" directory

## [2.0.0-beta.8] - 2020-06-17

### Changed

- Upgrade richie to 2.0.0-beta.8

### Fixed

- Add missing factory-boy dependency to allow generating the demo site

## [2.0.0-beta.7] - 2020-06-08

First demo image for richie to 2.0.0-beta.7

[unreleased]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.29.1...HEAD
[1.29.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.29.0...demo-1.29.1
[1.29.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.28.2...demo-1.29.0
[1.28.2]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.28.1...demo-1.28.2
[1.28.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.28.0...demo-1.28.1
[1.28.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.27.1...demo-1.28.0
[1.27.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.27.0...demo-1.27.1
[1.27.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.26.0...demo-1.27.0
[1.26.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.25.0...demo-1.26.0
[1.25.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.24.1...demo-1.25.0
[1.24.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.24.0...demo-1.24.1
[1.24.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.23.0...demo-1.24.0
[1.23.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.22.0...demo-1.23.0
[1.22.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.21.0...demo-1.22.0
[1.21.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.20.0...demo-1.21.0
[1.20.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.19.1...demo-1.20.0
[1.19.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.19.0...demo-1.19.1
[1.19.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.18.0...demo-1.19.0
[1.18.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.17.0...demo-1.18.0
[1.17.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.16.0...demo-1.17.0
[1.16.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.15.0...demo-1.16.0
[1.15.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.14.0...demo-1.15.0
[1.14.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.13.0...demo-1.14.0
[1.13.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.12.1...demo-1.13.0
[1.12.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.12.0...demo-1.12.1
[1.12.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.11.1...demo-1.12.0
[1.11.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.11.0...demo-1.11.1
[1.11.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.10.0...demo-1.11.0
[1.10.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.9.0...demo-1.10.0
[1.9.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.8.0...demo-1.9.0
[1.8.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.7.0...demo-1.8.0
[1.7.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.6.0...demo-1.7.0
[1.6.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.5.0...demo-1.6.0
[1.5.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.4.0...demo-1.5.0
[1.4.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.3.1...demo-1.4.0
[1.3.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.3.0...demo-1.3.1
[1.3.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.2.0...demo-1.3.0
[1.2.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.1.2...demo-1.2.0
[1.1.2]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.1.1...demo-1.1.2
[1.1.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.1.0...demo-1.1.1
[1.1.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-1.0.0...demo-1.1.0
[1.0.0]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.14.5...demo-1.0.0
[2.0.0-beta.14.5]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.14.4...demo-2.0.0-beta.14.5
[2.0.0-beta.14.4]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.14.3...demo-2.0.0-beta.14.4
[2.0.0-beta.14.3]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.14.2...demo-2.0.0-beta.14.3
[2.0.0-beta.14.2]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.14.1...demo-2.0.0-beta.14.2
[2.0.0-beta.14.1]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.14...demo-2.0.0-beta.14.1
[2.0.0-beta.14]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.11...demo-2.0.0-beta.14
[2.0.0-beta.11]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.8...demo-2.0.0-beta.11
[2.0.0-beta.8]: https://github.com/openfun/fun-richie-site-factory/compare/demo-2.0.0-beta.7...demo-2.0.0-beta.8
[2.0.0-beta.7]: https://github.com/openfun/fun-richie-site-factory/releases/tag/demo-2.0.0-beta.7
