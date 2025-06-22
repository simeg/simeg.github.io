from unittest.mock import patch, Mock
from everdrive_version_notifier.notifier import TelegramNotifier


def test_send_telegram_message_dry_run(capsys):
    notifier = TelegramNotifier("dummy_token", "dummy_chat_id", dry_run=True)
    test_message = "Dry run test message"
    notifier.send_telegram_message(test_message)

    out = capsys.readouterr().out
    assert "DRY RUN ENABLED" in out
    assert test_message in out


@patch("everdrive_version_notifier.notifier.requests.post")
def test_send_telegram_message_real(mock_post):
    mock_response = Mock()
    mock_response.raise_for_status = Mock()
    mock_post.return_value = mock_response

    token = "real_token"
    chat_id = "chat_id"
    message = "Real test message"
    notifier = TelegramNotifier(token, chat_id, dry_run=False)
    notifier.send_telegram_message(message)

    expected_url = f"https://api.telegram.org/bot{token}/sendMessage"
    expected_payload = {
        "chat_id": chat_id,
        "text": message,
        "disable_web_page_preview": True,
    }
    mock_post.assert_called_once_with(expected_url, json=expected_payload)
