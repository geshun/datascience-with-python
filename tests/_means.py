import unittest
from utils.means import product
from utils.means import arithmetic_mean
from utils.means import geometric_mean
from utils.means import harmonic_mean
from utils.means import Means


class TestMeans(unittest.TestCase):

    def test_product(self):
        self.assertEqual(product([1, 2, 3, 4]), 24)
        self.assertEqual(product((1, 2, 3, 4)), 24)
        self.assertEqual(product([0, 2, 3, 4]), 0)
        self.assertEqual(product([2.5, 3.5]), 8.75)
        with self.assertRaises(ValueError):
            product([])

    def test_arithmetic_mean(self):
        self.assertEqual(arithmetic_mean([1, 2, 3, 4]), 2.5)
        self.assertEqual(arithmetic_mean((1, 2, 3, 4)), 2.5)
        self.assertEqual(arithmetic_mean([2.5, 3.5]), 3.0)
        with self.assertRaises(ValueError):
            arithmetic_mean([])

    def test_geometric_mean(self):
        self.assertAlmostEqual(geometric_mean(
            [1, 2, 3, 4]), 2.213363839400643, places=7)
        self.assertAlmostEqual(geometric_mean(
            (1, 2, 3, 4)), 2.213363839400643, places=7)
        self.assertAlmostEqual(geometric_mean(
            [2.5, 3.5]), 2.958039891549808, places=7)
        with self.assertRaises(ValueError):
            geometric_mean([])
        with self.assertRaises(ValueError):
            geometric_mean([0, 2, 3, 4])
        with self.assertRaises(ValueError):
            geometric_mean([-1, 2, 3, 4])

    def test_harmonic_mean(self):
        self.assertAlmostEqual(harmonic_mean([1, 2, 3, 4]), 1.92, places=2)
        self.assertAlmostEqual(harmonic_mean((1, 2, 3, 4)), 1.92, places=2)
        self.assertAlmostEqual(harmonic_mean(
            [2.5, 3.5]), 2.9166666666666665, places=7)
        with self.assertRaises(ValueError):
            harmonic_mean([])
        with self.assertRaises(ValueError):
            harmonic_mean([0, 2, 3, 4])
        with self.assertRaises(ValueError):
            harmonic_mean([-1, 2, 3, 4])

    def test_means_class(self):
        means = Means([1, 2, 3, 4])
        self.assertEqual(means.product(), 24)
        self.assertEqual(means.arithmetic_mean(), 2.5)
        self.assertAlmostEqual(means.geometric_mean(),
                               2.213363839400643, places=7)
        self.assertAlmostEqual(means.harmonic_mean(), 1.92, places=2)

        means = Means([2.5, 3.5])
        self.assertEqual(means.product(), 8.75)
        self.assertEqual(means.arithmetic_mean(), 3.0)
        self.assertAlmostEqual(means.geometric_mean(),
                               2.958039891549808, places=7)
        self.assertAlmostEqual(means.harmonic_mean(),
                               2.9166666666666665, places=7)

        with self.assertRaises(ValueError):
            Means([])

        with self.assertRaises(ValueError):
            Means([1, 2, 0, 4]).geometric_mean()

        with self.assertRaises(ValueError):
            Means([1, 2, 0, 4]).harmonic_mean()


if __name__ == '__main__':
    unittest.main()

# run test from the terminal: python -m unittest tests/_means.py
