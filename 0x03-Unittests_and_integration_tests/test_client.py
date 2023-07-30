#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun July  30 15:00:00 2023

@Author: Nicanor Kyamba
"""
import unittest
from typing import Any, Dict
from unittest.mock import patch, PropertyMock, MagicMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from requests import HTTPError
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test public repos using mock

        Args:
            mock_get_json (MagicMock): Mock object for get_json method
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 1587145,
                    "name": "search",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1101001,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/search",
                    "created_at": "2022-03-03T22:52:33Z",
                    "updated_at": "2023-07-07T11:15:01Z",
                    "has_issues": True,
                    "forks": 90,
                    "default_branch": "master",
                },
                {
                    "id": 7787865,
                    "name": "task_manager",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": "123456789",
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/task_manager",
                    "created_at": "2022-03-03T22:52:33Z",
                    "updated_at": "2023-07-07T11:15:01Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "search",
                    "task_manager",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result) -> None:
        """
        Test the has_license method

        Args:
            repo (dict): Repository data with a license key
            license_key (str): License key to check
            expected_result (bool): Expected result of has_license method

        Returns:
            None
        """
        # Arrange
        client = GithubOrgClient("google")

        # Act
        result = client.has_license(repo, license_key)

        # Assert
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient class
    """
    @classmethod
    def setUpClass(cls) -> None:
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        Test the public_repos method
        """
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(
            result,
            self.expected_repos
        )

    def test_public_repos_with_license(self) -> None:
        """
        Test the public_repos method with a license
        """
        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(
            result,
            self.apache2_repos
        )
