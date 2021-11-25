"""
    Geocoding and Search API v7

    This document describes the Geocoding and Search API.  # noqa: E501

    The version of the OpenAPI document: 7.65
    Generated by: https://openapi-generator.tech
"""


import unittest

import geocoding
from geocoding.api.default_api import DefaultApi  # noqa: E501


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_autocomplete_get(self):
        """Test case for autocomplete_get

        Autocomplete  # noqa: E501
        """
        pass

    def test_autosuggest_get(self):
        """Test case for autosuggest_get

        Autosuggest  # noqa: E501
        """
        pass

    def test_browse_get(self):
        """Test case for browse_get

        Browse  # noqa: E501
        """
        pass

    def test_discover_get(self):
        """Test case for discover_get

        Discover  # noqa: E501
        """
        pass

    def test_geocode_get(self):
        """Test case for geocode_get

        Geocode  # noqa: E501
        """
        pass

    def test_lookup_get(self):
        """Test case for lookup_get

        Lookup By ID  # noqa: E501
        """
        pass

    def test_revgeocode_get(self):
        """Test case for revgeocode_get

        Reverse Geocode  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
