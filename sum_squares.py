#!/usr/bin/env python3
"""sum_squares.py"""


# Dave's code was referenced for the following lines, unless otherwise specifid.
def main() -> int:
    # For lines 6-10, ChatGPT was referenced. These lines undergo a loop that can sum the first 1000 natural numbers squared.
    loop_sums = 0
    for m in range(1001):
        loop_sums += m**2
    return loop_sums


loop_sum = main()

# These lines do the same as stated in line 5, however, the functional equation for Gaussian summation is used.
for n in range(1000, 1001):
    functional_equation: float = ((2 * (n * n * n)) + 3 * (n * n) + n) / 6
    # These print commands allow the above calculations to be displayed with commas in bewteen using
    # ["... ", " {:,}".format(name)]
    print("Loop sum: ", "{:,}".format(loop_sum))
    print("Gaussian Summation:", "{:,}".format(functional_equation))

if __name__ == "__main__":
    main()
