from dataclasses import dataclass
from decimal import Decimal
from typing import List

from .coffee_shop import CoffeeShop
from .person import Person


@dataclass
class WeightedCoffeeShop:
    coffee_shop: CoffeeShop
    persons: List[Person]
    average_rating: Decimal
