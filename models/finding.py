from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Finding:
    finding_id: str
    title: str
    category: str
    severity: str
    raw_score: int
    description: str
    recommendation: str
    module: str
    status: str = "OPEN"
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    def to_dict(self):
        return asdict(self)

    def __str__(self):

        return (
            f"[{self.severity}] "
            f"{self.title} "
            f"({self.module})"
        )