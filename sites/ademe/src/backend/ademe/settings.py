"""
Django settings for ADEME project.
"""

import json
import os

from django.utils.translation import gettext_lazy as _

# pylint: disable=ungrouped-imports
import sentry_sdk
from configurations import Configuration, values
from richie.apps.courses.settings.mixins import RichieCoursesConfigurationMixin
from sentry_sdk.integrations.django import DjangoIntegration

from base.utils import merge_dict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join("/", "data")

FILTERS_CONFIGURATION = {
    # Note: the key is a special name that connects the filter to page objects
    # in Richie as well as the corresponding indexer and API endpoint.
    "new": {
        "class": "richie.apps.search.filter_definitions.StaticChoicesFilterDefinition",
        "params": {
            "fragment_map": {"new": [{"term": {"is_new": True}}]},
            "human_name": _("New courses"),
            "min_doc_count": 0,
            "sorting": "conf",
            "values": {"new": _("First session")},
        },
    },
    "course_runs": {
        "class": "richie.apps.search.filter_definitions.NestingWrapper",
        "params": {
            "filters": {
                "availability": {
                    "class": "richie.apps.search.filter_definitions.AvailabilityFilterDefinition",
                    "params": {
                        "human_name": _("Availability"),
                        "is_drilldown": True,
                        "min_doc_count": 0,
                        "sorting": "conf",
                    },
                },
                "languages": {
                    "class": "richie.apps.search.filter_definitions.LanguagesFilterDefinition",
                    "params": {
                        "human_name": _("Languages"),
                        # There are too many available languages to show them all, all the time.
                        # Eg. 200 languages, 190+ of which will have 0 matching courses.
                        "min_doc_count": 1,
                    },
                },
            }
        },
    },
    "subjects": {
        "class": "richie.apps.search.filter_definitions.IndexableHierarchicalFilterDefinition",
        "params": {
            "human_name": _("Subjects"),
            "is_autocompletable": True,
            "is_searchable": True,
            "min_doc_count": 0,
            "reverse_id": "subjects",
            "term": "categories",
        },
    },
    "organizations": {
        "class": "richie.apps.search.filter_definitions.IndexableHierarchicalFilterDefinition",
        "params": {
            "human_name": _("Organizations"),
            "is_autocompletable": True,
            "is_searchable": True,
            "min_doc_count": 0,
            "reverse_id": "organizations",
        },
    },
    "licences": {
        "class": "richie.apps.search.filter_definitions.IndexableFilterDefinition",
        "params": {
            "human_name": _("Licences"),
            "is_autocompletable": True,
            "is_searchable": True,
            "min_doc_count": 0,
        },
    },
    "pace": {
        "class": "richie.apps.search.filter_definitions.StaticChoicesFilterDefinition",
        "params": {
            "fragment_map": {
                "self-paced": [{"bool": {"must_not": {"exists": {"field": "pace"}}}}],
                "lt-1h": [{"range": {"pace": {"lt": 60}}}],
                "1h-2h": [{"range": {"pace": {"gte": 60, "lte": 120}}}],
                "gt-2h": [{"range": {"pace": {"gt": 120}}}],
            },
            "human_name": _("Weekly pace"),
            "min_doc_count": 0,
            "sorting": "conf",
            "values": {
                "self-paced": _("Self-paced"),
                "lt-1h": _("Less than one hour"),
                "1h-2h": _("One to two hours"),
                "gt-2h": _("More than two hours"),
            },
        },
    },
}


def get_release():
    """Get the current release of the application.

    By release, we mean the release from the version.json file à la Mozilla [1]
    (if any). If this file has not been found, it defaults to "NA".

    [1]
    https://github.com/mozilla-services/Dockerflow/blob/master/docs/version_object.md
    """
    # Try to get the current release from the version.json file generated by the
    # CI during the Docker image build
    try:
        with open(os.path.join(BASE_DIR, "version.json")) as version:
            return json.load(version)["version"]
    except FileNotFoundError:
        return "NA"  # Default: not available


