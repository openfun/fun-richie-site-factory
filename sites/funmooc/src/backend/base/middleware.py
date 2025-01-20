"""Middleware for the FUN Mooc base app."""

from urllib.parse import unquote, urlparse

from django.core.exceptions import BadRequest
from django.utils.deprecation import MiddlewareMixin


class MalformedQueryStringMiddleware(MiddlewareMixin):
    """
    A middleware to detect malformed query string from the request. It detects malformed
    query string then raise a BadRequest exception if one is found.
    """

    def process_request(self, request):
        """
        Catch the path of the request and raise a BadRequest exception if
        the query string is malformed (contains several ?).
        Api endpoints and non GET requests are ignored.
        """
        parsed_url = urlparse(request.get_full_path())

        if request.method == "GET" and not parsed_url.path.startswith("/api/v"):
            if unquote(parsed_url.query).find("?") != -1:
                raise BadRequest("URL query string is malformed.")
