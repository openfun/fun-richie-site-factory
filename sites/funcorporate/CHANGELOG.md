# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.29.1] - 2025-07-04

### Fixed

- Exclude CMS endpoints from malformed query parameters

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

## [1.27.0] - 2025-05-05

### Added

- Add a middleware in charge of detecting malformed query strings

### Changed

- Upgrade richie to 3.0.0
- Migrate to new STORAGES settings

## [1.26.1] - 2023-11-02

### Fixed

- `coure_detail` template: fix missing endblock tag

## [1.26.0] - 2023-10-31

### Changed

- Override default permissions applied to Organization and Course pages

## [1.25.0] - 2023-10-05

### Changed

- Upgrade richie to 2.24.1

## [1.24.0] - 2023-09-25

### Changed

- Upgrade richie to 2.23.0

### Fixed

- Add "noreferrer noopener" to all target="_blank" links

## [1.23.0] - 2023-04-28

### Changed

- Upgrade richie to 2.22.0

## [1.22.1] - 2023-04-05

### Fixed

- Upgrade richie to 2.21.1

## [1.22.0] - 2023-04-04

### Changed

- Upgrade richie to 2.21.0

## [1.21.1] - 2023-03-01

### Fixed

- Add missing api course urls to urlpatterns to be able to use page autocomplete

## [1.21.0] - 2023-02-22

### Changed

- Upgrade richie to 2.20.1

## [1.20.0] - 2023-02-03

### Changed

- Upgrade richie to 2.19.0

## [1.19.0] - 2023-01-16

### Changed

- Upgrade richie to 2.18.0

## [1.18.1] - 2022-07-20

### Fixed

- Move factory-boy from dev requirements to base requirements

## [1.18.0] - 2022-07-04

### Added

- Enable "search" loc mem cache

### Changed

- Upgrade richie to 2.15.0

## [1.17.0] - 2022-03-07

### Changed

- Upgrade richie to 2.13.0

## [1.16.0] - 2022-01-04

### Changed

- Link footer logo to our new institutional site
- Upgrade richie to 2.11.0

### Fixed

- Upgrade stylesheets to handle new modal styles.

## [1.15.0] - 2021-12-27

### Changed

- Upgrade richie to 2.10.0

## [1.14.0] - 2021-11-03

### Changed

- Upgrade richie to 2.9.1

## [1.13.0] - 2021-10-07

### Changed

- Upgrade richie to 2.8.2

## [1.12.0] - 2021-09-30

### Added

- Set Django Check SEO up

### Changed

- Upgrade richie to 2.8.1
- Rename `LTI_TEST_*` settings to `LTI_*` as "TEST" does not make sense here

## [1.11.0] - 2021-06-04

### Changed

- Upgrade richie to 2.7.0

## [1.10.0] - 2021-05-03

### Changed

- Upgrade richie to 2.6.0

## [1.9.0] - 2021-04-22

### Changed

- Upgrade richie to 2.5.0

## [1.8.0] - 2021-04-07

### Changed

- Upgrade richie to 2.4.0
- Rename `fallback` cache to `memory_cache`

## [1.7.0] - 2021-03-25

### Changed

- Upgrade richie to 2.3.3

### Fixed

- Add missing stylesheet to patch CMS
- Add missing stylesheet for the LTI consumer plugin

## [1.6.0] - 2021-03-23

### Changed

- Upgrade richie to 2.3.0

## [1.5.0] - 2021-03-05

### Added

- Use custom views to handle errors (400, 403, 404, 500)
- Enable LTIConsumerPlugin on `course_teaser` placeholder

## [1.4.0] - 2021-02-05

### Changed

- Upgrade richie to 2.1.0
- Set `CMS_PAGETREE_DESCENDANTS_LIMIT` setting to control pagetree search node
  foldability according to its child node count

## [1.3.0] - 2021-01-14

### Changed

- Upgrade richie to 2.0.1

### Fixed

- Fix Sentry SDK initialization environment and release parameters

### Added

- Use a custom RedisCacheWithFallback cache to prevent denial of service
  when Redis is down

## [1.2.1] - 2020-12-09

### Fixed

- Include version in CMS cache prefix to bust cache when deploying new version

## [1.2.0] - 2020-12-07

### Changed

- Upgrade richie to 2.0.0-beta.22

## [1.1.0] - 2020-11-30

### Changed

- Upgrade richie to 2.0.0-beta.21
- Unpin Django now that django-admin-style 2.0.2 supports
  the latest version 3.1.3
- Return a 403 response when user tries to upload a file in unsorted folder

## [1.0.1] - 2020-11-15

### Fixed

- Pin Django to 3.1.1 because the `/admin/cms/page` layout is broken with
  Django>=3.1.2

## [1.0.0] - 2020-11-12

### Fixed

- Fix AWS media storage backend after upgrade to DjangoCMS 3.8.0

## [0.9.0] - 2020-11-12

### Changed

- Upgrade richie to 2.0.0-beta.20
- Override translations to replace course by training

## [0.8.1] - 2020-10-16

### Fixed

- Fix javascript build which was forgotten in Dockerfile and missing from image

## [0.8.0] - 2020-10-14

### Added

- Add a "Dashboard" button linking to OpenEdX

### Changed

- Allow several plugins in course description to relax limit on number of char
- Open contact form in a new tab
- Display course duration in course glimpse footer

## [0.7.0] - 2020-10-08

### Added

- Add middleware from richie.core to limit the browser cache TTL

### Changed

- Upgrade richie to 2.0.0-beta.15
- Customize slogan in footer

### Fixed

- Hide site in the english language until it is ready

### Removed

- Remove monkey patch that enabled cms page cache for non-staff users
- Remove Django cache middlewares from the settings

