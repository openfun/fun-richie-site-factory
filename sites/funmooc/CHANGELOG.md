# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic
Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Replace Paid offer color (eastern-blue) with #088488
- Use glimpse footer color for glimpse label icon

## [1.44.1] - 2025-07-04

### Fixed

- Exclude CMS endpoints from malformed query parameters

## [1.44.0] - 2025-06-25

### Changed

- Change settings to migrate media storage from AWS to Scaleway

## [1.43.2] - 2025-05-22

### Fixed

- Upgrade richie to 3.1.2

## [1.43.1] - 2025-05-21

### Fixed

- Upgrade richie to 3.1.1

## [1.43.0] - 2025-05-19

### Changed

- Upgrade richie to 3.1.0
- Upgrade all deps

## [1.42.0] - 2025-04-08

### Changed

- Hide offer icon for free courses
- Show offer price
- Upgrade to richie 3.0.0

## [1.42.0-beta.2] - 2025-03-31

### Changed

- Upgrade to latest richie dev version
- Enable Slider plugin

## [1.42.0-beta.1] - 2025-03-27

### Changed

- Upgrade to latest richie dev version
- Customize course glimpse look'n feel for course with a paid offer

## [1.42.0-beta.0] - 2025-03-11

### Changed

- Upgrade to richie next version
- Enable dropdown menu in topbar

## [1.41.1] - 2025-02-13

### Fixed

- Disable category_additional_information block in course detail page

## [1.41.0] - 2025-02-13

### Changed

- Upgrade to richie 2.34.0

## [1.40.1] - 2025-01-27

### Fixed

- Ignore admin endpoints in the middleware that detects malformed query strings

## [1.40.0] - 2025-01-23

### Added

- Add a middleware in charge of detecting malformed query strings

## [1.39.0] - 2024-12-02

### Changed

- Upgrade to richie 2.33.0

## [1.38.0] - 2024-11-27

### Changed

- Upgrade to richie 2.32.0

## [1.37.0] - 2024-11-20

### Changed

- Upgrade to richie 2.31.0

## [1.36.0] - 2024-10-16

### Changed

- Update 'funmooc' site integration to move up main menu and move down the
  search bar

## [1.35.2] - 2024-09-23

### Fixed

- Upgrade to richie 2.29.2

## [1.35.1] - 2024-08-26

### Fixed

- Upgrade to richie 2.29.1

## [1.35.0] - 2024-08-22

### Changed

- Upgrade to richie 2.29.0

## [1.34.1] - 2024-06-21

### Fixed

- Upgrade to richie 2.28.1

## [1.34.0] - 2024-06-11

### Changed

- Upgrade to richie 2.28.0

## [1.33.0] - 2024-06-03

### Changed

- Upgrade to richie 2.27.0

## [1.32.1] - 2024-05-23

### Fixed

- Add missing `CSRF_TRUSTED_ORIGINS` setting in Production configuration

## [1.32.0] - 2024-05-22

### Added

- Add custom course template for professional training

### Changed

- Upgrade to richie 2.26.0

## [1.31.0] - 2024-05-14

### Changed

- Replace the white fun mooc logo by the color one

## [1.30.0] - 2024-05-06

### Changed

- Add `REACT_DASHBOARD_MENU_LINKS` to display new dashboard links into user menu

## [1.29.1] - 2024-04-18

### Fixed

- Fix multiple page returned issue on edx redirect view
- Upgrade richie to 2.25.1
- Fix malformed dashboard url 

## [1.29.0] - 2024-04-11

### Added

- Add FUN Mooc logo in footer
- Add settings API_TOKEN for JOANIE_BACKEND

### Changed

- Upgrade richie to 2.25.0
- Change deprecated `xiti` web analytics service to `pianoanalytics`  
- Configure Piano Analytics to also collect UTM parameters
- Pin Piano Analytics JS SDK to 6.13.1

## [1.29.0-beta.0] - 2024-01-11

### Changed

- Upgrade richie to 2.25.0-beta.1

## [1.28.0] - 2023-10-31

### Changed

- Override default permissions applied to Organization and Course pages

## [1.27.2] - 2023-09-25

### Fixed

- Add "noreferrer noopener" to all target="_blank" links

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
- Replace header logo with a new one

## [1.22.0] - 2023-02-03

### Changed

- Upgrade richie to 2.19.0
- Improve accessibility by using lighter color for empty course label

## [1.21.0] - 2023-01-16

### Changed

