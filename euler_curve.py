#!/usr/bin/env python3
"""euler_curve.py"""

# Used Dave's code

from __future__ import annotations

import typing

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad  # type: ignore

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def x(t: float) -> float:
    """Parametric function for x-corrdinate of the curve."""
    return quad(lambda u: np.cos(u**2), 0, t)[0]  # type: ignore


def y(t: float) -> float:
    """Parametric function for y-coordinate of the curve."""
    return quad(lambda u: np.sin(u**2), 0, t)[0]  # type: ignore


def ds(t: float) -> float:
    """Arc length element of the curve at a given point t."""
    return float(np.sqrt(np.cos(t**2) ** 2 + np.sin(t**2) ** 2))


def plot(ax: Axes) -> None:
    """Plots Euler's curve and calculates its arc length."""
    tf: float = 12.34
    t: NDArray[np.float_] = np.linspace(0, tf, 1000)

    # Vectorize the parametric functions for efficient computation
    vx = np.vectorize(x)
    vy = np.vectorize(y)
    ax.plot(vx(t), vy(t))  # Plot the curve using the x and y parametric functions

    # Calculate the arc length of the curve using intergration
    arc_length: float = quad(ds, 0, tf)[0]  # type: ignore

    ax.set_title((rf"Euler's Curve $(0\leq t<{tf:.2f})$ arc length = {arc_length:.2f}"))
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")

    # Circle center is at the limit of intergral of cos(x**2) as x goes to infinity
    c: float = np.sqrt(np.pi / 2) / 2
    ax.scatter(c, c, color="red")  # Plot a red dot at the circle center


def main() -> None:
    """Main function to generate the plot."""
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