## [0.6.2] - 2020-09-17

### Changed

- Customize wording for "What you will learn" using translations

### Fixed

- Filter on "training domains", not on "categories" which is the root node
- Rename contact buttons in header and course page and point to Zendesk

## [0.6.1] - 2020-09-16

### Fixed

- Fix missing scss objects and components following richie upgrade

## [0.6.0] - 2020-09-16

### Added

- Override `course_detail` template to add a message above subheader CTA.
- Use the FunCorporate Zendesk link on "Contact Us" CTA in header.

### Changed

- Upgrade richie to 2.0.0-beta.14
- Hide licences block on the course detail pages
- Customize filters visible on the search page
- Customize social networks links

### Fixed

- Override .subheader .category-badge styles to fit fun-corporate mockups.
- Add i18n messages compilation in the DockerFile so translations are ready

## [0.5.0] - 2020-08-20

### Changed

- Upgrade richie to 2.0.0-beta.11
- Enable cache for content and sessions
- Enable Django CMS page cache for non-staff users

### Fixed

- Fix translation overrides by configuring the specific "locale" directory

## [0.4.0] - 2020-06-17

### Changed

- Upgrade richie to 2.0.0-beta.8

## [0.3.0] - 2020-06-08

### Changed

- Upgrade to richie 2.0.0-beta.7

## [0.2.2] - 2020-06-06

### Changed

- Upgrade to richie 2.0.0-beta.6

## [0.2.1] - 2020-05-07

### Fixed

- With django storages S3 backend, `STATIC_URL` should not start with a "/"

## [0.2.0] - 2020-05-07

### Changed

- Upgrade to django-storages 1.9.1
- Disable 'runs' and 'snapshot' blocks from course detail.
- Disable 'max-width' from '.course-detail\_\_wrapper'.
- Enable background and arc image for course detail primary group.

### Fixed

- DjangoCMS is not compatible with Django 3, force it in requirements

## [0.1.0] - 2020-04-21

### Changed

- Upgrade Terraform project to run with v0.12.24
- Upgrade Python requirements files to the last dependencies.
- Upgrade frontend "package.json" to the last dependencies.
- Update "main.scss" file to import richie Sass sources to be able to
  override settings.
- Update project settings to add styleguide and missing new settings.
- Update project urls to add styleguide and account views.
- Update layout color theme and logo to fit fun-corporate mockups.

[unreleased]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.29.1...HEAD
[1.29.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.29.0...funcorporate-1.29.1
[1.29.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.28.2...funcorporate-1.29.0
[1.28.2]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.28.1...funcorporate-1.28.2
[1.28.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.28.0...funcorporate-1.28.1
[1.28.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.27.0...funcorporate-1.28.0
[1.27.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.26.1...funcorporate-1.27.0
[1.26.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.26.0...funcorporate-1.26.1
[1.26.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.25.0...funcorporate-1.26.0
[1.25.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.24.0...funcorporate-1.25.0
[1.24.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.23.0...funcorporate-1.24.0
[1.23.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.22.1...funcorporate-1.23.0
[1.22.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.22.0...funcorporate-1.22.1
[1.22.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.21.1...funcorporate-1.22.0
[1.21.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.21.0...funcorporate-1.21.1
[1.21.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.20.0...funcorporate-1.21.0
[1.20.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.19.0...funcorporate-1.20.0
[1.19.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.18.1...funcorporate-1.19.0
[1.18.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.18.0...funcorporate-1.18.1
[1.18.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.17.0...funcorporate-1.18.0
[1.17.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.16.0...funcorporate-1.17.0
[1.16.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.15.0...funcorporate-1.16.0
[1.15.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.14.0...funcorporate-1.15.0
[1.14.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.13.0...funcorporate-1.14.0
[1.13.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.12.0...funcorporate-1.13.0
[1.12.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.11.0...funcorporate-1.12.0
[1.11.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.10.0...funcorporate-1.11.0
[1.10.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.9.0...funcorporate-1.10.0
[1.9.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.8.0...funcorporate-1.9.0
[1.8.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.7.0...funcorporate-1.8.0
[1.7.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.6.0...funcorporate-1.7.0
[1.6.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.5.0...funcorporate-1.6.0
[1.5.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.4.0...funcorporate-1.5.0
[1.4.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.3.0...funcorporate-1.4.0
[1.3.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.2.1...funcorporate-1.3.0
[1.2.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.2.0...funcorporate-1.2.1
[1.2.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.1.0...funcorporate-1.2.0
[1.1.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.0.1...funcorporate-1.1.0
[1.0.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-1.0.0...funcorporate-1.0.1
[1.0.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.9.0...funcorporate-1.0.0
[0.9.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.8.1...funcorporate-0.9.0
[0.8.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.8.0...funcorporate-0.8.1
[0.8.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.7.0...funcorporate-0.8.0
[0.7.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.6.2...funcorporate-0.7.0
[0.6.2]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.6.1...funcorporate-0.6.2
[0.6.1]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.6.0...funcorporate-0.6.1
[0.6.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.5.0...funcorporate-0.6.0
[0.5.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.4.0...funcorporate-0.5.0
[0.4.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.3.0...funcorporate-0.4.0
[0.3.0]: https://github.com/openfun/fun-richie-site-factory/compare/funcorporate-0.2.2...funcorporate-0.3.0
[0.2.2]: https://github.com/openfun/fun-richie-site-factory/releases/tag/funcorporate-0.2.2

# Deprecated repository

[0.2.1]: https://github.com/openfun/fun-corporate/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/openfun/fun-corporate/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/openfun/fun-corporate/releases/tag/v0.1.0
