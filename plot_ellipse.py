#!/usr/bin/env python3
"""plot_ellipse.py"""

from matplotlib.ticker import MultipleLocator
import numpy as np
import matplotlib.pyplot as plt

# Entirely used Dave's code


def plot(ax):  # type: ignore
    # Set the parameters for the ellipse.
    a = 100
    b = 50

    # Generates theta values from 0 to 2*pi
    theta = np.linspace(0, 2 * np.pi, 1000)
    # Calculates the radius for each theta value
    radius = a * b / np.sqrt((b * np.cos(theta)) ** 2 + (a * np.sin(theta)) ** 2)

    # Convert polar coordinates to Cartesian coordinates
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Plot the ellipse
    ax.plot(x, y)

    # Set the title of the plot
    ax.set_title(rf"$\frac{{x^2}}{{{a}^2}} + \frac{{y^2}}{{{b}^2}}= 1$")
    # Set the labels for x and y axes
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Add gridlines to the plot
    ax.grid()
    # Add horizontal and vertical lines at y=0 and x=0 respectively
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")

    # Set the major tick locators for x and y axes
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(10))

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect("equal")


def main() -> None:
    # Create a figure for the plot
    plt.figure(__file__)
    # Plot the ellipse on the axes
    plot(plt.axes())  # type: ignore
    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
