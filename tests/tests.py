import unittest
from src.ans import get_nested_value


class TestGetNestedValue(unittest.TestCase):
    def test_get_nested_value(self):
        nested_dict = {'a': {'b': {'c': 1}}}
        keys = ['a', 'b', 'c']
        self.assertEqual(get_nested_value(nested_dict, keys), 1)

    def test_key_not_found(self):
        nested_dict = {'a': {'b': 2}}
        keys = ['a', 'c']
        self.assertIsNone(get_nested_value(nested_dict, keys))

    def test_empty_keys(self):
        nested_dict = {'a': 1}
        self.assertIsNone(get_nested_value(nested_dict, []))

    def test_empty_dict(self):
        self.assertIsNone(get_nested_value({}, ['a']))


if __name__ == '__main__':
    unittest.main()
