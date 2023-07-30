#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July  30 15:00:00 2023

@Author: Nicanor Kyamba
"""
import unittest
from typing import Any, Dict
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    async def test_org(self, org_name: str, mock_get_json: Any) -> None:
        """
        Test the org method

        Args:
            org_name (str): The name of the org
            mock_get_json (Any): Mock the get_json method

        Returns:
            None
        """
        mock_get_json.return_value = {"name": org_name}

        client: GithubOrgClient = GithubOrgClient(org_name)
        result: Dict[str, Any] = await client.org()

        self.assertEqual(result, {"name": org_name})
        mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(
                    org_name))
