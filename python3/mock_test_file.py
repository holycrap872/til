from unittest.mock import patch, mock_open

@patch("builtins.open", new_callable=mock_open, read_data="data")
def test_patch(mock_file):
    assert open("path/to/open").read() == "data"
    mock_file.assert_called_with("path/to/open")
