from timur import Film
import unittest

class testFilm(unittest.TestCase):

    def setUp(self):
        self.film_1 = Film("aaaaa", "Aaaa Bbbb", 5, 1000000.0)

    def test_get_cash(self):
        self.assertEqual(self.film_1.get_cash(), 1000000)

    def test_get_director(self):
        self.assertEqual(self.film_1.get_director(), "Aaaa Bbbb")

    def test_set_name(self):
        name_2: str = 'aaaaa'
        self.film_1.set_name(name_2)
        self.assertEqual(self.film_1.name, name_2)

    def test_get_new_cash(self):
        self.film_1.set_new_cash(2000)
        self.assertEqual(self.film_1.cash, 2000)


if __name__ == '__main__':
    unittest.main()

