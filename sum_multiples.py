#!/usr/bin/env python3
"""sum_multiples.py"""


# Dave's code was referenced for the following lines.
def result() -> int:
    total_sum = 0
    # This for loop goes through all numbers less than 1900 finding the ones that are divisible by 7 and 11, then adds them together.
    for natural_numbers in range(1, 1900):
        if natural_numbers % 7 == 0 and natural_numbers % 11 == 0:
            total_sum += natural_numbers
    # This return command returns the last value that was calculated in the previous for loop.
    return total_sum


# This print command displays the calculated result in the previous for loop.
print(
    "The sum of numbers less than 1900 divisble by 7 and 11 are:",
    "{:,}".format(result()),
)

if __name__ == "__main__":
    result()
