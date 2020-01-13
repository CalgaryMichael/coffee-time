from decimal import Decimal

from typing import List

from coffee_time.models import WeightedCoffeeShop

TWO_PLACES = Decimal('0.01')


def normalize_weighted_coffee_shops(weighted_coffee_shops: List[WeightedCoffeeShop]) -> List[WeightedCoffeeShop]:
    """Returns a list of WeightedCoffeeShop that have a quantized average rating"""
    return list(normalize_weighted_coffee_shop(wcs) for wcs in weighted_coffee_shops)


def normalize_weighted_coffee_shop(original: WeightedCoffeeShop) -> WeightedCoffeeShop:
    """Returns a WeightedCoffeeShop that has a quantized average rating"""
    return WeightedCoffeeShop(
        coffee_shop=original.coffee_shop,
        persons=original.persons,
        average_rating=normalize_decimal(original.average_rating)
    )


def normalize_decimal(value: Decimal) -> Decimal:
    return value.quantize(TWO_PLACES)
