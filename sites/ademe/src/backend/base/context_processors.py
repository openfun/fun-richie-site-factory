"""
Template context_processors
"""

from django.conf import settings

from cms.utils import get_current_site


def site_metas(request):
    """
    Context processor to add all information required by frontend.
    """

    context = {
        "PRIVACY_CONTEXT": {
            "tarteaucitron": {
                "domain": get_current_site(),
                "id": getattr(settings, "TARTEAUCITRON_TAG_ID"),
                "locale": request.LANGUAGE_CODE,
            }
        }
    }

    return context
