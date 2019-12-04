from read_input import read_input

mass_list = read_input('input-1-1.txt', to_num=int)


def fuel_from_mass(m):
    return m//3 - 2


print(sum(fuel_from_mass(m) for m in mass_list))
