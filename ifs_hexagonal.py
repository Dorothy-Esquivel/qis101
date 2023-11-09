#!/usr/bin/env python3
"""ifs_hexagonal.py"""

# Used Dave's code

from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem
from pygame import Color
import numpy as np

ifs = IteratedFunctionSystem()


def plot_ifs(ss: SimpleScreen) -> None:
    # Set the number of iterations
    iterations = 200_000
    x: float = 0.0
    y: float = 0.0
    clr: Color

    # Iterate (but don't draw) to let IFS reach its stable orbit
    for _ in range(100):
        x, y, clr = ifs.transform_point(x, y)

    # Now draw each pixel in the stable orbit
    for _ in range(iterations):
        x, y, clr = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, clr)


def main() -> None:
    # Set the base frame of the IFS
    ifs.set_base_frame(0, 0, 30, 30)

    # Calculate the height of the hexagon
    h = 5 * np.sqrt(3)
    p: float = 1 / 6

    # Define the mappings for the hexagon
    # COD
    ifs.add_mapping(25, 15, 15, 15, 20, 15 + h, Color(255, 0, 0), p)  # Red
    # DOE
    ifs.add_mapping(20, 15 + h, 15, 15, 10, 15 + h, Color(0, 255, 0), p)  # Green
    # EOF
    ifs.add_mapping(10, 15 + h, 15, 15, 5, 15, Color(0, 0, 255), p)  # Blue
    # FOA
    ifs.add_mapping(5, 15, 15, 15, 10, 15 - h, Color(255, 255, 0), p)  # Yellow
    # AOB
    ifs.add_mapping(10, 15 - h, 15, 15, 20, 15 - h, Color(255, 0, 255), p)  # Magneta
    # BOC
    ifs.add_mapping(20, 15 - h, 15, 15, 25, 15, Color(0, 255, 255), p)  # Cyan

    ifs.generate_transforms()

    # Create the SimpleScreen object
    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),  # Define the world coordinates
        screen_size=(900, 900),  # Define the screen size in pixels
        draw_function=plot_ifs,  # Set the function to draw the IFS
        title="IFS Hexagonal",  # Set the title of the screen
    )
    ss.show()


if __name__ == "__main__":
    main()
