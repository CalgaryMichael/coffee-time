from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional

from .coffee_shop import CoffeeShop
from .person import Person


@dataclass
class WeightedCoffeeShop:
    coffee_shop: CoffeeShop
    persons: List[Person]
    average_rating: Decimal
    __rank_value: Optional[Decimal] = None

    def __eq__(self, other):
        return (
            self.coffee_shop == other.coffee_shop
            and self.persons == other.persons
            and self.average_rating == other.average_rating
            and self.calculate_rank_value() == other.calculate_rank_value()
        )

    def __gt__(self, other):
        return self.calculate_rank_value() > other.calculate_rank_value()

    def __lt__(self, other):
        return self.calculate_rank_value() < other.calculate_rank_value()

    def calculate_rank_value(self) -> Decimal:
        if self.__rank_value is None:
            rewards_bonus = Decimal('1.00')
            if self.coffee_shop.rewards is not None:
                rewards_bonus += self.coffee_shop.rewards
            weighted_distance = self.average_rating / self.coffee_shop.distance
            self.__rank_value = (self.average_rating * weighted_distance) * rewards_bonus
        return self.__rank_value
