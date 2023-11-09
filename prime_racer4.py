#!/usr/bin/env python3
"""prime_racer4.py"""

# Entirely used Dave's code.

# imports 'sqrt' from 'math' to calculate the square root of a number
from math import sqrt  # type: ignore
import random  # generates random numbers
import time  # measures the execution time of the program


def is_prime(n: int, known_primes: list[int]) -> bool:
    """Returns True/False if the given number is prime"""
    if n % 2 == 0:
        return False
    # Checks if 'n' is prime by iterating over a range of odd numbers from 3 to the square root of 'n'.
    # For each number in the rage, it checks if 'n' is divisible by that number. If 'n' is divisible by any
    # of these numbers, it returns 'False'. If 'n' is not divisible by any of the numbers, it returns 'True'.
    return all(n % factor != 0 for factor in range(3, int(sqrt(int(n))), 2))


def init_primes(max_n: int) -> list[int]:
    """Returns a list of primes less than the given value"""
    # Initializes a list of primes less than a given value 'max_n'. It starts with a known prime '2' and checks
    # odd numbers up to the sqrt of 'max_n' to find additional primes using trial division.
    known_primes: list[int] = [2]
    for n in range(3, int(sqrt(max_n)), 2):
        for factor in known_primes:
            if n % factor == 0:
                break
        else:
            known_primes.append(n)
    return known_primes


def main() -> None:
    random.seed(2016)

    num_samples: int = 10_000
    min_val: int = 100_000
    max_val: int = 1_000_000

    print(
        (
            f"Counting the number of primes in {num_samples:,} random samples\n"
            f"with each sample having a value between {min_val:,} "
            f"and {max_val:,} inclusive . . ."
        )
    )

    # A list comprehension that generates 'num_samples' random int between 'min_val' and 'max_val' using 'random_randint'.
    samples: list[int] = [random.randint(min_val, max_val) for _ in range(num_samples)]

    known_primes: list[int] = init_primes(max_val)

    start_time: float = time.process_time()
    # a list of comprehension that checks each number in 'samples' for primality using the 'is_prime()' function.
    num_primes: int = [is_prime(n, known_primes) for n in samples].count(
        True
    )  # Type: ignore
    elapsed_time: float = time.process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


if __name__ == "__main__":
    main()
