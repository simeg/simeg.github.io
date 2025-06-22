import json
from pathlib import Path
import pytest
from everdrive_version_notifier.state import FileStateTracker


def test_save_and_load_state(tmp_path: Path):
    tracker = FileStateTracker(tmp_path / "state.json")
    data = ["file1.zip", "file2.zip"]
    tracker.save(data)
    assert tracker.load() == data


def test_load_returns_empty_when_file_missing(tmp_path: Path):
    tracker = FileStateTracker(tmp_path / "missing.json")
    assert tracker.load() == []


def test_save_overwrites_existing_file(tmp_path: Path):
    path = tmp_path / "state.json"
    path.write_text(json.dumps(["old.zip"]))
    tracker = FileStateTracker(path)
    new_data = ["new.zip"]
    tracker.save(new_data)
    assert json.loads(path.read_text()) == new_data


def test_load_reads_valid_json(tmp_path: Path):
    expected = ["one.zip", "two.zip"]
    path = tmp_path / "state.json"
    path.write_text(json.dumps(expected))
    tracker = FileStateTracker(path)
    assert tracker.load() == expected
