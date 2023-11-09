#!/usr/bin/env python3
"""herons_method.py"""

# Entirely used Dave's code.

# Imports random to generate a random integer
import random


def heron_sqrt(s):  # type: ignore
    """heron_sqrt is defined to calculate the square root of any number using the Heron's method. 's'is a parameter that is taken as an input to represent the number to be used."""
    x: float = s / 2
    epsilon = 1e-8
    # This while loop continues until x^2 > epsilon with x being update each loop with the Heron's method.
    while x**2 - s > epsilon:
        x = (s / x + x) / 2
    # Simply returns the calculated x when the while loop ends
    return x


def main() -> None:  # type: ignore
    """Generates a random number (s) in between 1 million and 2 million using the random.randint function. Also calls and assigns the heron_sqrt function to r, which is then rounded to 8 decimal places."""
    s: int = random.randint(int(1e6), int(2e6))
    r: float = round(heron_sqrt(s), 8)
    # Simply prints a message using the 's' and 'r' values, with commas in between the value, appropriately.
    print(f"The square root of {s:,} is {r:,}")


if __name__ == "__main__":
    main()
