#!/usr/bin/env python3
"""werner_formula.py"""

# Used Dave's Code

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray

# Define the values of a and b
a: float = 0.8
b: float = 0.5


# Define the function y1, y2, y3, and y4
def y1(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(np.sin(a * x))


def y2(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(np.sin(b * x))


def y3(x: NDArray[np.float_]) -> NDArray[np.float_]:
    return np.array(y1(x) * y2(x))


def y4(x: NDArray[np.float_]) -> NDArray[np.float_]:
    # This is one of Werner's Formulas
    return np.array((np.cos((a - b) * x) - np.cos((a + b) * x)) / 2)


# Define the plot function
def plot(ax: Axes) -> None:
    r = 3
    x: NDArray[np.float_] = np.linspace(-r * np.pi, r * np.pi, 500)

    # Plot y1, y2, y3, and y4
    ax.plot(x, y1(x), label=rf"$y_1=\sin{a}x$")
    ax.plot(x, y2(x), label=rf"$y_2=\sin{b}x$")
    ax.plot(x, y3(x), label=r"$y_3=y_1\cdot y_2$", linewidth=3)

    # Plot y4 with special formatting, such as dotted linestyle in order for it to be visible
    # fmt: off
    ax.plot(x, y4(x),
            label=rf"$y_4=\frac{{\cos{np.round(a-b)}x-\cos{a+b}x}}{{2}}$",
            color="grey", linestyle="dotted", marker="o", markerfacecolor = "none")
    # fmt: on

    # Set the title, labels, legend, and grid
    ax.set_title("Angle Product Identity (Werner's Formula)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # Set the major tick locator for the x-axis to a MultipleLocator with base 2/0.2
    # This ensures that the major ticks on the x-axis are placed at intervals of 2/0.2 units
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.legend(loc="upper right", fontsize=16)

    ax.axhline(0, color="black", linestyle="-")
    ax.axvline(0, color="black", linestyle="-")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
