#!/usr/bin/env python3
"""
Unittests for the utils.access_nested_map function
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, requests
from typing import Dict


class TestAccessNestedMap(unittest.TestCase):
    """
    Class for testing the utils.access_nested_map function
    """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Class for testing utils.get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict
            ) -> None:
        """Test the return of requests.get method
        """
        attrs = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
