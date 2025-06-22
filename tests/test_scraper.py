import pytest
import requests
from unittest.mock import patch, Mock
from everdrive_version_notifier.scraper import EverdriveScraper


HTML_SAMPLE = """
<html>
<body>
<a href="?C=N;O=D">Sort</a>
<a href="GBC-OS-v1.00.zip">GBC-OS-v1.00.zip</a>
<a href="GBC-OS-v1.01.zip">GBC-OS-v1.01.zip</a>
<a href="changelist.txt">changelist.txt</a>
<a href="folder/">folder/</a>
</body>
</html>
"""


@patch("everdrive_version_notifier.scraper.requests.get")
def test_fetch_file_list_filters_zip(mock_get):
    mock_response = Mock()
    mock_response.text = HTML_SAMPLE
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    scraper = EverdriveScraper("http://example.com")
    files = scraper.fetch_file_list()

    assert files == ["GBC-OS-v1.00.zip", "GBC-OS-v1.01.zip"]


@patch("everdrive_version_notifier.scraper.requests.get")
def test_fetch_file_list_raises_on_http_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("403 Forbidden")
    mock_get.return_value = mock_response

    scraper = EverdriveScraper("http://example.com")

    with pytest.raises(requests.HTTPError):
        scraper.fetch_file_list()