class StyleguideMixin:
    """
    Theme styleguide reference

    Only used to build styleguide page without the need to hardcode properties
    and values into styleguide template.
    """

    STYLEGUIDE = {
        # Available font family names (do not expose montserrat and hind since they
        # are not the real font names
        "fonts": ["din2014", "gotham"],
        # Named color palette
        "palette": [
            "black",
            "black-two",
            "dark",
            "battleship-grey",
            "black-three",
            "black-four",
            "dark-two",
            "warm-grey",
            "warm-grey-two",
            "pale-grey-two",
            "pale-grey",
            "white-three",
            "white",
            "dark-aquamarine",
            "topaz",
            "turquoise-blue",
            "tealish",
            "light-teal",
            "burnt-orange",
            "pumpkin-orange",
            "silver",
        ],
        # Available gradient background
        "gradient_colors": [
            "neutral-gradient",
            "light-gradient",
            "middle-gradient",
            "dark-gradient",
            "tealish-gradient",
        ],
        # Available color schemes
        "schemes": [
            "primary",
            "secondary",
            "tertiary",
            "clear",
            "light",
            "lightest",
            "dark-aquamarine",
            "topaz",
            "tealish",
            "light-teal",
            "peppermint",
            "burnt-orange",
            "pumpkin-orange",
            "clouds",
            "neutral-gradient",
            "light-gradient",
            "middle-gradient",
            "dark-gradient",
            "tealish-gradient",
        ],
    }


class DRFMixin:
    """
    Django Rest Framework configuration mixin.
    NB: DRF picks its settings from the REST_FRAMEWORK namespace on the settings, hence
    the nesting of all our values inside that prop
    """

    REST_FRAMEWORK = {
        "ALLOWED_VERSIONS": ("1.0",),
        "DEFAULT_VERSION": "1.0",
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.SessionAuthentication",
        ),
    }


