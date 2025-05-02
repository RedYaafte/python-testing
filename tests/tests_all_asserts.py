import unittest


SERVER = "server_a"


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

    @unittest.skip("Trabajo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "chao")

    @unittest.skipIf(
        SERVER == "server_a", "No se encuentra en el servidor adecuado a ejecutar."
    )
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 101)
