from unittest.mock import MagicMock


def external_service():
    return "real data"


def test_mocking():
    mock_service = MagicMock(return_value="mock data")
    assert mock_service() == "mock data"