class Base(StyleguideMixin, DRFMixin, RichieCoursesConfigurationMixin, Configuration):
    """
    This is the base configuration every configuration (aka environnement) should inherit from. It
    is recommended to configure third-party applications by creating a configuration mixins in
    ./configurations and compose the Base configuration with those mixins.

    It depends on an environment variable that SHOULD be defined:

    * DJANGO_SECRET_KEY

    You may also want to override default configuration by setting the following environment
    variables:

    * DJANGO_SENTRY_DSN
    * RICHIE_ES_HOST
    * DB_NAME
    * DB_USER
    * DB_PASSWORD
    * DB_HOST
    * DB_PORT
    """

    DEBUG = False

    SITE_ID = 1

    # Security
    ALLOWED_HOSTS = values.ListValue([])
    SECRET_KEY = "ThisIsAnExampleKeyForDevPurposeOnly"  # nosec
    # System check reference:
    # https://docs.djangoproject.com/en/3.1/ref/checks/#security
    SILENCED_SYSTEM_CHECKS = values.ListValue(
        [
            # Allow the X_FRAME_OPTIONS to be set to "SAMEORIGIN"
            "security.W019"
        ]
    )
    # The X_FRAME_OPTIONS value should be set to "SAMEORIGIN" to display
    # DjangoCMS frontend admin frames. Dockerflow raises a system check security
    # warning with this setting, one should add "security.W019" to the
    # SILENCED_SYSTEM_CHECKS setting (see above).
    X_FRAME_OPTIONS = "SAMEORIGIN"

    # Application definition
    ROOT_URLCONF = "ademe.urls"
    WSGI_APPLICATION = "ademe.wsgi.application"

    # Database
    DATABASES = {
        "default": {
            "ENGINE": values.Value(
                "django.db.backends.postgresql_psycopg2",
                environ_name="DB_ENGINE",
                environ_prefix=None,
            ),
            "NAME": values.Value("ademe", environ_name="DB_NAME", environ_prefix=None),
            "USER": values.Value("ademe", environ_name="DB_USER", environ_prefix=None),
            "PASSWORD": values.Value(
                "pass", environ_name="DB_PASSWORD", environ_prefix=None
            ),
            "HOST": values.Value(
                "localhost", environ_name="DB_HOST", environ_prefix=None
            ),
            "PORT": values.Value(5432, environ_name="DB_PORT", environ_prefix=None),
        }
    }
    DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
    MIGRATION_MODULES = {}

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(DATA_DIR, "media")
    STATIC_ROOT = os.path.join(DATA_DIR, "static")

    # For static files, we want to use a backend that includes a hash in
    # the filename, that is calculated from the file content, so that browsers always
    # get the updated version of each file.
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "base.storage.CDNManifestStaticFilesStorage",
        },
    }

    AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

    # AUTHENTICATION DELEGATION
    RICHIE_AUTHENTICATION_DELEGATION = {
        "BASE_URL": values.Value(
            "", environ_name="AUTHENTICATION_BASE_URL", environ_prefix=None
        ),
        "BACKEND": values.Value(
            "openedx-dogwood",
            environ_name="AUTHENTICATION_BACKEND",
            environ_prefix=None,
        ),
        # PROFILE_URLS are custom links to access to Auth profile views
        # from Richie. Link order will reflect the order of display in frontend.
        # (i) Info - {base_url} is AUTHENTICATION_DELEGATION.BASE_URL
        # (i) If you need to bind user data into href url, wrap the property between ()
        # e.g: for user.username = johndoe, /u/(username) will be /u/johndoe
        "PROFILE_URLS": values.DictValue(
            {
                "dashboard": {
                    "label": _("Dashboard"),
                    "href": _("{base_url:s}/dashboard"),
                },
                "profile": {
                    "label": _("Profile"),
                    "href": _("{base_url:s}/u/(username)"),
                },
                "account": {
                    "label": _("Account"),
                    "href": _("{base_url:s}/account/settings"),
                },
            },
            environ_name="AUTHENTICATION_PROFILE_URLS",
            environ_prefix=None,
        ),
    }

    # LMS
    RICHIE_LMS_BACKENDS = [
        {
            "BACKEND": values.Value(
                "richie.apps.courses.lms.edx.EdXLMSBackend",
                environ_name="EDX_BACKEND",
                environ_prefix=None,
            ),
            "JS_BACKEND": values.Value(
                "openedx-dogwood",
                environ_name="EDX_JS_BACKEND",
                environ_prefix=None,
            ),
            "COURSE_REGEX": values.Value(
                r"^.*/courses/(?P<course_id>.*)/info/?$",
                environ_name="EDX_COURSE_REGEX",
                environ_prefix=None,
            ),
            "COURSE_RUN_SYNC_NO_UPDATE_FIELDS": ["languages"],
            "JS_COURSE_REGEX": values.Value(
                r"^.*/courses/(.*)/info/?$",
                environ_name="EDX_JS_COURSE_REGEX",
                environ_prefix=None,
            ),
            "BASE_URL": values.Value(environ_name="EDX_BASE_URL", environ_prefix=None),
        }
    ]
    RICHIE_COURSE_RUN_SYNC_SECRETS = values.ListValue([])

    # CMS
    # Minimum enrollment count value that would be shown on course detail page
    RICHIE_MINIMUM_COURSE_RUNS_ENROLLMENT_COUNT = values.Value(
        0,
        environ_name="RICHIE_MINIMUM_COURSE_RUNS_ENROLLMENT_COUNT",
        environ_prefix=None,
    )

    # Joanie
    """
    NB: Richie picks all Joanie's settings from the JOANIE_BACKEND namespace in the
    settings, hence the nesting of all Joanie's values inside that prop.

    If BASE_URL is defined, this setting is bound into RICHIE_LMS_BACKENDS to use Joanie
    as a LMS BACKEND.
    """
    JOANIE_BACKEND = {
        "BASE_URL": values.Value(environ_name="JOANIE_BASE_URL", environ_prefix=None),
        "BACKEND": values.Value(
            "richie.apps.courses.lms.joanie.JoanieBackend",
            environ_name="JOANIE_BACKEND",
            environ_prefix=None,
        ),
        "JS_BACKEND": values.Value(
            "joanie", environ_name="JOANIE_JS_BACKEND", environ_prefix=None
        ),
        "COURSE_REGEX": values.Value(
            r"^.*/api/v1.0/(?P<resource_type>(course-runs|products))/(?P<resource_id>[^/]*)/?$",
            environ_name="JOANIE_COURSE_REGEX",
            environ_prefix=None,
        ),
        "JS_COURSE_REGEX": values.Value(
            r"^.*/api/v1.0/(course-runs|products)/([^/]*)/?$",
            environ_name="JOANIE_JS_COURSE_REGEX",
            environ_prefix=None,
        ),
        # Course runs synchronization
        "COURSE_RUN_SYNC_NO_UPDATE_FIELDS": [],
        "DEFAULT_COURSE_RUN_SYNC_MODE": "sync_to_public",
    }

    # Internationalization
    TIME_ZONE = "Europe/Paris"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

    # Templates
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(BASE_DIR, "templates")],
            "OPTIONS": {
                "context_processors": [
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.template.context_processors.media",
                    "django.template.context_processors.csrf",
                    "django.template.context_processors.tz",
                    "sekizai.context_processors.sekizai",
                    "django.template.context_processors.static",
                    "cms.context_processors.cms_settings",
                    "richie.apps.core.context_processors.site_metas",
                    "base.context_processors.site_metas",
                ],
                "loaders": [
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                ],
            },
        }
    ]

    # Placeholders
    CMS_PLACEHOLDER_CONF_OVERRIDES = {
        "courses/cms/course_detail.html course_teaser": {
            "name": _("Teaser"),
            "plugins": ["LTIConsumerPlugin", "VideoPlayerPlugin"],
            "limits": {
                "LTIConsumerPlugin": 1,
                "VideoPlayerPlugin": 1,
            },
        },
    }

    RICHIE_SIMPLETEXT_CONFIGURATION = [
        {
            "placeholders": ["course_description"],
            "ckeditor": "CKEDITOR_LIMITED_CONFIGURATION",
            "max_length": 2000,
        },
        *RichieCoursesConfigurationMixin.RICHIE_SIMPLETEXT_CONFIGURATION,
    ]

    MIDDLEWARE = (
        "richie.apps.core.cache.LimitBrowserCacheTTLHeaders",
        "cms.middleware.utils.ApphookReloadMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.locale.LocaleMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "dockerflow.django.middleware.DockerflowMiddleware",
        "cms.middleware.user.CurrentUserMiddleware",
        "cms.middleware.page.CurrentPageMiddleware",
        "cms.middleware.toolbar.ToolbarMiddleware",
        "cms.middleware.language.LanguageCookieMiddleware",
        "dj_pagination.middleware.PaginationMiddleware",
    )

    INSTALLED_APPS = (
        # ADEME stuff
        "base",
        # Richie stuff
        "richie.apps.demo",
        "richie.apps.search",
        "richie.apps.courses",
        "richie.apps.core",
        "richie.plugins.glimpse",
        "richie.plugins.html_sitemap",
        "richie.plugins.large_banner",
        "richie.plugins.lti_consumer",
        "richie.plugins.nesteditem",
        "richie.plugins.plain_text",
        "richie.plugins.section",
        "richie.plugins.simple_picture",
        "richie.plugins.simple_text_ckeditor",
        "richie",
        # Third party apps
        "dj_pagination",
        "dockerflow.django",
        "parler",
        "rest_framework",
        "storages",
        # django-autocomplete-light
        "dal",
        "dal_select2",
        # Django-cms
        "djangocms_admin_style",
        "djangocms_googlemap",
        "djangocms_link",
        "djangocms_picture",
        "djangocms_text_ckeditor",
        "djangocms_video",
        "django_check_seo",
        "cms",
        "menus",
        "sekizai",
        "treebeard",
        "filer",
        "easy_thumbnails",
        # Django
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.admin",
        "django.contrib.sites",
        "django.contrib.sitemaps",
        "django.contrib.staticfiles",
        "django.contrib.messages",
        "django.contrib.humanize",
    )

    RICHIE_FILTERS_CONFIGURATION = FILTERS_CONFIGURATION
    RICHIE_FILTERS_PRESENTATION = [
        "new",
        "availability",
        "subjects",
        "organizations",
        "languages",
        "licences",
        "pace",
    ]

    # Languages
    # - Django
    LANGUAGE_CODE = "fr"

    # Careful! Languages should be ordered by priority, as this tuple is used to get
    # fallback/default languages throughout the app.
    # Use "en" as default as it is the language that is most likely to be spoken by any visitor
    # when their preferred language, whatever it is, is unavailable
    LANGUAGES = (("fr", _("French")), ("en", _("English")))

    # - Django CMS
    CMS_LANGUAGES = {
        "default": {
            "public": True,
            "hide_untranslated": False,
            "redirect_on_fallback": True,
            "fallbacks": ["en", "fr"],
        },
        1: [
            {
                "public": False,
                "code": "en",
                "hide_untranslated": False,
                "name": _("English"),
                "fallbacks": ["fr"],
                "redirect_on_fallback": False,
            },
            {
                "public": True,
                "code": "fr",
                "hide_untranslated": False,
                "name": _("French"),
                "fallbacks": ["en"],
                "redirect_on_fallback": False,
            },
        ],
    }

    # - Django Parler
    PARLER_LANGUAGES = CMS_LANGUAGES

    # Permisions
    # - Django CMS
    CMS_PERMISSION = True

    # - Django Filer
    FILER_ENABLE_PERMISSIONS = True
    FILER_IS_PUBLIC_DEFAULT = True

    # - Django Pagination
    PAGINATION_INVALID_PAGE_RAISES_404 = True
    PAGINATION_DEFAULT_WINDOW = 2
    PAGINATION_DEFAULT_MARGIN = 1

    # Logging
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s "
                "%(process)d %(thread)d %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            }
        },
        "loggers": {
            "django.db.backends": {
                "level": "ERROR",
                "handlers": ["console"],
                "propagate": False,
            }
        },
    }

    # Web Analytics
    WEB_ANALYTICS = values.DictValue(
        None,
        environ_name="WEB_ANALYTICS",
        environ_prefix=None,
    )

    # Demo
    RICHIE_DEMO_SITE_DOMAIN = values.Value(
        default="localhost:8000",
        environ_name="RICHIE_DEMO_SITE_DOMAIN",
        environ_prefix=None,
    )
    RICHIE_DEMO_FIXTURES_DIR = os.path.join(BASE_DIR, "base", "fixtures")

    # Elasticsearch
    RICHIE_ES_HOST = values.Value(
        "elasticsearch", environ_name="RICHIE_ES_HOST", environ_prefix=None
    )
    RICHIE_ES_INDICES_PREFIX = values.Value(
        default="richie", environ_name="RICHIE_ES_INDICES_PREFIX", environ_prefix=None
    )
    RICHIE_ES_STATE_WEIGHTS = values.ListValue(None)

    # LTI Content
    RICHIE_LTI_PROVIDERS = {
        "marsha": {
            "oauth_consumer_key": values.Value(
                "InsecureOauthConsumerKey",
                environ_name="LTI_OAUTH_CONSUMER_KEY",
                environ_prefix=None,
            ),
            "shared_secret": values.Value(
                "InsecureSharedSecret",
                environ_name="LTI_SHARED_SECRET",
                environ_prefix=None,
            ),
            "base_url": values.Value(
                "https://marsha\.education/lti/videos/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",  # noqa
                environ_name="LTI_BASE_URL",
                environ_prefix=None,
            ),
            "display_name": "Marsha Video",
            "is_base_url_regex": True,
            "automatic_resizing": True,
            "inline_ratio": 0.5625,
        }
    }

    # Cache
    CACHES = values.DictValue(
        {
            "default": {
                "BACKEND": values.Value(
                    "base.cache.RedisCacheWithFallback",
                    environ_name="CACHE_DEFAULT_BACKEND",
                    environ_prefix=None,
                ),
                "LOCATION": values.Value(
                    "mymaster/redis-sentinel:26379,redis-sentinel:26379/0",
                    environ_name="CACHE_DEFAULT_LOCATION",
                    environ_prefix=None,
                ),
                "OPTIONS": values.DictValue(
                    {
                        "CLIENT_CLASS": "richie.apps.core.cache.SentinelClient",
                    },
                    environ_name="CACHE_DEFAULT_OPTIONS",
                    environ_prefix=None,
                ),
                "TIMEOUT": values.IntegerValue(
                    300, environ_name="CACHE_DEFAULT_TIMEOUT", environ_prefix=None
                ),
            },
            "memory_cache": {
                "BACKEND": values.Value(
                    "django.core.cache.backends.locmem.LocMemCache",
                    environ_name="CACHE_FALLBACK_BACKEND",
                    environ_prefix=None,
                ),
                "LOCATION": values.Value(
                    None,
                    environ_name="CACHE_FALLBACK_LOCATION",
                    environ_prefix=None,
                ),
                "OPTIONS": values.DictValue(
                    {},
                    environ_name="CACHE_FALLBACK_OPTIONS",
                    environ_prefix=None,
                ),
            },
            "search": {
                "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
                "LOCATION": "search_cache",
                "TIMEOUT": 60,
            },
        }
    )

    # For more details about CMS_CACHE_DURATION, see :
    # http://docs.django-cms.org/en/latest/reference/configuration.html#cms-cache-durations
    CMS_CACHE_DURATIONS = values.DictValue(
        {"menus": 3600, "content": 86400, "permissions": 86400}
    )
    MAX_BROWSER_CACHE_TTL = 600

    # Sessions
    SESSION_ENGINE = values.Value("django.contrib.sessions.backends.cache")

    # Sentry
    SENTRY_DSN = values.Value(None, environ_name="SENTRY_DSN")

    # Admin
    # - Django CMS
    # Maximum children nodes to allow a parent to be unfoldable
    # in the page tree admin view
    CMS_PAGETREE_DESCENDANTS_LIMIT = 80

    # - Django CMS Check SEO
    # Excludes all elements that are not related to the page content
    DJANGO_CHECK_SEO_EXCLUDE_CONTENT = (
        "body > svg, #main-menu, .body-footer, .body-mentions"
    )

    # Permissions
    RICHIE_ORGANIZATION_ADMIN_ROLE = {
        "django_permissions": [
            # Objects
            "cms.change_page",
            "cms.add_title",
            "cms.change_title",
            "courses.change_course",
            "cms.use_structure",
            # Filer
            "filer.add_file",
            "filer.change_file",
            "filer.view_file",
            "filer.add_image",
            "filer.change_image",
            "filer.view_image",
            "filer.can_use_directory_listing",
            "filer.change_folder",
            "filer.view_folder",
            # Plugins
            "djangocms_link.add_link",
            "djangocms_link.change_link",
            "djangocms_link.delete_link",
            "djangocms_link.view_link",
            "djangocms_picture.add_picture",
            "djangocms_picture.change_picture",
            "djangocms_picture.delete_picture",
            "djangocms_picture.view_picture",
            "djangocms_text_ckeditor.add_text",
            "djangocms_text_ckeditor.change_text",
            "djangocms_text_ckeditor.delete_text",
            "djangocms_text_ckeditor.view_text",
            "djangocms_video.add_videoplayer",
            "djangocms_video.change_videoplayer",
            "djangocms_video.delete_videoplayer",
            "djangocms_video.view_videoplayer",
            "djangocms_video.add_videosource",
            "djangocms_video.change_videosource",
            "djangocms_video.delete_videosource",
            "djangocms_video.view_videosource",
            "djangocms_video.add_videotrack",
            "djangocms_video.change_videotrack",
            "djangocms_video.delete_videotrack",
            "djangocms_video.view_videotrack",
            "plain_text.add_plaintext",
            "plain_text.change_plaintext",
            "plain_text.delete_plaintext",
            "plain_text.view_plaintext",
            "section.add_section",
            "section.change_section",
            "section.delete_section",
            "section.view_section",
            "simple_text_ckeditor.add_simpletext",
            "simple_text_ckeditor.change_simpletext",
            "simple_text_ckeditor.delete_simpletext",
            "simple_text_ckeditor.view_simpletext",
            "courses.add_personpluginmodel",
            "courses.change_personpluginmodel",
            "courses.delete_personpluginmodel",
            "courses.view_personpluginmodel",
            "courses.add_categorypluginmodel",
            "courses.change_categorypluginmodel",
            "courses.delete_categorypluginmodel",
            "courses.view_categorypluginmodel",
            "courses.add_licencepluginmodel",
            "courses.change_licencepluginmodel",
            "courses.delete_licencepluginmodel",
            "courses.view_licencepluginmodel",
            "courses.view_category",
            "courses.view_person",
            "glimpse.add_glimpse",
            "glimpse.change_glimpse",
            "glimpse.delete_glimpse",
            "glimpse.view_glimpse",
            "lti_consumer.add_lticonsumer",
            "lti_consumer.change_lticonsumer",
            "lti_consumer.delete_lticonsumer",
            "lti_consumer.view_lticonsumer",
            "nesteditem.add_nesteditem",
            "nesteditem.change_nesteditem",
            "nesteditem.delete_nesteditem",
            "nesteditem.view_nesteditem",
        ],
    }

    RICHIE_COURSE_ADMIN_ROLE = {
        "django_permissions": [
            # Objects
            "cms.change_page",
            "cms.add_title",
            "cms.change_title",
            "cms.use_structure",
            # Filer
            "filer.add_file",
            "filer.change_file",
            "filer.view_file",
            "filer.add_image",
            "filer.change_image",
            "filer.view_image",
            "filer.can_use_directory_listing",
            "filer.change_folder",
            "filer.view_folder",
            # Plugins
            "djangocms_link.add_link",
            "djangocms_link.change_link",
            "djangocms_link.delete_link",
            "djangocms_link.view_link",
            "djangocms_picture.add_picture",
            "djangocms_picture.change_picture",
            "djangocms_picture.delete_picture",
            "djangocms_picture.view_picture",
            "djangocms_text_ckeditor.add_text",
            "djangocms_text_ckeditor.change_text",
            "djangocms_text_ckeditor.delete_text",
            "djangocms_text_ckeditor.view_text",
            "djangocms_video.add_videoplayer",
            "djangocms_video.change_videoplayer",
            "djangocms_video.delete_videoplayer",
            "djangocms_video.view_videoplayer",
            "djangocms_video.add_videosource",
            "djangocms_video.change_videosource",
            "djangocms_video.delete_videosource",
            "djangocms_video.view_videosource",
            "djangocms_video.add_videotrack",
            "djangocms_video.change_videotrack",
            "djangocms_video.delete_videotrack",
            "djangocms_video.view_videotrack",
            "plain_text.add_plaintext",
            "plain_text.change_plaintext",
            "plain_text.delete_plaintext",
            "plain_text.view_plaintext",
            "section.add_section",
            "section.change_section",
            "section.delete_section",
            "section.view_section",
            "simple_text_ckeditor.add_simpletext",
            "simple_text_ckeditor.change_simpletext",
            "simple_text_ckeditor.delete_simpletext",
            "simple_text_ckeditor.view_simpletext",
            "courses.add_personpluginmodel",
            "courses.change_personpluginmodel",
            "courses.delete_personpluginmodel",
            "courses.view_personpluginmodel",
            "courses.add_categorypluginmodel",
            "courses.change_categorypluginmodel",
            "courses.delete_categorypluginmodel",
            "courses.view_categorypluginmodel",
            "courses.add_licencepluginmodel",
            "courses.change_licencepluginmodel",
            "courses.delete_licencepluginmodel",
            "courses.view_licencepluginmodel",
            "courses.view_category",
            "courses.view_person",
            "glimpse.add_glimpse",
            "glimpse.change_glimpse",
            "glimpse.delete_glimpse",
            "glimpse.view_glimpse",
            "lti_consumer.add_lticonsumer",
            "lti_consumer.change_lticonsumer",
            "lti_consumer.delete_lticonsumer",
            "lti_consumer.view_lticonsumer",
            "nesteditem.add_nesteditem",
            "nesteditem.change_nesteditem",
            "nesteditem.delete_nesteditem",
            "nesteditem.view_nesteditem",
        ],
    }

    # - Cookie consent (Tarte au citron)
    TARTEAUCITRON_TAG_ID = values.Value(
        None, environ_name="TARTEAUCITRON_TAG_ID", environ_prefix=None
    )

    # pylint: disable=invalid-name
    @property
    def ENVIRONMENT(self):
        """Environment in which the application is launched."""
        return self.__class__.__name__.lower()

    # pylint: disable=invalid-name
    @property
    def RELEASE(self):
        """
        Return the release information.

        Delegate to the module function to enable easier testing.
        """
        return get_release()

    # pylint: disable=invalid-name
    @property
    def CMS_CACHE_PREFIX(self):
        """
        Set cache prefix specific to release so existing cache is invalidated for new deployments.
        """
        return f"cms_{get_release():s}_"

    @classmethod
    def post_setup(cls):
        """Post setup configuration.
        This is the place where you can configure settings that require other
        settings to be loaded.
        """
        super().post_setup()

        # The SENTRY_DSN setting should be available to activate sentry for an environment
        if cls.SENTRY_DSN is not None:
            sentry_sdk.init(
                dsn=cls.SENTRY_DSN,
                environment=cls.__name__.lower(),
                release=get_release(),
                integrations=[DjangoIntegration()],
            )
            sentry_sdk.set_tag("application", "backend")

        # If a Joanie Backend has been configured, we add it into LMS_BACKENDS dict
        if cls.JOANIE_BACKEND.get("BASE_URL") is not None:
            cls.RICHIE_LMS_BACKENDS.append(cls.JOANIE_BACKEND)

        # Customize DjangoCMS placeholders configuration
        cls.CMS_PLACEHOLDER_CONF = merge_dict(
            cls.CMS_PLACEHOLDER_CONF, cls.CMS_PLACEHOLDER_CONF_OVERRIDES
        )


