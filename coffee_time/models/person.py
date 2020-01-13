from dataclasses import dataclass
from typing import List

from .opinion import Opinion


@dataclass
class Person:
    name: str
    opinions: List[Opinion]
