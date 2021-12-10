import unittest
import responses
from requests.exceptions import RequestException, ConnectionError, Timeout
from . import BaseTest
import services


class TestServices(BaseTest):

    @responses.activate
    def test__call_on_RequestException(self):
        """Testing retries on exceptions"""

        responses.add(
            responses.GET,
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
            body=RequestException()
        )

        with self.assertRaises(RequestException):
            services.call('/v1/cryptocurrency/quotes/latest', payload={})

    @responses.activate
    def test__call_on_ConnectionError(self):
        """Testing retries on exceptions"""

        responses.add(
            responses.GET,
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
            body=ConnectionError()
        )

        with self.assertRaises(ConnectionError):
            services.call('/v1/cryptocurrency/quotes/latest', payload={})

    @responses.activate
    def test__call_on_Timeout(self):
        """Testing retries on exceptions"""

        responses.add(
            responses.GET,
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest',
            body=Timeout()
        )

        with self.assertRaises(Timeout):
            services.call('/v1/cryptocurrency/quotes/latest', payload={})
