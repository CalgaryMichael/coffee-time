from decimal import Decimal

from coffee_time.models import WeightedCoffeeShop

from . import data, utils


def test_calculate_rank_value__low_rating__low_distance__no_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_3,
        persons=data.PERSONS,
        average_rating=Decimal('1.67')
    )
    expected = Decimal('7.97')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__low_rating__med_distance__low_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_1,
        persons=data.PERSONS,
        average_rating=Decimal('1.67')
    )
    expected = Decimal('6.14')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__low_rating__high_distance__high_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_2,
        persons=data.PERSONS,
        average_rating=Decimal('1.67')
    )
    expected = Decimal('5.15')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__med_rating__low_distance__no_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_3,
        persons=data.PERSONS,
        average_rating=Decimal('2.00')
    )
    expected = Decimal('11.43')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__med_rating__med_distance__low_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_1,
        persons=data.PERSONS,
        average_rating=Decimal('2.00')
    )
    expected = Decimal('8.80')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__med_rating__high_distance__high_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_2,
        persons=data.PERSONS,
        average_rating=Decimal('2.00')
    )
    expected = Decimal('7.38')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__high_rating__low_distance__no_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_3,
        persons=data.PERSONS,
        average_rating=Decimal('2.33')
    )
    expected = Decimal('15.51')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__high_rating__med_distance__low_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_1,
        persons=data.PERSONS,
        average_rating=Decimal('2.33')
    )
    expected = Decimal('11.94')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected


def test_calculate_rank_value__high_rating__high_distance__high_rewards():
    under_test = WeightedCoffeeShop(
        coffee_shop=data.COFFEE_SHOP_2,
        persons=data.PERSONS,
        average_rating=Decimal('2.33')
    )
    expected = Decimal('10.02')
    actual = under_test.calculate_rank_value()
    assert utils.normalize_decimal(actual) == expected
