​from random import randint, sample, uniform
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(num_items=30):
    list = []
    for i in range(0, num_items):
        rand_id = randint(1000000, 9999999)
        rand_price = randint(5, 100)
        rand_weight = randint(5, 100)
        rand_flam = random.uniform(0, 2.5)
        name = f'{choice(ADJECTIVES)} {choice(NOUNS)}'
        a = Product(name, identifier=rand_id, price=rand_price,
                    weight=rand_weight, flammability=rand_flam)
        list.append(a.attributes)
    return list


def inventory_report(products: list) -> None:
    names = set()
    prices = []
    weights = []
    flammabilities = []
    for product in products:
        names |= {product.name}
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    uniques = len(names)
    avg_price = sum(prices)/len(prices)
    avg_weight = sum(weights)/len(weights)
    avg_flammability = sum(flammabilities)/len(flammabilities)
    print(f"""
ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: {uniques}
Average price: ${avg_price:,.02f}
Average weight: {avg_weight}
Average flammability: {avg_flammability}
""")


if __name__ == '__main__':
    inventory_report(generate_products())