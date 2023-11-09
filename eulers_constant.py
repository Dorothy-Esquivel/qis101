#!/usr/bin/env python3
"""eulers_constant.py"""

# Used Dave's code

from __future__ import annotations

import typing

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate  # type: ignore
from matplotlib.ticker import MultipleLocator

if typing.TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


def f(x: float) -> float:
    """Define the function to integrate: f(x) = ln(ln(1/x))"""
    return float(np.log(np.log(1 / x)))  # type: ignore


# Calculates and stores the Euler's constant by numerically integrating the function 'f(x) over the interval [0,1].
euler_constant: float = -scipy.integrate.quad(f, 0, 1)[0]  # type: ignore

h: NDArray[np.float_] = np.zeros(50)  # type: ignore
h[2] = 1
for i in range(3, 50):
    # Calculates the harmonic number at index i by adding the reciprocal of (i - 1) to the previous harmonic number.
    h[i] = h[i - 1] + 1 / (i - 1)


def plot(ax: "Axes") -> None:
    """Plot the harmonic numbers and the logarithmic function"""
    # Plot the step function of harmonic numbers
    ax.step(np.arange(50), h, label=r"$\sum_{k=1}^{\lfloor x\rfloor}\frac{1}{k}$")

    # Generate x values for the logarithmic function (excluding 0)
    x: NDArray[np.float_] = np.linspace(0, 50, 500)[1:]

    # Calculate the logarithmic function values using euler_constant and log(x)
    logf: NDArray[np.float_] = euler_constant + np.log(x)  # type: ignore

    # Plot the logarithmic function
    ax.plot(x, logf, label=r"$\gamma+\ln x$")

    # Set the title for the plot
    ax.set_title("Asymptotic Limit of the Harmonic Numbers")

    # Set the labels for x-axis and y-axis
    ax.set_xlabel("x")
    ax.set_ylabel("Harmonic Number")

    # Set the major and minor locators for x-axis and y-axis
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    # Add a legend to the plot
    ax.legend(loc="center right")

    # Set the limits for x-axis and y-axis
    ax.set_xlim(0)
    ax.set_ylim(0, 5)


def main() -> None:
    """Main function to generate the plot"""
    plt.figure(__file__)
    # Create an Axes object for the plot
    ax: Axes = plt.axes()
    # Call the plot function and pass the Axes object
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
