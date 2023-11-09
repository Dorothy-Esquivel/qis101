#!/usr/bin/env python3
"""factor_quadratic.py"""

import numpy as np

# Entirely used Dave's code


def factor_quadratic(h: int, i: int, j: int) -> None:
    """Takes three integers h,i, and j into a quadratic and attempts to factor it."""
    print("Given the quadratic:", end=" ")
    print(f"{h}x^2 + {i}x + {j}")

    # Keeps track if any factors are found using 'False'.
    found_factor: bool = False

    # Using the gcd from NumPy library, the variables g,h,i, and j are assigned new values after they are divided by the gcd.
    g: int = int(np.gcd(h, np.gcd(i, j)))
    h, i, j = h // g, i // g, j // g

    # The following is a nested loop
    # Simply put, the loop finds what values are divisible by the values of the quadratic.
    for a in range(1, h + 1):
        # Put into human words, if h is divisible by a, it assigns c as the quotient of division. This process is repeated in line 27.
        if h % a == 0:
            c: int = h // a
            for b in range(1, j + 1):
                if j % b == 0:
                    d: int = j // b
                    # If the previous lines of the loop was a success then the equation below should hold and the quadratic is then factored.
                    if a * d + b * c == i:
                        print("The factors are:", end=" ")
                        if g > 0:
                            print(f"({g})", end="")
                        print(f"({a}x + {b})({c}x + {d})")
                        # The loop breaks using True if the quadratic is factored.
                        found_factor = True
                        break
            if found_factor:
                break
    # The following line is for prime quadractics.
    if not found_factor:
        print("There are no factors. The quadratic is prime.")


def main() -> None:
    factor_quadratic(115425, 3254121, 379021)


if __name__ == "__main__":
    main()
