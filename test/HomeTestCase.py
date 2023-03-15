import unittest


class HomeTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

class BestTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(0, True)


if __name__ == '__main__':
    unittest.main()
