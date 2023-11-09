#!/usr/bin/env python3
"""ladder_problem.py"""

#Entirely used Dave's Code

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize  # type: ignore
from matplotlib.ticker import AutoMinorLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from scipy.optimize import OptimizeResult  # type: ignore
    from numpy.typing import NDArray


def length(theta: NDArray[np.float_]) -> NDArray[np.float_]:
    """Calculate the length of the ladder at different angles"""
    return 2 / np.sin(theta) + 1 / np.cos(theta)


def plot(ax: Axes) -> None:
    # Don't include the start or end points as they cause division by zero
    # in either the first or second term of the sum for length
    theta: NDArray[np.float_] = np.linspace(0, np.pi / 2, 100, dtype=np.float_)[1:-2]
    ladder: NDArray[np.float_] = length(theta)

    #Plot the ladder length as a function of angle
    ax.plot(theta, ladder)

    # Find point where ladder length is CONSTANT
    # This means the first derivative of length() is zero at an extrema point
    # In this case that extrema is global minimum of length()
    res: OptimizeResult = scipy.optimize.minimize(length, np.pi / 4)  # type: ignore

    # The resilt.x is an array, and we only want the first element
    c_theta: float = res.x[0]  # type: ignore
    c_length: float = float(length(np.array(c_theta)))  # type: ignore

    #Set the title of the plot with the maximum length
    ax.set_title(f"Max Length = {c_length:.4f} m")

    #Mark the point of maximum length on the plot
    ax.plot(c_theta, c_length, color="green", marker="o")
    ax.axhline(c_length, color="gray", linestyle="--")
    ax.vlines(x=c_theta, ymin=0, ymax=c_length, color="red")

    #Set the labels for the x and y axes
    ax.set_xlabel(r"$/theta$ (radians)")
    ax.set_ylabel("Length (m)")

    #Add minor ticks to both x and y axes
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    #Set the y-axis limits
    ax.set_ylim(0, 25)


def main() -> None:
    """Create a new figure and plot the ladder length"""
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
