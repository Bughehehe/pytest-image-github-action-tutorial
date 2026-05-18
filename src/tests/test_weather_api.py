import pytest_tutorial.main as main

def test_get_weather_api(mocker):
    # Mock requests.get
    mock_get = mocker.patch("pytest_tutorial.main.requests.get")

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

    # Call function
    result = main.get_weather_api("Dubai")

    assert result == {"temperature": 25, "condition": "Sunny"}
    mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai", timeout=5)