#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

# Entirely used Dave's code


def main() -> None:
    # Constants for calculations
    rydberg_constant: float = 1.0967757e7
    e_charge: float = 1.602e-19
    e_mass: float = 9.109e-31
    permittivity: float = 8.854e-12
    h_plank: float = 6.626e-34
    speed_light: float = 2.998e8

    # Bohr's formula for ground state energy
    e_0: float = (pow(e_charge, 4) * e_mass) / (
        8 * pow(permittivity, 2) * pow(h_plank, 2)
    )

    # High Energy Series (Pfund and Humphreys)
    for final_orbit in range(5, 7):
        # Prints headers for the table using the '>' symbol that right-aligns the respective values(Transition, Rydberg, and Bohr) within a field of the specified width.
        print(f"{'Transition':>16}{'Rydberg':>11}{'Bohr':>11}")

        # Calculates and prints the transition details for different initial orbits
        for init_orbit in range(final_orbit + 1, final_orbit + 6):
            # Initial energy level
            e_i: float = -e_0 / pow(init_orbit, 2)
            # Final energy level
            e_f: float = -e_0 / pow(final_orbit, 2)
            # Formula for wavelength in nanometers using Rydberg constant
            wave_length_rydberg: float = (
                1
                / (
                    rydberg_constant
                    * (1 / pow(final_orbit, 2) - 1 / pow(init_orbit, 2))
                )
                * 1e9
            )
            # Formula for wavelength in nanometers using Bohr's formula
            wave_length_bohr: float = h_plank * speed_light / (e_i - e_f) * 1e9

            # Prints the transition details
            print(
                (
                    f"\t{init_orbit:>2} -> {final_orbit:>2}"
                    f"{wave_length_rydberg:8.0f} nm"
                    f"{wave_length_bohr:8.0f} nm"
                )
            )
        # Prints an empty line to separate different final orbits
        print()


if __name__ == "__main__":
    main()
