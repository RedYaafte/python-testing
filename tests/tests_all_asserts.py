import unittest


class AllAssertsTests(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(1, 3 - 2)

    def test_assert_not_equal(self):
        self.assertNotEqual(2, 1)

    def test_assert_true(self):
        self.assertTrue(1 == 1)

    def test_assert_false(self):
        self.assertFalse(1 == 2)

    def test_assert_is(self):
        self.assertIs(None, None)

    def test_assert_is_not(self):
        self.assertIsNot(None, 6)

    def test_assert_is_none(self):
        self.assertIsNone(None)

    def test_assert_is_not_none(self):
        self.assertIsNotNone(7)

    def test_assert_in(self):
        self.assertIn(4, [1, 2, 3, 4])

    def test_assert_not_in(self):
        self.assertNotIn(4, [5, 6, 7])

    def test_assert_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0