- Update some styles to display properly CourseProductItem
- Upgrade richie to 2.18.0

## [1.20.0] - 2022-11-10

### Changed

- Upgrade richie to 2.17.0

### Fixed

- Xiti issues when a course page has only one organization. 

## [1.19.0] - 2022-10-18

### Changed

- Add Pashto to the language choices for course runs
- Migrate web analytics to piano analytics
- Change help button label to "FAQ"
- Upgrade richie to 2.15.1

## [1.18.0] - 2022-07-28

### Added

- Add JOANIE settings configurable through environment variables

## [1.17.2] - 2022-07-20

### Fixed

- Move factory-boy from dev requirements to base requirements

## [1.17.1] - 2022-07-04

### Added

- Enable "search" loc mem cache

## [1.17.0] - 2022-06-24

### Changed

- Upgrade richie to 2.15.0
- Update href of Help button to target an internal page with id "help"

## [1.16.0] - 2022-04-07

### Changed

- Upgrade richie to 2.14.1

## [1.15.2] - 2022-04-05

### Fixed

- Prevent course glimpse title color to be overriden by the section font color

## [1.15.1] - 2022-04-05

### Fixed

- Fix layout issue on course detail

## [1.15.0] - 2022-04-04

### Changed

- Upgrade richie to 2.14.0

## [1.14.0] - 2022-03-07

### Added

- Enable Xiti course enrollment analytics

### Changed

- Upgrade richie to 2.13.0


## [1.13.0] - 2022-01-04

### Changed

- Link footer logo to our new institutional site
- Upgrade richie to 2.11.0

### Fixed

- Upgrade stylesheets to handle new modal styles.

## [1.12.0] - 2021-12-27

### Changed

- Upgrade richie to 2.10.0

## [1.11.0] - 2021-11-03

### Changed

- Upgrade richie to 2.9.1

## [1.10.0] - 2021-10-07

### Changed

- Upgrade richie to 2.8.2

## [1.9.0] - 2021-09-30

### Added

- Set Django Check SEO up

### Changed

- Remove `MARKETING_CONTEXT` and use `WEB_ANALYTICS_*` context instead
- Upgrade richie to 2.8.1
- Rename `LTI_TEST_*` settings to `LTI_*` as "TEST" does not make sense here

## [1.8.1] - 2021-06-08

### Fixed

- Upgrade richie to 2.7.1 to fix LTI consumer when logged-in OpenEdX

## [1.8.0] - 2021-06-04

### Changed

- Upgrade richie to 2.7.0

## [1.7.0] - 2021-05-03

### Changed

- Upgrade richie to 2.6.0

## [1.6.1] - 2021-04-28

### Fixed

- Fix contributors filter by overriding only its human name
- Rename "New course" option to "New courses" for coherence with filter name

## [1.6.0] - 2021-04-22

### Fixed

- Send xiti hits unless visitor explicity refuses

### Changed

- Upgrade richie to 2.5.0

## [1.5.0] - 2021-04-13

### Added

- Redirect OpenEdX university urls to richie university pages

### Changed

- Redirect old OpenEdX course urls to richie course pages

## [1.4.0] - 2021-04-07

### Changed

- Upgrade richie to 2.4.0
- Rename `fallback` cache to `memory_cache`

## [1.3.0] - 2021-03-25

### Changed

- Upgrade richie to 2.3.3
- Rename filter "First session" to "New course" following user feedback

### Fixed

- Add missing stylesheet to patch CMS
- Add missing stylesheet for the LTI consumer plugin

## [1.2.0] - 2021-03-23

### Changed

- Display the first open course run in the header of the course detail page
- Upgrade richie to 2.3.0

### Added

