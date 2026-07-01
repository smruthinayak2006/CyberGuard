from dataclasses import dataclass
from datetime import datetime


@dataclass
class Finding:

    id: str

    title: str

    category: str

    severity: str

    raw_score: int

    description: str

    recommendation: str

    module: str

    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status: str = "OPEN"