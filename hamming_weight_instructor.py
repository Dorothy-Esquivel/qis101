#!usr/bin/env python3
"""hamming_weight_instructor.py"""

# Entirely used Dave's code


def pop_count(n: int) -> int:
    """Calculates the Hamming weight on an integer 'n'."""
    # Keeps track of the number of bits set to 1.
    count_onebits: int = 0
    # This while loop continues until 'n' becomes 0 by adding the least significant bit of 'n' to 'count_onebits'.
    while n > 0:
        count_onebits += n % 2  # Counting the number of 1-bits
        n //= 2  # Right-shifting the number by 1 bit
    return count_onebits


def main() -> None:
    n: int = 95601

    # Calculates the Hamming weight of 'n' using the 'pop_count' function and assigns the result to 'hamming_weight'
    hamming_weight: int = pop_count(n)
    print(f"The Hamming weight of = {n:,} in base 2 is {hamming_weight:,}")

    # Calculates the Hamming weight of 'n' by converting 'n' to its binary representation using 'bin(n)' and then counts the number of occurrences of "1" using the 'count() method.
    hamming_weight = bin(n).count("1")
    print(f"The Hamming weight of = {n:,} in base 2 is {hamming_weight:,}")


if __name__ == "__main__":
    main()
