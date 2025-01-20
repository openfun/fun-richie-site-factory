"""Test suite for the base app middlewares."""

from django.core.exceptions import BadRequest
from django.http import HttpRequest
from django.test import TestCase

from base.middleware import MalformedQueryStringMiddleware


class TestMalformedQueryStringMiddleware(TestCase):
    """Test case for the MalformedQueryStringMiddleware."""

    def test_malformed_query_string_middleware_self(self):
        """
        If a query string is malformed, a bad request should be returned.
        """
        request = HttpRequest()
        request.method = "GET"
        request.META["QUERY_STRING"] = "foo=bar?bar=foo"
        request.path = "/"

        with self.assertRaises(BadRequest):
            MalformedQueryStringMiddleware(request).process_request(request)

        # Encoded chars should be decoded
        request.META["QUERY_STRING"] = "foo=bar%3Fbar=foo"

        with self.assertRaises(BadRequest):
            MalformedQueryStringMiddleware(request).process_request(request)

    def test_malformed_query_string_middleware_ignore_api_endpoint(self):
        """
        If the request path is an api endpoint, the middleware should ignore it.
        """
        request = HttpRequest()
        request.method = "GET"
        request.META["QUERY_STRING"] = "q=Hello?"
        request.path = "/api/v1.0/search/"

        MalformedQueryStringMiddleware(request).process_request(request)

    def test_malformed_query_string_middleware_ignore_non_get_request(self):
        """
        If the request method is something else than GET,
        the middleware should ignore it.
        """
        request = HttpRequest()
        request.method = "POST"
        request.META["QUERY_STRING"] = "q=Hello?"
        request.path = "/api/v1.0/search/"

        MalformedQueryStringMiddleware(request).process_request(request)