class Development(Base):
    """
    Development environment settings

    We set DEBUG to True and configure the server to respond from all hosts.
    """

    DEBUG = True
    ALLOWED_HOSTS = ["*"]

    CACHES = {"default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"}}

    # Django Check SEO
    DJANGO_CHECK_SEO_FORCE_HTTP = True

    RICHIE_DEMO_PAGES_INFO = {
        "annex": {
            "title": {"en": "Annex", "fr": "Annexe"},
            "in_navigation": False,
            "template": "richie/single_column.html",
            "children": {
                "annex__about": {
                    "title": {"en": "About", "fr": "A propos"},
                    "in_navigation": True,
                    "template": "richie/single_column.html",
                },
                "annex__sitemap": {
                    "title": {"en": "Sitemap", "fr": "Plan de site"},
                    "in_navigation": True,
                    "template": "richie/single_column.html",
                },
                "contact": {
                    "title": {"en": "Contact", "fr": "Contact"},
                    "in_navigation": True,
                    "template": "richie/single_column.html",
                },
                "login-error": {
                    "title": {"en": "Login error", "fr": "Erreur de connexion"},
                    "in_navigation": False,
                    "template": "richie/single_column.html",
                },
            },
        },
    }


class Test(Base):
    """Test environment settings"""

    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }


