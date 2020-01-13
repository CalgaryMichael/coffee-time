from coffee_time.models import CoffeeShop, Opinion, Person


COFFEE_SHOP_1 = CoffeeShop(
    name='Coffee Shop #1',
    location='123 W Main St',
    distance=0.50,
    rewards=0.10
)

COFFEE_SHOP_2 = CoffeeShop(
    name='Coffee Shop #2',
    location='456 E Broadway St',
    distance=0.65,
    rewards=0.2
)

COFFEE_SHOP_3 = CoffeeShop(
    name='Coffee Shop #3',
    location='789 S 6th Ave',
    distance=0.15,
    rewards=None
)

PERSON_1_OPINIONS = [
    Opinion(
        coffee_shop=COFFEE_SHOP_1,
        rating=1
    ),
    Opinion(
        coffee_shop=COFFEE_SHOP_2,
        rating=2
    ),
    Opinion(
        coffee_shop=COFFEE_SHOP_3,
        rating=3
    ),
]

PERSON_2_OPINIONS = [
    Opinion(
        coffee_shop=COFFEE_SHOP_1,
        rating=2
    ),
    Opinion(
        coffee_shop=COFFEE_SHOP_2,
        rating=3
    ),
    Opinion(
        coffee_shop=COFFEE_SHOP_3,
        rating=1
    ),
]

PERSON_3_OPINIONS = [
    Opinion(
        coffee_shop=COFFEE_SHOP_1,
        rating=2
    ),
    Opinion(
        coffee_shop=COFFEE_SHOP_2,
        rating=1
    ),
    Opinion(
        coffee_shop=COFFEE_SHOP_3,
        rating=3
    ),
]

PERSON_1 = Person(
    name='Miles Davis',
    opinions=PERSON_1_OPINIONS
)

PERSON_2 = Person(
    name='John Coltrane',
    opinions=PERSON_2_OPINIONS
)

PERSON_3 = Person(
    name='Nina Simone',
    opinions=PERSON_3_OPINIONS
)

PERSONS = [
    PERSON_1,
    PERSON_2,
    PERSON_3
]
