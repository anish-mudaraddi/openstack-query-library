from unittest.mock import patch

import pytest

from openstackquery.api.query_api import QueryAPI
from openstackquery.api.query_objects import (
    AggregateQuery,
    FlavorQuery,
    HypervisorQuery,
    ImageQuery,
    ProjectQuery,
    ServerQuery,
    UserQuery,
    get_common,
)
from openstackquery.mappings.server_mapping import ServerMapping


def test_get_common():
    """
    tests that function _get_common works
    should use QueryFactory to setup a query object with given mapping class
    """
    query_api_instance = get_common(ServerMapping)
    assert isinstance(
        query_api_instance, QueryAPI
    ), "get_common should return an instance of QueryAPI"


@pytest.fixture(name="run_query_test_case")
def run_query_test_case_fixture():
    """
    Fixture to test each query function
    """

    def _run_query_test_case(mock_query_func, expected_mapping):
        """
        tests each given query_function calls get_common with expected mapping class
        """

        with patch("openstackquery.api.query_objects.get_common") as mock_get_common:
            res = mock_query_func()
            mock_get_common.assert_called_once_with(expected_mapping)
        assert res == mock_get_common.return_value

    return _run_query_test_case


def test_server_query(run_query_test_case):
    """
    tests that function ServerQuery works
    should call get_common with ServerMapping
    """
    with patch("openstackquery.api.query_objects.ServerMapping") as mock_server_mapping:
        run_query_test_case(ServerQuery, mock_server_mapping)


def test_user_query(run_query_test_case):
    """
    tests that function UserQuery works
    should call get_common with UserMapping
    """
    with patch("openstackquery.api.query_objects.UserMapping") as mock_user_mapping:
        run_query_test_case(UserQuery, mock_user_mapping)


def test_flavor_query(run_query_test_case):
    """
    tests that function FlavorQuery works
    should call get_common with FlavorMapping
    """
    with patch("openstackquery.api.query_objects.FlavorMapping") as mock_flavor_mapping:
        run_query_test_case(FlavorQuery, mock_flavor_mapping)


def test_project_query(run_query_test_case):
    """
    tests that function ProjectQuery works
    should call get_common with ProjectMapping
    """
    with patch(
        "openstackquery.api.query_objects.ProjectMapping"
    ) as mock_project_mapping:
        run_query_test_case(ProjectQuery, mock_project_mapping)


def test_image_query(run_query_test_case):
    """
    tests that function ImageQuery works
    should call get_common with ImageMapping
    """
    with patch("openstackquery.api.query_objects.ImageMapping") as mock_project_mapping:
        run_query_test_case(ImageQuery, mock_project_mapping)


def test_hypervisor_query(run_query_test_case):
    """
    tests that function HypervisorQuery works
    should call get_common with HypervisorMapping
    """
    with patch(
        "openstackquery.api.query_objects.HypervisorMapping"
    ) as mock_project_mapping:
        run_query_test_case(HypervisorQuery, mock_project_mapping)


def test_aggregate_query(run_query_test_case):
    """
    tests that function AggregateQuery works
    should call get_common with AggregateMapping
    """
    with patch(
        "openstackquery.api.query_objects.AggregateMapping"
    ) as mock_project_mapping:
        run_query_test_case(AggregateQuery, mock_project_mapping)
