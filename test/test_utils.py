import unittest
from unittest.mock import patch
from sorting_algorithms import BubbleSort, SelectionSort, InsertionSort
from utils import generate_starting_list, create_algorithm


class TestUtils(unittest.TestCase):
    """
    A test suite for the sorting functions.
    """

    @patch('random.randint', side_effect=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    def test_generate_starting_list(self, mock_randint):
        """
        Test the generate_starting_list function.

        Ensures that the function generates a list of the correct length with the expected values.

        """
        result = generate_starting_list(11, 1, 10)
        expected_result = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(result, expected_result)
        mock_randint.assert_called_with(1, 10)

    def test_create_algorithm_bubble_sort(self):
        """
        Test the create_algorithm function for BubbleSort.

        Ensures that the function creates an instance of the BubbleSort class.

        """
        result = create_algorithm("BubbleSort")
        self.assertIsInstance(result, BubbleSort)

    def test_create_algorithm_selection_sort(self):
        """
        Test the create_algorithm function for SelectionSort.

        Ensures that the function creates an instance of the SelectionSort class.

        """
        result = create_algorithm("SelectionSort")
        self.assertIsInstance(result, SelectionSort)

    def test_create_algorithm_insertion_sort(self):
        """
        Test the create_algorithm function for InsertionSort.

        Ensures that the function creates an instance of the InsertionSort class.

        """
        result = create_algorithm("InsertionSort")
        self.assertIsInstance(result, InsertionSort)

    def test_create_algorithm_invalid_type(self):
        """
        Test the create_algorithm function with an invalid algorithm type.

        Ensures that the function raises a ValueError for an unsupported algorithm type.

        """
        with self.assertRaises(ValueError):
            create_algorithm("InvalidSortAlgorithm")


if __name__ == '__main__':
    unittest.main()
