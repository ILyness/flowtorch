"""Smoke tests for the installed package."""

import unittest

import flowtorch


class PackageTests(unittest.TestCase):
    def test_package_has_version(self) -> None:
        self.assertEqual(flowtorch.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
