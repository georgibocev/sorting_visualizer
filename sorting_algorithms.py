from abc import ABC, abstractmethod


class SortingAlgorithm(ABC):
    """
    Abstract base class for sorting algorithms.
    """
    @abstractmethod
    def sort(self, draw_info, ascending=True):
        """
        Abstract method to perform sorting.

        Parameters:
        - draw_info: DrawInformation
            Object containing information for visualization.
        - ascending: bool, optional
            Indicates whether to sort in ascending or descending order.

        Returns:
        None
        """
        pass


class BubbleSort(SortingAlgorithm):
    """
    Class representing the Bubble Sort algorithm.
    """
    def sort(self, draw_info, ascending=True):
        """
        Performs Bubble Sort algorithm and visualizes the process.

        Parameters:
        - draw_info: DrawInformation
            Object containing information for visualization.
        - ascending: bool, optional
            Indicates whether to sort in ascending or descending order.

        Yields:
        True for each step of the sorting process.

        Returns:
        List[int]
            Sorted list.
        """
        lst = draw_info.lst

        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                num1 = lst[j]
                num2 = lst[j + 1]

                if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    draw_info.draw_list({j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                    yield True

        return lst


class SelectionSort(SortingAlgorithm):
    """
    Class representing the Selection Sort algorithm.
    """
    def sort(self, draw_info, ascending=True):
        """
        Performs Selection Sort algorithm and visualizes the process.

        Parameters:
        - draw_info: DrawInformation
            Object containing information for visualization.
        - ascending: bool, optional
            Indicates whether to sort in ascending or descending order.

        Yields:
        True for each step of the sorting process.

        Returns:
        List[int]
            Sorted list.
        """
        lst = draw_info.lst

        for i in range(len(lst)):
            min_index = i

            for j in range(i + 1, len(lst)):
                if (lst[j] < lst[min_index] and ascending) or (lst[j] > lst[min_index] and not ascending):
                    min_index = j

            lst[i], lst[min_index] = lst[min_index], lst[i]
            draw_info.draw_list({i: draw_info.GREEN, min_index: draw_info.RED}, True)
            yield True

        return lst


class InsertionSort(SortingAlgorithm):
    """
    Class representing the Insertion Sort algorithm.
    """

    def sort(self, draw_info, ascending=True):
        """
        Performs Insertion Sort algorithm and visualizes the process.

        Parameters:
        - draw_info: DrawInformation
            Object containing information for visualization.
        - ascending: bool, optional
            Indicates whether to sort in ascending or descending order.

        Yields:
        True for each step of the sorting process.

        Returns:
        List[int]
            Sorted list.
        """
        lst = draw_info.lst

        for i in range(1, len(lst)):
            current = lst[i]

            while True:
                ascending_sort = i > 0 and lst[i - 1] > current and ascending
                descending_sort = i > 0 and lst[i - 1] < current and not ascending

                if not ascending_sort and not descending_sort:
                    break

                lst[i] = lst[i - 1]
                i = i - 1
                lst[i] = current
                draw_info.draw_list({i - 1: draw_info.GREEN, i: draw_info.RED}, True)
                yield True

        return lst
