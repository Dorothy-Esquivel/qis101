#!/usr/bin/env python3
"""plot3d_cylinder.py"""

# Used Dave's code

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes

    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    """A function named 'plot' that takes an 'Axes' object as input and returns None"""
    # An array with values evenly spaced from 0 to pi
    u: NDArray[np.float_] = np.linspace(0, np.pi, 30)  # poloidal angle
    # An array with values evenly spaced from 0 to 2*pi
    v: NDArray[np.float_] = np.linspace(0, 2 * np.pi, 30)  # toroidal angle

    # fmt: off
    # Arrays created by taking the outer product of 'u', 'sin(v)', 'cos(v), and 'v'
    x: NDArray[np.float_] = np.outer(np.ones_like(u), np.sin(v))
    y: NDArray[np.float_] = np.outer(np.ones_like(u), np.cos(v))
    z: NDArray[np.float_] = np.outer(np.cos(u), np.ones_like(v))

    # fmt: on

    # Setting labels x, y, and z axes on the given 'Axes' object
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    # Plot the a solid cylinder with varying colors
    ax.plot_surface(x, y, z, cmap="hsv")  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
