#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July  30 15:00:00 2023

@Author: Nicanor Kyamba
"""
import unittest
from typing import Any, Dict
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """
        Test the public_repos_url method

        Returns:
            None
        """
        # Use patch with new_callable=PropertyMock to mock the org property
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            # Configure the PropertyMock to return the specified payload
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }

            # Arrange
            org_name = "google"
            client = GithubOrgClient(org_name)

            # Act
            result = client._public_repos_url

            # Assert
            self.assertEqual(
                result, "https://api.github.com/users/google/repos"
            )
