#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July  28 13:00:00 2023

@Author: Nicanor Kyamba
"""
import unittest
from typing import Any, Sequence, Mapping
from parameterized import parameterized
from utils import access_nested_map


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
