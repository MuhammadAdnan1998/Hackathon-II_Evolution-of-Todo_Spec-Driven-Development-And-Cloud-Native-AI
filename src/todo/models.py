from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Todo:
    id: int
    title: str
    is_completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
