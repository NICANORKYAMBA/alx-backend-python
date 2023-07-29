#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July  28 13:00:00 2023

@Author: Nicanor Kyamba
"""
import unittest
from unittest.mock import patch, Mock
from typing import Any, Sequence, Mapping
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected_path: Sequence) -> Any:
        """
        Test method for access_nested_map

        Args:
            nested_map (Mapping): nested map
            path (Sequence): path
            expected_path (Sequence): expected path

        Returns:
            Any: return
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_path)

    @parameterized.expand([
        ({}, {"a", }, KeyError),
        ({"a": 1}, {"a", "b"}, KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected_error: Any) -> Any:
        """
        Test method for access_nested_map_exception

        Returns:
            Any: return
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json
    """
    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping) -> Any:
        """
        Test method for get_json

        Args:
            test_url (str): test url
            test_payload (Mapping): test payload

        Returns:
            Any: return
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch("requests.get", return_value=mock_response):
            self.assertEqual(get_json(test_url), test_payload)
