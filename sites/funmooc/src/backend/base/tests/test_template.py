"""Test fun-mooc templates."""

from django.conf import settings
from django.contrib.staticfiles import finders
from django.test import TestCase
from django.utils import translation

import lxml.html  # nosec
from richie.apps.core.factories import PageFactory, UserFactory
from richie.apps.courses.factories import CourseFactory


class TemplateBaseTestCase(TestCase):
    """Test the base template."""

    def test_template_base_localized_topbar_logo(self):
        """
        Test that the base template has a localized topbar logo
        for each enabled languages.
        """
        page = PageFactory(
            template="richie/base.html",
            should_publish=True,
        )

        for language_code, _ in settings.LANGUAGES:
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


class TemplateProfessionalTrainingDetailTestCase(TestCase):
    """Test the professional training detail template."""

    def test_template_professional_training(self):
        """A professional training template should exist."""
        user = UserFactory(is_staff=True, is_superuser=True)
        self.client.login(username=user.username, password="password")  # nosec

        page = PageFactory(template="cms/professional_training_detail.html")
        CourseFactory(extended_object=page)
        page_url = page.get_absolute_url()
        url = f"{page_url:s}?edit"

        # The template should extend the `courses/cms/course_detail.html` template
        with self.assertTemplateUsed("courses/cms/course_detail.html"):
            response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        html = lxml.html.fromstring(str(response.content.decode("utf-8")))

        course_skills = html.cssselect(".course-detail__skills")[0]
        course_skills_title = course_skills.cssselect("h2")[0]
        course_skills_description = course_skills.cssselect("p")[0]

        self.assertEqual(course_skills_title.text_content(), "Objectifs")
        self.assertEqual(
            course_skills_description.text_content(),
            "À la fin de cette formation, vous serez capable de :",
        )

        course_program = html.cssselect(".course-detail__plan")[0]
        course_program_title = course_program.cssselect("h2")[0]
        course_program_description = course_program.cssselect("p")[0]
        self.assertEqual(course_program_title.text_content(), "Programme")
        self.assertEqual(
            course_program_description.text_content(),
            "Détaillez ici le programme de la formation.",
        )
