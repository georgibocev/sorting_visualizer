import unittest
from draw_information import DrawInformation

class TestDrawInformation(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment with a DrawInformation instance.

        Returns:
        None
        """
        lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.draw_info = DrawInformation(800, 600, lst)

    def test_initialization(self):
        """
        Test the initialization of the DrawInformation instance.

        This test checks whether the instance is correctly initialized with the provided parameters.

        Returns:
        None
        """
        self.assertEqual(self.draw_info.width, 800)
        self.assertEqual(self.draw_info.height, 600)
        self.assertIsNotNone(self.draw_info.window)
        self.assertEqual(self.draw_info.lst, [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        self.assertEqual(self.draw_info.min_val, 1)
        self.assertEqual(self.draw_info.max_val, 9)
        self.assertIsNotNone(self.draw_info.block_width)
        self.assertIsNotNone(self.draw_info.block_height)
        self.assertIsNotNone(self.draw_info.start_x)

    def test_set_list(self):
        """
        Test the set_list method of the DrawInformation class.

        This test checks whether the set_list method correctly updates the list and related parameters.

        Returns:
        None
        """
        new_list = [8, 4, 6, 2, 7, 1, 3, 5]
        self.draw_info.set_list(new_list)
        self.assertEqual(self.draw_info.lst, new_list)
        self.assertEqual(self.draw_info.min_val, 1)
        self.assertEqual(self.draw_info.max_val, 8)

    def test_draw_list(self):
        """
        Test the draw_list method of the DrawInformation class.

        This test checks whether the draw_list method correctly updates the window based on the provided parameters.

        Cases:
        - Test when the color_positions dictionary is empty and clear_bg is False.
        - Test when the color_positions dictionary contains valid positions and clear_bg is False.
        - Test when clear_bg is True.

        Returns:
        None
        """
        # Case 1: Test when the color_positions dictionary is empty and clear_bg is False.
        self.draw_info.draw_list()
        # Add assertions based on the expected behavior of the draw_list method in this case.

        # Case 2: Test when the color_positions dictionary contains valid positions and clear_bg is False.
        color_positions = {0: (255, 0, 0), 1: (0, 255, 0)}
        self.draw_info.draw_list(color_positions)
        # Add assertions based on the expected behavior of the draw_list method in this case.

        # Case 3: Test when clear_bg is True.
        self.draw_info.draw_list(clear_bg=True)



