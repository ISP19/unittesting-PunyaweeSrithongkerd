import unittest
from listutil import unique


class UniqueTest(unittest.TestCase):
    """Test for function Unique."""

    def test_empty_list_test(self):
        """"Test the empty list
        :return empty list
        """
        self.assertEqual([], unique([]))

    def test_single_item_test(self):
        """"Test single item list."""
        self.assertEqual(['Dog'], unique(['Dog']))
        self.assertEqual([1], unique([1]))

    def test_one_item_many_times(self):
        """Test one item many times."""
        self.assertEqual(['Dog'], unique(['Dog', 'Dog', 'Dog']))
        self.assertEqual([1], unique([1, 1, 1, 1]))

    def test_two_items_many_times_many_orders(self):
        """Test 2 items, many times, many orders."""
        self.assertEqual(['Dog',[1],1], unique(['Dog', 'Dog', [1], 'Dog', 1]))
        self.assertEqual([1, [2], 'C'], unique([1, 1, 1, 1,[2],'C']))

    def test_argument_not__list(self):
        """"throws exception"""
        with self.assertRaises(TypeError):
            unique(1)
        with self.assertRaises(TypeError):
            unique('c')
