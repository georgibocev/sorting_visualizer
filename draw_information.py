import pygame
import math
pygame.init()


class DrawInformation:
    """
    Class representing information for sorting algorithm visualization.
    """
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (74, 222, 222),
        (28, 167, 236),
        (31, 47, 152)
    ]

    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        """
        Initializes a DrawInformation instance.

        Parameters:
        - width: int
            Width of the window.
        - height: int
            Height of the window.
        - lst: List[int]
            List of integers to be visualized.
        """
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    def set_list(self, lst):
        """
        Sets the list to be visualized and calculates related parameters.

        Parameters:
            - lst: List[int]
                List of integers to be visualized.

        Returns:
        None
        """
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.__width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

    def draw_list(self, color_positions={}, clear_bg=False):
        """
        Draws the current state of the list in the window.

        Parameters:
        - color_positions: Dict[int, Tuple[int, int, int]]
            Dictionary specifying colors for specific positions in the list.
        - clear_bg: bool
            Indicates whether to clear the background.

        Returns:
        None
        """
        if clear_bg:
            clear_rect = (self.SIDE_PAD // 2, self.TOP_PAD,
                          self.__width - self.SIDE_PAD, self.height - self.TOP_PAD)
            pygame.draw.rect(self.window, self.BACKGROUND_COLOR, clear_rect)

        for i, val in enumerate(self.lst):
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height

            color = self.GRADIENTS[i % 3]

            if i in color_positions:
                color = color_positions[i]

            pygame.draw.rect(self.window, color, (x, y, self.block_width, self.height))

        if clear_bg:
            pygame.display.update()
