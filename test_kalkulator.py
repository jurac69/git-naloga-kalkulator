import unittest

from kalkulator import deli, odstej, sestej, zmnozi


class TestKalkulator(unittest.TestCase):
    def test_sestej(self):
        self.assertEqual(sestej(2, 3), 5)

    def test_odstej(self):
        self.assertEqual(odstej(5, 3), 2)

    def test_zmnozi(self):
        self.assertEqual(zmnozi(4, 3), 12)

    def test_deli(self):
        self.assertEqual(deli(10, 2), 5)

    def test_deli_z_nic(self):
        with self.assertRaises(ValueError):
            deli(1, 0)


if __name__ == "__main__":
    unittest.main()
