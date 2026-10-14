"""Unit tests for the altitude monitoring functions.

Run from the repository root: python -m unittest discover -s tests -v
"""
import unittest

from satellite_altitude_monitor import (
    altitude_deviation,
    altitude_extremes,
    average_altitude,
    build_report,
    classify_altitude,
    count_warnings,
    load_altitudes,
)


class AltitudeMonitorTests(unittest.TestCase):
    def setUp(self):
        self.values = [405, 402, 398, 395, 410, 387, 400]

    def test_load_data(self):
        self.assertEqual(load_altitudes(), self.values)

    def test_average(self):
        self.assertAlmostEqual(average_altitude(self.values), 399.5714285714)

    def test_classification_and_boundaries(self):
        self.assertEqual(classify_altitude(387), "LOW")
        self.assertEqual(classify_altitude(411), "HIGH")
        self.assertEqual(classify_altitude(390), "NORMAL")
        self.assertEqual(classify_altitude(410), "NORMAL")

    def test_warnings(self):
        self.assertEqual(count_warnings(self.values), 1)

    def test_extremes(self):
        self.assertEqual(altitude_extremes(self.values), (387, 410))

    def test_deviations(self):
        self.assertEqual(altitude_deviation([405, 387]), [5, -13])

    def test_report(self):
        report = build_report(self.values)
        self.assertIn("Average altitude: 399.57 km", report)
        self.assertIn("ATTENTION REQUIRED", report)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            average_altitude([])


if __name__ == "__main__":
    unittest.main()
