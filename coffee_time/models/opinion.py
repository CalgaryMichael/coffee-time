from dataclasses import dataclass

from .coffee_shop import CoffeeShop


@dataclass
class Opinion:
    coffee_shop: CoffeeShop
    rating: int
