from unittest.mock import Mock
from everdrive_version_notifier.coordinator import EverdriveNotifier


def test_run_sends_message_and_updates_state():
    scraper = Mock()
    scraper.fetch_file_list.return_value = ["new1.zip", "new2.zip"]
    scraper.url = "https://example.com/"

    state_tracker = Mock()
    state_tracker.load.return_value = ["old1.zip"]
    notifier = Mock()

    coordinator = EverdriveNotifier(scraper, state_tracker, notifier)
    coordinator.run()

    expected_message = (
        "🆕 New EverDrive OS files:\n\n"
        "https://example.com/new1.zip\n"
        "https://example.com/new2.zip"
    )

    notifier.send_telegram_message.assert_called_once_with(expected_message)
    state_tracker.save.assert_called_once_with(["new1.zip", "new2.zip"])


def test_run_no_new_files_prints_message(capsys):
    scraper = Mock()
    scraper.fetch_file_list.return_value = ["same.zip"]
    scraper.url = "https://example.com/"

    state_tracker = Mock()
    state_tracker.load.return_value = ["same.zip"]
    notifier = Mock()

    coordinator = EverdriveNotifier(scraper, state_tracker, notifier)
    coordinator.run()

    notifier.send_telegram_message.assert_not_called()
    state_tracker.save.assert_not_called()

    out = capsys.readouterr().out
    assert "No new files found." in out
