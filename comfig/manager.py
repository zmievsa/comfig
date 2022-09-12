import json
from typing import Any, List
from pathlib import Path

USER_HOME = Path.home()


class Comfig(dict):
    def __init__(self, filename: str):
        super().__init__()
        self.user = Path(USER_HOME, ".config", filename)
        self.user.parent.mkdir(exist_ok=True)
        if self.user.exists():
            super().update(json.loads(self.user.read_text()))
        self.local = Path.cwd() / filename

    def save(self, file: Path) -> None:
        file.write_text(str(self))

    def __str__(self):
        return json.dumps(self, ensure_ascii=False, indent=2)
