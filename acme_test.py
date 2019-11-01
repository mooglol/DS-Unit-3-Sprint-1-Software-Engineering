import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
​
​
class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
​
​
if __name__ == '__main__':
    unittest.main()


import unittest
from acme import Product
from acme_report import generate_products, adj_name, noun_name


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_explode(self):
        prod = Product('Test Explosive Product', weight=42, flammability=2.5)
        self.assertEqual(prod.explode(), '...BABOOM!!')

    def test_stealable(self):
        prod = Product('Test Theft Product', weight=42, price=1)
        self.assertEqual(prod.stealability(), 'Not so stealable...')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names_adj(self):
        products = generate_products()
        for i in range(0, len(products)):
            self.assertIn(products[i][1].split()[0], adj_name)

    def test_legal_names_noun(self):
        products = generate_products()
        for i in range(0, len(products)):
            self.assertIn(products[i][1].split()[1], noun_name)


if __name__ == '__main__':
    unittest.main()