import pytest
from unittest.mock import patch, Mock
from everdrive_version_notifier import run_notifier


@patch("everdrive_version_notifier.run_notifier.EverdriveNotifier")
@patch("everdrive_version_notifier.run_notifier.TelegramNotifier")
@patch("everdrive_version_notifier.run_notifier.FileStateTracker")
@patch("everdrive_version_notifier.run_notifier.EverdriveScraper")
def test_main_runs_successfully(
    mock_scraper, mock_state_tracker, mock_notifier, mock_coordinator
):
    os.environ["TELEGRAM_BOT_TOKEN"] = "test_token"
    os.environ["TELEGRAM_CHAT_ID"] = "test_chat"
    mock_instance = Mock()
    mock_coordinator.return_value = mock_instance

    run_notifier.main()

    mock_scraper.assert_called_once()
    mock_state_tracker.assert_called_once()
    mock_notifier.assert_called_once()
    mock_coordinator.assert_called_once()
    mock_instance.run.assert_called_once()


def test_main_missing_env_vars(monkeypatch):
    monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)
    monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)

    with pytest.raises(EnvironmentError) as excinfo:
        run_notifier.main()

    assert "Missing required environment variables" in str(excinfo.value)
