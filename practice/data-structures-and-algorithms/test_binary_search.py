# run this normally
import unittest
import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_locate_card_binary(self):
        with self.assertRaises(ValueError, msg = "cards is not list or tuple"):
            binary_search.locate_card_binary(3, 0)

        self.assertEqual(binary_search.locate_card_binary([13, 11, 10, 7, 4, 3, 1, 0], 1), 6, msg = "query is not an end point")

        self.assertEqual(binary_search.locate_card_binary([4, 2, 1, -1], 4), 0, msg = "query is first element")

        self.assertEqual(binary_search.locate_card_binary([3, -1, -9, -127], -127), 3, msg = "query is last element")

        self.assertEqual(binary_search.locate_card_binary([6], 6), 0, msg = "cards contains one element")

        self.assertEqual(binary_search.locate_card_binary([9, 7, 5, 2, -9], 4), -1, msg = "query not in cards")

        self.assertEqual(binary_search.locate_card_binary([], 22), -1, msg = "cards is empty")

        self.assertEqual(binary_search.locate_card_binary([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 3), 7, msg = "repeating elemements in cards")

        self.assertEqual(binary_search.locate_card_binary([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 6), 2, msg = "cards has multiple instances of query")
        
        self.assertEqual(binary_search.locate_card_binary([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2], -2), 18, msg = "multiple instances (I)")

        self.assertEqual(binary_search.locate_card_binary([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2], -1), 12, msg = "multiple instances (II)")
        
        self.assertEqual(binary_search.locate_card_binary([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2], 0), 6, msg = "multiple instances (III)")

        self.assertEqual(binary_search.locate_card_binary([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2], 1), 0, msg = "multiple instances (IV)")

if __name__ == '__main__':
    unittest.main()