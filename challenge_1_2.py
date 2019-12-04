from read_input import read_input
from challenge_1_1 import fuel_from_mass

mass_list = read_input('input-1-1.txt', to_num=int)


def fuel_for_fuel(fuel_mass):

    if fuel_from_mass(fuel_mass) <= 0:
        return 0
    return fuel_from_mass(fuel_mass) + fuel_for_fuel(fuel_from_mass(fuel_mass))


print(sum(fuel_for_fuel(m) for m in mass_list))
