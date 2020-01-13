from decimal import Decimal
from typing import List

from coffee_time.models import WeightedCoffeeShop

TWO_PLACES = Decimal('0.01')


def normalize_weighted_coffee_shops(weighted_coffee_shops: List[WeightedCoffeeShop]) -> List[WeightedCoffeeShop]:
    """Returns a list of WeightedCoffeeShop that have a quantized average rating"""
    normalized = weighted_coffee_shops[:]
    for weighted_coffee_shop in normalized:
        weighted_coffee_shop.average_rating = weighted_coffee_shop.average_rating.quantize(TWO_PLACES)
    return normalized
