"""Middleware for the Ademe base app."""

import re
from urllib.parse import unquote, urlparse

from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin


class MalformedQueryStringMiddleware(MiddlewareMixin):
    """
    A middleware to detect malformed query string from the request. It detects malformed
    query string then raise a BadRequest exception if one is found.
    """

    EXCLUDED_PATH_REGEX = (
        r"(^/api/v)"  # Exclude API endpoints
        r"|"
        r"(^/[a-z-]+/admin/)"  # Exclude admin paths
    )

    def process_request(self, request):
        """
        Catch the path of the request and raise a BadRequest exception if
        the query string is malformed (contains several ?).
        Api endpoints and non GET requests are ignored.
        """
        parsed_url = urlparse(request.get_full_path())

        if (
            request.method == "GET"
            and re.search(self.EXCLUDED_PATH_REGEX, parsed_url.path) is None
        ):
            if unquote(parsed_url.query).find("?") != -1:
                return HttpResponseBadRequest("URL query string is malformed.")

        return None
