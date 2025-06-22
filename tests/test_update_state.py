import json
from pathlib import Path
from unittest.mock import patch, Mock
from everdrive_version_notifier.update_state import StateUpdater


HTML_SAMPLE = """
<html>
<body>
<a href="?sort">Sort</a>
<a href="file1.zip">file1.zip</a>
<a href="file2.zip">file2.zip</a>
<a href="readme.txt">readme.txt</a>
</body>
</html>
"""


@patch("everdrive_version_notifier.update_state.requests.get")
def test_fetch_file_list_filters_out_question_links(mock_get):
    mock_response = Mock()
    mock_response.text = HTML_SAMPLE
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    updater = StateUpdater("http://example.com", Path("/dev/null"))
    result = updater.fetch_file_list()

    assert result == ["file1.zip", "file2.zip", "readme.txt"]


@patch("everdrive_version_notifier.update_state.requests.get")
def test_update_state_writes_expected_file(mock_get, tmp_path: Path):
    mock_response = Mock()
    mock_response.text = HTML_SAMPLE
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    state_file = tmp_path / "latest_files.json"
    updater = StateUpdater("http://example.com", state_file)
    updater.update_state()

    data = json.loads(state_file.read_text())
    assert data == ["file1.zip", "file2.zip", "readme.txt"]


@patch("everdrive_version_notifier.update_state.requests.get")
def test_main_updates_expected_file(mock_get, tmp_path: Path):
    from everdrive_version_notifier import update_state

    mock_response = Mock()
    mock_response.text = HTML_SAMPLE
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    # Patch __file__ so that main() writes to our tmp_path
    dummy_file = tmp_path / "dummy.py"
    dummy_file.touch()  # Make sure file exists

    with patch.object(update_state, "__file__", str(dummy_file)):
        update_state.main()

    state_file = tmp_path / "latest_files.json"
    assert state_file.exists()

    data = json.loads(state_file.read_text())
    assert data == ["file1.zip", "file2.zip", "readme.txt"]
