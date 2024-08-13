from dataclasses import dataclass
from datetime import date

@dataclass
class Gospel:
    date: date
    text: str
    reference: str
