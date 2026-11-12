
"""
NERTEX EDGE
Model Unit Tests
"""

import unittest

from src.edge.model import TinyLinearModel


class TestTinyLinearModel(unittest.TestCase):

    def setUp(self):
        self.model = TinyLinearModel(
            weights=[1.0, 1.0],
            bias=0.0
        )

    def test_positive_prediction(self):
        self.assertEqual(
            self.model.predict([2.0, 3.0]),
            1
        )

    def test_negative_prediction(self):
        self.assertEqual(
            self.model.predict([-2.0, -3.0]),
            0
        )

    def test_probability_range(self):
        probability = self.model.predict_proba([1.0, 2.0])

        self.assertGreaterEqual(probability, 0.0)
        self.assertLessEqual(probability, 1.0)

    def test_invalid_input_dimensions(self):
        with self.assertRaises(ValueError):
            self.model.predict([1.0])

    def test_empty_weights(self):
        with self.assertRaises(ValueError):
            TinyLinearModel([])


if __name__ == "__main__":
    unittest.main()
