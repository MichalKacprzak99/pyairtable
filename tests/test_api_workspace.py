import pytest

from pyairtable.api.workspace import Workspace


@pytest.fixture
def workspace(api):
    return Workspace(api, "wspFakeWorkspaceId")


@pytest.fixture
def mock_info(workspace, requests_mock, sample_json):
    return requests_mock.get(workspace.url, json=sample_json("Workspace"))


def test_info(workspace, mock_info):
    assert workspace.info().id == "wspmhESAta6clCCwF"
    assert workspace.info().name == "my first workspace"
    assert mock_info.call_count == 1


def test_name(workspace, mock_info):
    assert workspace.name == "my first workspace"
    assert mock_info.call_count == 1


def test_bases(workspace, mock_info):
    bases = workspace.bases()
    assert len(bases) == 2
    assert bases[0].id == "appLkNDICXNqxSDhG"
    assert bases[1].id == "appSW9R5uCNmRmfl6"
    assert mock_info.call_count == 1
