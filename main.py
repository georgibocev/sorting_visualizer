import pygame
from utils import generate_starting_list, create_algorithm
from draw_information import DrawInformation


def draw(draw_info, algo_name, ascending):
    """
    Draw the current state of the sorting algorithm visualization.

    Parameters:
    - draw_info: DrawInformation
       An instance of DrawInformation containing information about the visualization.
    - algo_name: str
        The name of the sorting algorithm being visualized.
    - ascending: bool
        Indicates whether the sorting is in ascending order.

    Returns:
    None
    """
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,
                                        draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width() / 2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1,
                                     draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 45))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 75))

    draw_info.draw_list()
    pygame.display.update()


def main():
    """
    Main function to run the sorting algorithm visualization.

    Parameters:
    None

    Returns:
    None
    """
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1200, 900, lst)
    sorting = False
    ascending = True

    sorting_algorithm = create_algorithm("BubbleSort")
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm.sort(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = create_algorithm("InsertionSort")
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = create_algorithm("BubbleSort")
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = create_algorithm("SelectionSort")
                sorting_algo_name = "Selection Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
