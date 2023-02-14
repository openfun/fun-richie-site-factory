"""Test fun-mooc templates."""
from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import TestCase
from django.utils import translation

import lxml.html  # nosec
from richie.apps.core.factories import PageFactory


class BaseTemplateTestCase(TestCase):
    """Test the base template."""

    def test_base_template_localized_topbar_logo(self):
        """
        Test that the base template has a localized topbar logo
        for each enabled languages.
        """
        page = PageFactory(
            template="richie/base.html",
            should_publish=True,
        )

        for (language_code, _) in settings.LANGUAGES:
            # Get page for the current language code
            with translation.override(language_code):
                response = self.client.get(page.get_public_url())

            html = lxml.html.fromstring(str(response.content))
            topbar_logo = html.cssselect(".topbar__logo")

            # Now we should get the logo for the current language
            logo_path = topbar_logo[0].attrib["src"]
            logo_filename = f"logo-{language_code}.svg"
            self.assertEqual(logo_path, f"/static/richie/images/{logo_filename}")

            # Check that the logo file exists in the static folder
            self.assertIsNotNone(finders.find(f"richie/images/{logo_filename}"))
