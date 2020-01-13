import pydash
from typing import List

from .models import Person, WeightedCoffeeShop
from . import average_ratings


def get_highest_ranked_coffee_shop(persons: List[Person]) -> WeightedCoffeeShop:
    weighted_coffee_shops = average_ratings.calculate_average_ratings(persons)
    return pydash.sort(weighted_coffee_shops, compare_weighted_coffee_shops)[0]


def compare_weighted_coffee_shops(a: WeightedCoffeeShop, b: WeightedCoffeeShop) -> int:
    if a < b:
        return 1
    elif a > b:
        return -1
    else:
        return 0
