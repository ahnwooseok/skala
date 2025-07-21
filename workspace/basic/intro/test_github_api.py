# test_github_api.py
import pytest
from unittest.mock import patch, Mock
from github_api import get_github_user_info

# 정상적인 사용자 요청을 모의
@patch("github_api.requests.get")
def test_valid_user(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "login": "torvalds",
        "name": "Linus Torvalds",
    }
    mock_get.return_value = mock_response

    result = get_github_user_info("torvalds")
    assert result is not None
    assert result["login"] == "torvalds"

# 존재하지 않는 사용자 요청을 모의
@patch("github_api.requests.get")
def test_invalid_user(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = get_github_user_info("non_existing_user_xyz")
    assert result is None

# 네트워크 예외(mocked)
@patch("github_api.requests.get")
def test_network_error(mock_get):
    mock_get.side_effect = Exception("Network Error")

    result = get_github_user_info("any_user")
    assert result is None
