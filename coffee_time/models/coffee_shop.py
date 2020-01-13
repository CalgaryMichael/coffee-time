from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CoffeeShop:
    name: str
    location: str
    distance: Decimal  # in mi
    rewards: Decimal   # ratio of drink purchases to free drinks

    def __hash__(self):
        return hash(self.location)
