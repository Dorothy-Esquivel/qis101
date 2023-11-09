#!/usr/bin/env python3
"""celsius_to_fahrenheit.py"""

#Dave's code was referenced for the following
def main() -> None:
    # This for loop analyzes the range of celsius values in between -44 and 104, in steps of 4. Then executes a statement holding an equation to transform celsius values to fahrenheit decimal values.
    for celsius in range(-44, 105, 4):
        fahrenheit: float = (celsius * 9 / 5) + 32
        # This print() command displays each equal values of celsius and fahrenheit with 5 characters wide and 2 decimal points.
        print(f"{celsius:>5.2f} C = {fahrenheit:>5.2f} F")
    # This for loop does the same as stated in line 6 and 8, however only focuses on the celsius value 106.
    for celsius in range(106, 107):
        fahrenheit_s: float = (celsius * 9 / 5) + 32
        print(f"{celsius:>5.2f} C = {fahrenheit_s:>5.2f} F")


if __name__ == "__main__":
    main()
    