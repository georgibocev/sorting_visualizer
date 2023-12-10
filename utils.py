import random
from sorting_algorithms import BubbleSort, SelectionSort, InsertionSort


def generate_starting_list(n, min_val, max_val):
    """
    Generates a random list of integers.

    Parameters:
    - n: int
        The length of the list.
    - min_val: int
        The minimum possible value for elements in the list.
    - max_val: int
        The maximum possible value for elements in the list.

    Returns:
    List[int]: A randomly generated list of integers.

    """
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def create_algorithm(algorithm_type):
    """
    Creates an instance of a sorting algorithm using the factory design pattern.

    Parameters:
    - algorithm_type: str
        The type of sorting algorithm to create.

    Returns:
    SortingAlgorithm: An instance of the specified sorting algorithm.

    Raises:
    ValueError: If the specified algorithm type is not supported.

    """
    algorithm_mapping = {
        "BubbleSort": BubbleSort,
        "SelectionSort": SelectionSort,
        "InsertionSort": InsertionSort,
    }
    algorithm_class = algorithm_mapping.get(algorithm_type)
    if algorithm_class:
        return algorithm_class()
    else:
        raise ValueError(f"Unsupported sorting algorithm: {algorithm_type}")
