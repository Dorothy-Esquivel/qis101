#!/usr/bin/env python3
"""random_walk_gamma.py"""

# Entirely used Dave's code

from __future__ import annotations  # enables the use of forward references for type

# hints, alllowing type annotations to refer to classes defined later in the code.

import typing  # Provides support for type hints.

# Imports the pyplot module from the Matplotlib library, which provides functions for creating
# and customizing plots.
import matplotlib.pyplot as plt
import numpy as np

# Imports the 'gamma' function from the 'scipy.special' module
from scipy.special import gamma  # type: ignore

# Imports type hints related to the Matplotlib and NumPy libraries
if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def plot(ax: Axes) -> None:
    n: int = 20_000
    # Generates x values
    x: NDArray[np.float_] = np.linspace(1, 25, 100, dtype=np.float_)  # type: ignore

    # Calculates y values using the formula for mean final distance
    y: NDArray[np.float_] = np.sqrt(2 * n / x) * np.power(
        gamma((x + 1.0) / 2) / gamma(x / 2), 2  # type: ignore
    )

    # Plot the data with a linewidth of 2
    ax.plot(x, y, linewidth=2)

    ax.set_title("Mean Final Distance of a\n Uniform Random Walk on a Unit Lattice")
    ax.set_xlabel("Dimensions")
    ax.set_ylabel("Mean Final Distance")


def main() -> None:
    plt.figure(__file__)
    plot(plt.axes())
    plt.show()


if __name__ == "__main__":
    main()
