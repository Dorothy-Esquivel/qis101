#!/usr/bin/env python3
"""plot3d_complex_sine.py"""

# Used Dave's code

from __future__ import annotations

import typing

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

if typing.TYPE_CHECKING:
    from typing import Any
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def f(x: NDArray[np.float_], y: NDArray[np.float_]) -> NDArray[np.complex_]:
    """Compute the absolute value of the complex sine function."""
    return np.array(np.abs(np.sin(x + 1j * y)))


def plot(ax: Axes) -> None:
    """Plot the 3D surface using the provided 'Axes' object."""
    # Arrays with values evenly spaced
    x: NDArray[np.float_] = np.linspace(-2.5, 2.5, 100)
    y: NDArray[np.float_] = np.linspace(-1, 1, 100)

    # Creating a meshgrid of 'x' and 'y' arrays to form a grid of coordinates.
    x, y = np.meshgrid(x, y)

    # An array created by calling 'f' function with 'x' and 'y' as arguments.
    z: NDArray[np.complex_] = f(x, y)

    # Plotting a surface on the given 'Axes' object using 'x', 'y', and 'z' arrays.
    surf: Any = ax.plot_surface(  # type:ignore
        x, y, z, cmap="magma", linewidth=0, antialiased=False  # type:ignore
    )

    # Setting the major tick locator and formatter for the z-axis of the 'Axes' object
    ax.zaxis.set_major_locator(LinearLocator(10))  # type: ignore
    ax.zaxis.set_major_formatter("{x:.02f}")  # type: ignore

    # Adding a colorbar to the plot
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=5)  # type: ignore

    # Setting labels for the x, y, and z axes on the given 'Axes' object
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")  # type: ignore

    # Setting the color of the grid to black
    ax.xaxis._axinfo["grid"]["color"] = "black"  # type: ignore
    ax.yaxis._axinfo["grid"]["color"] = "black"  # type: ignore
    ax.zaxis._axinfo["grid"]["color"] = "black"  # type: ignore


def main() -> None:
    plt.figure(__file__, constrained_layout=True)
    plot(plt.axes(projection="3d"))
    plt.show()


if __name__ == "__main__":
    main()
