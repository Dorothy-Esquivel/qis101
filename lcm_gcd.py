#!/usr/bin/env python3
"""lcm_gcd.py"""

# Entirely used Dave's code.
"""imports NumPy and assigns it to 'np'."""
import numpy as np


def main() -> None:
    """Simply states the integer numbers to variable name a and b. Then uses those two int to calculate the gcd and lcm."""
    a: int = 447618
    b: int = 2011835

    # Uses gcd (which is in the NumPy library) to calculate the greatest common divisor.
    gcd: int = int(np.gcd(a, b))
    # The variable name lcm calculates the lowest common multiple to the nearest whole number using the equation shown.
    lcm: int = a * b // gcd

    # Simply prints out statements in the output of what a, b, gcd, manual lcm and numpy lcm is
    print(f"a = {a:,}")
    print(f"b = {b:,}")
    print(f"gcd(a,b) = {gcd:,}")
    print(f"manual lcm(a, b) = {lcm:,}")
    # This print command specifically uses NumPy to calculate the lcm, without having to use line 16.
    print(f"numpy lcm (a, b) = {np.lcm(a,b):,}")


if __name__ == "__main__":
    main()
