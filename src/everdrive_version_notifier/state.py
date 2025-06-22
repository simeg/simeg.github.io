import json
from pathlib import Path


class FileStateTracker:
    def __init__(self, state_file: Path):
        self.state_file = state_file

    def load(self) -> list[str]:
        if self.state_file.exists():
            return json.loads(self.state_file.read_text())
        return []

    def save(self, files: list[str]) -> None:
        self.state_file.write_text(json.dumps(files, indent=2))
