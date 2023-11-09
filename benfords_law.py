#!/usr/bin/env python3
"""benfords_law.py"""

import random
import matplotlib.pyplot as plt
import numpy as np
from typing import List  # Import the List type from the typing module for type hints

# Referenced Dave's Code and ChaptGPT


def calculate_msd_probability(numbers: List[int]) -> List[float]:
    # Calculate the counts of each most significant digit
    msd_counts = [0] * 10
    for number in numbers:
        msd_counts[int(str(number)[0])] += 1
    # Calculate the probability of each most significant digit
    return [count / len(numbers) for count in msd_counts]


def main() -> None:
    # Generate a list of random numbers
    random_numbers = [random.randint(1, 1000000) ** 100 for _ in range(100000)]
    # Calculate the probability of each most significant digit
    msd_probability = calculate_msd_probability(random_numbers)  # type: ignore
    # Define the digits for the x-axis
    digits = np.arange(1, 10)

    # Create a new figure and axes for the plot
    _, ax = plt.subplots()
    # Plot the bar chart of the probability of each most significant digit
    ax.bar(digits, msd_probability[1:], color="blue", alpha=0.75)  # type: ignore

    # Set the labels and title of the plot
    ax.set(
        xlabel="Most Significant Digit (MSD)",
        ylabel="Probability of MSD",
        title="Benford's Law",
    )
    # Set the x-axis ticks
    ax.set_xticks(digits)

    # Add the probability values as text above each bar
    for i, prob in enumerate(msd_probability[1:], start=1):
        ax.text(i, prob + 0.003, f"{prob:.3f}", ha="center", va="bottom", fontsize=10)

    # Add a horizontal grid with dashed lines
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    # Adjust the layout to prevent labels from being cut off
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
