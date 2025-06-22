# EverDrive Version Notifier [![Check EverDrive Files](https://github.com/simeg/everdrive-version-notifier/actions/workflows/check_files.yml/badge.svg)](https://github.com/simeg/everdrive-version-notifier/actions/workflows/check_files.yml) [![codecov](https://codecov.io/gh/simeg/everdrive-version-notifier/branch/main/graph/badge.svg)](https://codecov.io/gh/simeg/everdrive-version-notifier)

This tool checks for new firmware files published to the [EverDrive GB X-Series OS directory](https://krikzz.com/pub/support/everdrive-gb/x-series/OS/) and notifies you via Telegram when new `.zip` files appear.

🔔 **You will get a Telegram message** with direct links to the new files if any are found. If nothing new is found, nothing happens.

---

## 🤔 Why This Exists

You're monitoring a firmware directory that rarely updates (maybe once a year). This project automates that process so you don't have to remember to check it manually.

Once set up, **it just runs once per week via GitHub Actions** and tells you only if something changed.

You’ll likely forget this tool even exists — and that’s by design.

---

## 📦 Project Structure

- `src/everdrive_version_notifier/`: main source code
- `tests/`: unit tests for everything
- `latest_files.json`: snapshot of the last known file state (checked into repo)
- `.github/workflows/check_files.yml`: GitHub Actions automation

---

## 🧠 What to Expect

Each week:
- The GitHub Action runs and loads the `latest_files.json` state
- It scrapes the EverDrive OS folder for new `.zip` files
- If it finds any that aren't in the state, it:
  - Sends you a Telegram message
  - Updates the `latest_files.json` file in memory (not committed)
- You'll get a PR or can run a manual `make update-state` to commit the new state

If no new files are found:
- It prints "No new files found." and does nothing else

---

## 🚀 Setup

1. Clone the repo
2. Create a `.env` file with:

   ```
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

3. Install dependencies:

   ```bash
   poetry install
   ```

4. Run the notifier locally (optional):

   ```bash
   make check
   ```

---

## 🛠️ Makefile Targets

| Target             | Description |
|--------------------|-------------|
| `make check`       | Run the full check (load, scrape, notify if new files) |
| `make update-state`| Manually update the `latest_files.json` snapshot to the current state of the EverDrive site |
| `make dry-run`     | Simulates a check without sending a Telegram message |
| `make test`        | Run all unit tests (includes linting first) |
| `make coverage`    | Run tests and print coverage report |
| `make watch`       | Watch for changes and re-run tests automatically |
| `make format`      | Format all Python code using `black` |
| `make lint`        | Run `black` in check-only mode (lint style enforcement) |

---

## 📎 Notes to Future Me

- The OS directory updates *very* rarely — expect 0–1 updates per year.
- If you ever change Telegram tokens or chat ID, update `.env` or GitHub Secrets accordingly.
- Don’t forget to run `make update-state` and commit `latest_files.json` when you receive an update message.

Enjoy the peace of mind ✌️
