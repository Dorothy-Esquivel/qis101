#!/usr/bin/env python3
"""archimedes_spiral.py"""

# Used Dave's Code

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate  # type: ignore


def f(theta: float) -> float:
    """Function to calculate the value of f(theta) for the spiral equation."""
    return float(np.sqrt(theta**2 + 1))


def plot(ax: plt.Axes) -> None:
    """Plot the Archimedes Spiral"""
    # Generate theta values from 0 to 8*pi
    theta = np.linspace(0, 8 * np.pi, 1000)
    # Calculate x-coordinates for each theta
    x = theta * np.cos(theta)
    # Calculate y-coordinates for each theta
    y = theta * np.sin(theta)
    # Define colors based on theta values
    colors = theta

    # Plot the spiral with color variation in honor of Pride Month
    ax.scatter(x, y, c=colors, cmap="hsv")

    # Calculate the arc length using quad integration
    arc_length, _ = scipy.integrate.quad(f, 0, 8 * np.pi)  # type: ignore

    ax.set_title(
        (
            r"Archimedes Spiral $(r=\theta, \;0\leq\theta\leq 8\pi)$"
            f"\nArc Length = {arc_length:.4f}"
        )  # Set the title with sprial equation and arc length
    )

    # Set the x-axis label
    ax.set_xlabel("x")
    # Set the y-axis label
    ax.set_ylabel("y")

    # Draw a horizontal line at y=0
    ax.axhline(0, color="black")
    # Draw a vertical line at x=0
    ax.axvline(0, color="black")

    # Set the aspect ratio of the plot to equal
    ax.set_aspect("equal")


def main() -> None:
    """Main function to execute the program"""
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
