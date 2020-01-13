from collections import defaultdict
from decimal import Decimal

import pydash
from typing import Dict, List, NewType, Tuple

from .models import CoffeeShop, Opinion, Person, WeightedCoffeeShop

CoffeeShopRatings = NewType('CoffeeShopRatings', Tuple[CoffeeShop, List[int]])


def calculate_average_ratings(persons: List[Person]) -> List[WeightedCoffeeShop]:
    return pydash.flow(
        _get_opinions,
        _map_ratings,
        pydash.partial(_calculate_average_ratings, persons)
    )(persons)


def _calculate_average_ratings(
    persons: List[Person],
    coffee_shops_ratings: List[CoffeeShopRatings]
) -> List[WeightedCoffeeShop]:
    return list(_calculate_average_rating(persons, cpr) for cpr in coffee_shops_ratings)


def _calculate_average_rating(persons: List[Person], coffee_shop_ratings: CoffeeShopRatings) -> WeightedCoffeeShop:
    average_rating = Decimal(sum(coffee_shop_ratings[1]) / len(coffee_shop_ratings[1]))
    return WeightedCoffeeShop(
        coffee_shop=coffee_shop_ratings[0],
        persons=persons,
        average_rating=average_rating
    )


def _get_opinions(persons: List[Person]) -> List[Opinion]:
    opinions: List[Opinion] = []
    for person in persons:
        opinions += person.opinions
    return opinions


def _map_ratings(opinions: List[Opinion]) -> List[CoffeeShopRatings]:
    ratings_map: Dict[CoffeeShop, List[int]] = defaultdict(list)
    for opinion in opinions:
        ratings_map[opinion.coffee_shop] += [opinion.rating]
    return list(CoffeeShopRatings((coffee_shop, ratings)) for coffee_shop, ratings in ratings_map.items())
