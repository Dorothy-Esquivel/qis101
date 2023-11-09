#!/usr/bin/env python3
"""maxwell_boltzmann.py"""

# Referenced Dave's Code and ChatGPT

from __future__ import annotations

import typing

import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray

if typing.TYPE_CHECKING:
    from numpy.typing import NDArray


def maxwell_boltzmann_pdf(x: NDArray[np.float_], a: float) -> NDArray[np.float_]:
    """Calculate the PDF of the Maxwell-Boltzmann distribution."""
    return np.array(
        np.sqrt(2 / np.pi) * (x**2) * np.exp(-(x**2) / (2 * a**2)) / a**3
    )


def main() -> None:
    # Define the range of x values
    x = np.linspace(0, 20, 1000)[None, :]

    # Define the parameters for the PDFs
    parameters = [1, 2, 5]

    # Create a new figure and axes for the plot
    _, ax = plt.subplots()

    # Plot the PDFs for different parameters
    for a in parameters:
        pdf = maxwell_boltzmann_pdf(x, a)
        ax.plot(x[0, :], pdf[0, :], label=f"a = {a}")

    # Set the labels and title of the plot
    ax.set(xlabel="x", ylabel="PDF", title="Maxwell-Boltzmann Distribution PDF")

    # Set the plot limits
    ax.set_xlim(0, 20)

    # Add a legend to distinguish the PDFs
    ax.legend()

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