- Enable Xiti traffic analytics
- Add Cookies consent using [tarteaucitron](https://tarteaucitron.io)

## [1.1.0] - 2021-03-05

### Added

- Add "Types" category as search filter
- Use custom views to handle errors (400, 403, 404, 500)
- Enable LTIConsumerPlugin on `course_teaser` placeholder

### Changed

- Prevent course run languages update when synchronization hook is triggered
- Set english language as public

## [1.0.0] - 2021-02-05

### Added

- Redirect old OpenEdX course urls to new richie course pages

### Changed

- Upgrade richie to 2.1.0
- Set `CMS_PAGETREE_DESCENDANTS_LIMIT` setting to control pagetree search node
  foldability according to its child node count

## [0.19.0] - 2021-01-14

### Changed

- Upgrade richie to 2.0.1

### Fixed

- Fix Sentry SDK initialization environment and release parameters

### Added

- Use a custom RedisCacheWithFallback cache to prevent denial of service
  when Redis is down

## [0.18.0] - 2020-12-11

### Changed

- Customize search filters with new categories

### Fixed

- Fix regex that extracts course ids for enrollments

## [0.17.3] - 2020-12-10

### Fixed

- Fix missing url patterns for the course runs API

## [0.17.2] - 2020-12-10

### Fixed

- Configure cache durations to make cache effective in production

## [0.17.1] - 2020-12-09

### Fixed

- Include version in CMS cache prefix to bust cache when deploying new version

## [0.17.0] - 2020-12-07

### Changed

- Upgrade richie to 2.0.0-beta.22

### Removed

- Remove gimporter app

## [0.16.0] - 2020-11-30

### Changed

- Upgrade richie to 2.0.0-beta.21
- Unpin Django now that django-admin-style 2.0.2 supports
  the latest version 3.1.3
- Return a 403 response when user tries to upload a file in unsorted folder

## [0.15.2] - 2020-11-15

### Fixed

- Pin Django to 3.1.1 because the `/admin/cms/page` layout is broken with
  Django>=3.1.2

## [0.15.1] - 2020-11-12

### Fixed

- Fix AWS media storage backend after upgrade to DjangoCMS 3.8.0

## [0.15.0] - 2020-11-12

### Changed

- Upgrade richie to 2.0.0-beta.20

## [0.14.0] - 2020-10-08

### Added

- Add middleware from richie.core to limit the browser cache TTL

### Changed

- Upgrade richie to 2.0.0-beta.15

### Fixed

- Add i18n messages compilation in the DockerFile so translations are ready

### Removed

- Remove monkey patch that enabled cms page cache for non-staff users
- Remove Django cache middlewares from the settings

## [0.13.0] - 2020-08-20

### Changed

- Upgrade richie to 2.0.0-beta.11
- Homepage hero intro adjustments for font and background.
- Button caesura variant alternative color for some section.
- Adjust 'middle-gradient' to try to be more accessible.
- Correct links on social networks badges.
- More accessible category badges color everywhere.
- Adapt bullet list checkmark icon color to funmooc theme.
- Removed header bottom border.
- Enable Django CMS page cache for non-staff users
- Enable cache for content and sessions

### Fixed

- Fix translation overrides by configuring the specific "locale" directory

## [0.12.0] - 2020-06-17

### Changed

- Upgrade richie to 2.0.0-beta.8

## [0.11.0] - 2020-06-08

### Changed

- Upgrade to richie 2.0.0-beta.7

## [0.10.1] - 2020-05-27

### Fixed

- Use nginx image adapted for OpenShift

## [0.10.0] - 2020-05-27

### Changed

- Move static files to a custom nginx image
- Refactor Docker Compose project to run both the development and production
  images

### Fixed

- Fix svg images in static files by adding alias to the CloudFront
  distribution on the same domain as the app

## [0.9.6] - 2020-05-22

### Fixed

- Fix copying frontend build to image

## [0.9.5] - 2020-05-22

### Added

- Add nginx to the stack to test collectstatic

### Changed

- Upgrade to Terraform 0.12

### Fixed

- Fix css build location after refactoring

## [0.9.4] - 2020-05-21

### Fixed

- Fix path to storage class following refactoring

## [0.9.3] - 2020-05-21

### Added

- Add translations for strings specific to fun-mooc

### Changed

- Upgrade richie to 2.0.0-beta.6.
- Disable "Contact Us" CTA from course detail.

### Fixed

- Refactor project to the classical Django structure to fix static files
- Correctly adjust hero-intro background to homepage mockup.
- Use the FunMooc help center link on "Contact Us" CTA in header.

## [0.9.2] - 2020-05-07

### Fixed

- With django storages S3 backend, `STATIC_URL` should not start with a "/"

## [0.9.1] - 2020-05-07

### Changed

- Upgrade to django-storages 1.9.1

### Fixed

- With the django storages S3 backend, `MEDIA_URL` should not start with a "/"

## [0.9.0] - 2020-05-06

### Changed

- Upgrade richie to 2.0.0-beta.5.
- Update "main.scss" file to import richie Sass sources to be able to
  override settings.
- Update project settings to add styleguide and missing new settings.
- Update project urls to add styleguide.
- Update layout color theme and logo to fit fun-mooc mockups.

## [0.8.0] - 2019-12-15

### Changed

- Upgrade richie to 1.16.1.

### Fixed

- Upgrade django-storages to fix static manifest storage bakend and media
  files upload.

## [0.7.1] - 2019-11-24

### Fixed

- Add missing user related urls and settings.

## [0.7.0] - 2019-11-23

### Changed

- Upgrade richie to 1.14.1.

## [0.6.0] - 2019-10-23

### Changed

- Upgrade richie to 1.12.0.

## [0.5.0] - 2019-10-08

### Changed

- Upgrade richie to 1.10.0,
- Make the superuser field readonly for non superusers.

### Fixed

- Make API calls work behind an htaccess by removing Basic Auth fallback.

## [0.4.3] - 2019-09-12

### Changed

- Let the Google sheet importer sort media files related to each organization
  or course in their specific folder in Django filer.

### Fixed

- Clean-up the content imported from the Google sheet with gimporter:
  * fix broken links by porting missing media files to Django filer,
  * make all urls relative (exit france-universite-numerique-mooc.fr),
  * replace old urls by new ones computed with DjangoCMS page slugs.

## [0.4.2] - 2019-09-06

### Added

- Create roles and permissions for organizations and courses imported via the
  Google sheet importer,
- Import blog posts from Google sheet fixtures,
- Import course licences from Google sheet fixtures.

### Changed

- Upgrade richie to 1.8.3.

## [0.4.1] - 2019-09-02

### Fixed

- Fix CKEditor static files to work with a CDN,
- Fix logo override by moving it to the same new location as in Richie.

## [0.4.0] - 2019-08-28

### Added

- Add a gimporter app to automatically transfer existing content on fun-mooc.fr
- Automate backend code assessment with a classical python toolkit (flake8,
  isort, black, pylint, bandit)

### Changed

- Disable the "unsorted uploads" directory on Django Filer,
- Upgrade richie to 1.8.0.

### Security

- Update `lodash` and related packages to safe versions.

## [0.3.0] - 2019-07-04

### Added

- Define CDN_DOMAIN setting from AWS CloudFront domain value

### Changed

- Upgrade richie to 1.5.0

### Fixed

- Configure `X_FRAME_OPTIONS` to `SAMEORIGIN` to allow DjangoCMS frontend admin
  frames display

### Security

- Update `fstream` to a safe version (>=1.0.12)

## [0.2.0] - 2019-05-07

### Changed

- Upgrade richie to 1.0.0-beta.8

### Fixed

- The `data/` directory and its subdirectories are now properly created while
  bootstrapping the project
- Remove unused ElasticSearchMixin in project settings

## [0.1.0] - 2019-04-18

### Added

- Design a Richie-based project for the future fun-mooc.fr front end
- Static and media files are stored in AWS S3 buckets and distributed _via_
  Amazon CloudFront

[unreleased]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.44.1...HEAD
[1.44.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.44.0...funmooc-1.44.1
[1.44.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.43.2...funmooc-1.44.0
[1.43.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.43.1...funmooc-1.43.2
[1.43.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.43.0...funmooc-1.43.1
[1.43.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.42.0...funmooc-1.43.0
[1.42.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.42.0-beta.2...funmooc-1.42.0
[1.42.0-beta.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.42.0-beta.1...funmooc-1.42.0-beta.2
[1.42.0-beta.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.42.0-beta.0...funmooc-1.42.0-beta.1
[1.42.0-beta.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.41.1...funmooc-1.42.0-beta.0
[1.41.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.41.0...funmooc-1.41.1
[1.41.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.40.1...funmooc-1.41.0
[1.40.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.40.0...funmooc-1.40.1
[1.40.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.39.0...funmooc-1.40.0
[1.39.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.38.0...funmooc-1.39.0
[1.38.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.37.0...funmooc-1.38.0
[1.37.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.36.0...funmooc-1.37.0
[1.36.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.35.2...funmooc-1.36.0
[1.35.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.35.1...funmooc-1.35.2
[1.35.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.35.0...funmooc-1.35.1
[1.35.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.34.1...funmooc-1.35.0
[1.34.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.34.0...funmooc-1.34.1
[1.34.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.33.0...funmooc-1.34.0
[1.33.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.32.1...funmooc-1.33.0
[1.32.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.32.0...funmooc-1.32.1
[1.32.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.31.0...funmooc-1.32.0
[1.31.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.30.0...funmooc-1.31.0
[1.30.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.29.1...funmooc-1.30.0
[1.29.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.29.0...funmooc-1.29.1
[1.29.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.29.0-beta.0...funmooc-1.29.0
[1.29.0-beta.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.28.0...funmooc-1.29.0-beta.0
[1.28.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.27.2...funmooc-1.28.0
[1.27.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.27.1...funmooc-1.27.2
[1.27.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.27.0...funmooc-1.27.1
[1.27.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.26.0...funmooc-1.27.0
[1.26.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.25.0...funmooc-1.26.0
[1.25.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.24.1...funmooc-1.25.0
[1.24.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.24.0...funmooc-1.24.1
[1.24.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.23.0...funmooc-1.24.0
[1.23.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.22.0...funmooc-1.23.0
[1.22.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.21.0...funmooc-1.22.0
[1.21.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.20.0...funmooc-1.21.0
[1.20.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.19.0...funmooc-1.20.0
[1.19.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.18.0...funmooc-1.19.0
[1.18.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.17.2...funmooc-1.18.0
[1.17.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.17.1...funmooc-1.17.2
[1.17.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.17.0...funmooc-1.17.1
[1.17.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.16.0...funmooc-1.17.0
[1.16.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.15.2...funmooc-1.16.0
[1.15.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.15.1...funmooc-1.15.2
[1.15.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.15.0...funmooc-1.15.1
[1.15.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.14.0...funmooc-1.15.0
[1.14.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.13.0...funmooc-1.14.0
[1.13.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.12.0...funmooc-1.13.0
[1.12.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.11.0...funmooc-1.12.0
[1.11.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.10.0...funmooc-1.11.0
[1.10.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.9.0...funmooc-1.10.0
[1.9.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.8.1...funmooc-1.9.0
[1.8.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.8.0...funmooc-1.8.1
[1.8.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.7.0...funmooc-1.8.0
[1.7.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.6.1...funmooc-1.7.0
[1.6.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.6.0...funmooc-1.6.1
[1.6.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.5.0...funmooc-1.6.0
[1.5.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.4.0...funmooc-1.5.0
[1.4.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.3.0...funmooc-1.4.0
[1.3.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.2.0...funmooc-1.3.0
[1.2.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.1.0...funmooc-1.2.0
[1.1.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-1.0.0...funmooc-1.1.0
[1.0.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.19.0...funmooc-1.0.0
[0.19.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.18.0...funmooc-0.19.0
[0.18.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.17.3...funmooc-0.18.0
[0.17.3]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.17.2...funmooc-0.17.3
[0.17.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.17.1...funmooc-0.17.2
[0.17.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.17.0...funmooc-0.17.1
[0.17.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.16.0...funmooc-0.17.0
[0.16.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.15.2...funmooc-0.16.0
[0.15.2]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.15.1...funmooc-0.15.2
[0.15.1]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.15.0...funmooc-0.15.1
[0.15.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.14.0...funmooc-0.15.0
[0.14.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.13.0...funmooc-0.14.0
[0.13.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.12.0...funmooc-0.13.0
[0.12.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.11.0...funmooc-0.12.0
[0.11.0]: https://github.com/openfun/fun-richie-site-factory/compare/funmooc-0.10.1...funmooc-0.11.0
[0.10.1]: https://github.com/openfun/fun-richie-site-factory/compare/v0.10.0...funmooc-0.10.1
[0.10.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.9.6...v0.10.0
[0.9.6]: https://github.com/openfun/fun-richie-site-factory/compare/v0.9.5...v0.9.6
[0.9.5]: https://github.com/openfun/fun-richie-site-factory/compare/v0.9.4...v0.9.5
[0.9.4]: https://github.com/openfun/fun-richie-site-factory/compare/v0.9.3...v0.9.4
[0.9.3]: https://github.com/openfun/fun-richie-site-factory/compare/v0.9.2...v0.9.3
[0.9.2]: https://github.com/openfun/fun-richie-site-factory/compare/v0.9.1...v0.9.2
[0.9.1]: https://github.com/openfun/fun-richie-site-factory/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.7.1...v0.8.0
[0.7.1]: https://github.com/openfun/fun-richie-site-factory/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.4.3...v0.5.0
[0.4.3]: https://github.com/openfun/fun-richie-site-factory/compare/v0.4.2...v0.4.3
[0.4.2]: https://github.com/openfun/fun-richie-site-factory/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/openfun/fun-richie-site-factory/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/openfun/fun-richie-site-factory/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/openfun/fun-richie-site-factory/releases/tag/v0.1.0
