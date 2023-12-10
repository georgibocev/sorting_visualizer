import unittest
from draw_information import DrawInformation
from sorting_algorithms import BubbleSort, SelectionSort, InsertionSort


class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.draw_info = DrawInformation(800, 600, lst)

    def test_bubble_sort(self):
        """
        Test the BubbleSort algorithm.
        """
        bubble_sort = BubbleSort()
        generator = bubble_sort.sort(self.draw_info)
        for _ in generator:
            pass
        sorted_list = self.draw_info.lst.copy()

        self.assertEqual(sorted_list, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_bubble_sort_descending(self):
        """
        Test the BubbleSort algorithm in descending order.
        """
        bubble_sort = BubbleSort()
        generator = bubble_sort.sort(self.draw_info, ascending=False)
        for _ in generator:
            pass
        sorted_list = self.draw_info.lst.copy()

        self.assertEqual(sorted_list, [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1])

    def test_selection_sort(self):
        """
        Test the SelectionSort algorithm.
        """
        selection_sort = SelectionSort()
        generator = selection_sort.sort(self.draw_info)
        for _ in generator:
            pass
        sorted_list = self.draw_info.lst.copy()

        self.assertEqual(sorted_list, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_selection_sort_descending(self):
        """
        Test the SelectionSort algorithm in descending order.
        """
        selection_sort = SelectionSort()
        generator = selection_sort.sort(self.draw_info, ascending=False)
        for _ in generator:
            pass
        sorted_list = self.draw_info.lst.copy()

        self.assertEqual(sorted_list, [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1])

    def test_insertion_sort(self):
        """
        Test the InsertionSort algorithm.
        """
        insertion_sort = InsertionSort()
        generator = insertion_sort.sort(self.draw_info)
        for _ in generator:
            pass
        sorted_list = self.draw_info.lst.copy()

        self.assertEqual(sorted_list, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])

    def test_insertion_sort_descending(self):
        """
        Test the InsertionSort algorithm in descending order.
        """
        insertion_sort = InsertionSort()
        generator = insertion_sort.sort(self.draw_info, ascending=False)
        for _ in generator:
            pass
        sorted_list = self.draw_info.lst.copy()

        self.assertEqual(sorted_list, [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1])
