from decimal import Decimal

from coffee_time import calculations as under_test
from coffee_time.models import WeightedCoffeeShop

from . import data, utils


def test_calculate_average_ratings():
    expected = [
        WeightedCoffeeShop(
            coffee_shop=data.COFFEE_SHOP_1,
            persons=data.PERSONS,
            average_rating=Decimal('1.67')
        ),
        WeightedCoffeeShop(
            coffee_shop=data.COFFEE_SHOP_2,
            persons=data.PERSONS,
            average_rating=Decimal('2.00')
        ),
        WeightedCoffeeShop(
            coffee_shop=data.COFFEE_SHOP_3,
            persons=data.PERSONS,
            average_rating=Decimal('2.33')
        ),
    ]
    actual = under_test.calculate_average_ratings(data.PERSONS)
    assert utils.normalize_weighted_coffee_shops(actual) == expected


def test__map_ratings():
    opinions = data.PERSON_1_OPINIONS + data.PERSON_2_OPINIONS + data.PERSON_3_OPINIONS
    expected = [
        (data.COFFEE_SHOP_1, [
            data.PERSON_1_OPINIONS[0].rating,
            data.PERSON_2_OPINIONS[0].rating,
            data.PERSON_3_OPINIONS[0].rating
        ]),
        (data.COFFEE_SHOP_2, [
            data.PERSON_1_OPINIONS[1].rating,
            data.PERSON_2_OPINIONS[1].rating,
            data.PERSON_3_OPINIONS[1].rating
        ]),
        (data.COFFEE_SHOP_3, [
            data.PERSON_1_OPINIONS[2].rating,
            data.PERSON_2_OPINIONS[2].rating,
            data.PERSON_3_OPINIONS[2].rating
        ])
    ]
    actual = under_test._map_ratings(opinions)
    assert actual == expected


def test__get_opinions():
    expected = data.PERSON_1_OPINIONS + data.PERSON_2_OPINIONS + data.PERSON_3_OPINIONS
    actual = under_test._get_opinions(data.PERSONS)
    assert actual == expected