class ContinuousIntegration(Test):
    """
    Continous Integration environment settings

    nota bene: it should inherit from the Test environment.
    """


class Production(Base):
    """Production environment settings

    You must define the DJANGO_ALLOWED_HOSTS environment variable in Production
    configuration (and derived configurations):

    DJANGO_ALLOWED_HOSTS="foo.com,foo.fr"
    """

    # Security
    SECRET_KEY = values.SecretValue()
    CSRF_COOKIE_SECURE = True
    CSRF_TRUSTED_ORIGINS = values.ListValue([])
    CSRF_COOKIE_DOMAIN = values.Value(None)
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True

    STORAGES = {
        "default": {
            "BACKEND": "base.storage.MediaStorage",
        },
        "staticfiles": {
            "BACKEND": "base.storage.CDNManifestStaticFilesStorage",
        },
    }
    AWS_DEFAULT_ACL = None
    AWS_LOCATION = "media"

    AWS_ACCESS_KEY_ID = values.SecretValue()
    AWS_SECRET_ACCESS_KEY = values.SecretValue()

    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }

    AWS_S3_REGION_NAME = values.Value("eu-west-1")

    AWS_MEDIA_BUCKET_NAME = values.Value("production-ademe-media")

    # CDN domain for static/media urls. It is passed to the frontend to load built chunks
    CDN_DOMAIN = values.Value()

    @property
    def TEXT_CKEDITOR_BASE_PATH(self):
        """Configure CKEditor with an absolute url as base path to point to CloudFront."""
        return "//{!s}/static/djangocms_text_ckeditor/ckeditor/".format(self.CDN_DOMAIN)


class Feature(Production):
    """
    Feature environment settings

    nota bene: it should inherit from the Production environment.
    """

    AWS_MEDIA_BUCKET_NAME = values.Value("feature-ademe-media")


class Staging(Production):
    """
    Staging environment settings

    nota bene: it should inherit from the Production environment.
    """

    AWS_MEDIA_BUCKET_NAME = values.Value("staging-ademe-media")


class PreProduction(Production):
    """
    Pre-production environment settings

    nota bene: it should inherit from the Production environment.
    """

    AWS_MEDIA_BUCKET_NAME = values.Value("preprod-ademe-media")
