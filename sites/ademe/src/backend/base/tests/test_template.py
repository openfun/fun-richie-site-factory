"""Test ademe templates."""

from django.contrib.sites.models import Site
from django.test import TestCase, override_settings

from richie.apps.core.factories import PageFactory


class BaseTemplateTestCase(TestCase):
    """Test the base template."""

    @override_settings(TARTEAUCITRON_TAG_ID="123456")
    def test_base_template_tarteaucitron_tag(self):
        """
        Test that the base template has script tag to load tarteaucitron tag which
        depends on the current language, the current site and the tarteaucitron tag id
        """
        # Override default site to ensure that the current site is really used
        site = Site.objects.get(pk=1)
        site.domain = "www.mbd.fr"
        site.save()

        page = PageFactory(
            template="richie/base.html",
            should_publish=True,
        )

        response = self.client.get(page.get_public_url())
        self.assertContains(
            response,
            'src="https://tarteaucitron.io/load.js?domain=www.mbd.fr&uuid=123456&locale=fr"',
        )
