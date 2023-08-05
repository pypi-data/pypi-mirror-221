from dataclasses import dataclass, field
import datetime
import json
from pathlib import Path

DATA_FILE = Path.home() / ".config" / "ephemeral"


@dataclass
class Task:
    ts: int = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
    task: str | None = None
    dt: datetime.datetime = field(init=False)

    def __post_init__(self):
        self.dt = datetime.datetime.fromtimestamp(self.ts)

    @classmethod
    def load(self) -> "Task":
        if not DATA_FILE.is_file():
            return Task()
        data = json.loads(DATA_FILE.read_text())
        return Task(**data)

    @property
    def json(self) -> dict:
        return {"ts": self.ts, "task": self.task}

    def save(self) -> None:
        DATA_FILE.write_text(json.dumps(self.json))

    def read(self) -> "Task":
        try:
            data = json.loads(DATA_FILE.read_text())
            self.ts = data.get("ts", 0)
            self.task = data.get("task", "")
        except FileNotFoundError:
            self.ts = 0
        return self

    def update(self, new_task: str) -> None:
        self.task = new_task
        self.ts = int(datetime.datetime.now(datetime.timezone.utc).timestamp())
        self.save()

    def delete(self) -> None:
        DATA_FILE.write_text("{}")
        self.task = None
