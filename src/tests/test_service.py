from pytest_tutorial import service as service


def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=service.APIClient)

    mock_api_client.get_user_data.return_value = {"id": 1, "name": "Alice"}

    serv = service.UserService(mock_api_client)

    result = serv.get_username(1)

    assert result == "ALICE"
    mock_api_client.get_user_data.assert_called_once_with(1)
