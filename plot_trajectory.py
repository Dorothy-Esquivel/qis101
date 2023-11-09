#!/usr/bin/env python3
"""plot_trajectory.py"""

# Used Dave's code

from __future__ import annotations

import typing

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def fit_linear(x: NDArray[np.float_], y: NDArray[np.float_]) -> tuple[float, float]:
    """Fits a linear regression line to the data points (x, y) and returns the slope and intercept"""
    n: int = len(x)
    # Calcualte the slope using the least squares method
    m: float = float(n * np.sum(x * y) - np.sum(x) * np.sum(y))
    m /= float(n * np.sum(x**2) - np.sum(x) ** 2)
    # Calculate the intercept
    b: float = float(np.sum(y) - m * np.sum(x))
    b /= n
    return m, b


def plot(ax: Axes) -> None:
    """Plots the trajectory of secondary cosmic rays."""
    # Load data from a CSV file
    data_file: Path = Path(__file__).parent.joinpath("ray.csv")
    data = np.genfromtxt(data_file, delimiter=",")

    x = data[:, 0]  # time in nanoseconds
    y = data[:, 1]  # height in centimeters

    m: float
    b: float
    m, b = fit_linear(x, y)
    h = (np.abs(m) * 1e9 / 100) * (0.1743 / 1e3) / 1000  # Convert slope to kilometers
    c = 29.98  # speed of light in cm/ns

    # Print the slope with 4 digits after the decimal place
    print(f"Slope = {abs(m):.4f} cm/ns")
    # Print the velocity and origination height with 2 digits after the decimal place
    print(f"Velocity = {np.abs(m)/c:,.2f} c")
    print(f"Origination Height = {h:,.2f} km")

    # Plot the data points
    ax.scatter(x, y)
    # Plot the linear regression line
    ax.plot(x, m * x + b, color="red", linewidth=2)

    # Set the plot title, x-axis label, and y-axis label
    ax.set_title("Secondary Cosmic Ray Trajectory")
    ax.set_xlabel("time (ns)")
    ax.set_ylabel("height (cm)")
    ax.grid()  # Add gridlines to the plot


def main() -> None:
    """Main function to generate the plot."""
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
