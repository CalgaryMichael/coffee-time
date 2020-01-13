from decimal import Decimal

from coffee_time import rankings as under_test
from coffee_time.models import WeightedCoffeeShop

from . import data, utils


def test_get_highest_ranked_coffee_shop(monkeypatch):
    # 8.80
    weighted_1 = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_1,
        persons=data.PERSONS,
        average_rating=Decimal('2.00')
    )
    # 10.02
    weighted_2 = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_2,
        persons=data.PERSONS,
        average_rating=Decimal('2.33')
    )
    # 7.97
    weighted_3 = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_3,
        persons=data.PERSONS,
        average_rating=Decimal('1.67')
    )
    monkeypatch.setattr(
        under_test.average_ratings,
        'calculate_average_ratings',
        lambda x: [weighted_1, weighted_2, weighted_3]
    )
    expected = weighted_2
    actual = under_test.get_highest_ranked_coffee_shop(data.PERSONS)
    assert utils.normalize_weighted_coffee_shop(actual) == expected
