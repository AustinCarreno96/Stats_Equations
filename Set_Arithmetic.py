
def main_function():
    set_dict = {'sample_space': set(input('What is the sample space: ').split()),
                'A': set(input('What is the event A: ').split()),
                'A`': set({}),
                'B': set(input('What is the event B: ').split()),
                'B`': set({}),
                'C': set(input('What is the event C: ').split()),
                'C`': set({}),
                }
    find_complement(set_dict)
    find_unions(set_dict)
    find_intersections(set_dict)
    needed_to_print = input("What do you need to find (A_U_B or A_n_B): ").split()


def find_complement(set_dict):
    for element in set_dict['sample_space']:
        if element not in set_dict['A']:
            set_dict['A`'].add(element)
        if element not in set_dict['B']:
            set_dict['B`'].add(element)
        if element not in set_dict['C']:
            set_dict['C`'].add(element)


def find_unions(set_dict):
    set_dict['A_U_B'] = set_dict['A'].union(set_dict['B'])
    set_dict['A`_U_B'] = set_dict['A`'].union(set_dict['B'])
    set_dict['A`_U_Β`'] = set_dict['A`'].union(set_dict['B`'])
    set_dict['A_U_Β`'] = set_dict['A'].union(set_dict['B`'])

    set_dict['A_U_C'] = set_dict['A'].union(set_dict['C'])
    set_dict['A`_U_C'] = set_dict['A`'].union(set_dict['C'])
    set_dict['A_U_C`'] = set_dict['A'].union(set_dict['C`'])
    set_dict['A`_U_C`'] = set_dict['A`'].union(set_dict['C`'])

    set_dict['B_U_C'] = set_dict['B'].union(set_dict['C'])
    set_dict['B`_U_C'] = set_dict['B`'].union(set_dict['C'])
    set_dict['B_U_C`'] = set_dict['B'].union(set_dict['C`'])
    set_dict['B`_U_C`'] = set_dict['B`'].union(set_dict['C`'])


def find_intersections(set_dict):
    set_dict['A_n_B'] = set_dict['A'].intersection(set_dict['B'])
    set_dict['A`_n_B'] = set_dict['A`'].intersection(set_dict['B'])
    set_dict['A`_n_Β`'] = set_dict['A`'].intersection(set_dict['B`'])
    set_dict['A_n_Β`'] = set_dict['A'].intersection(set_dict['B`'])

    set_dict['A_n_C'] = set_dict['A'].intersection(set_dict['C'])
    set_dict['A`_n_C'] = set_dict['A`'].intersection(set_dict['C'])
    set_dict['A_n_C`'] = set_dict['A'].intersection(set_dict['C`'])
    set_dict['A`_n_C`'] = set_dict['A`'].intersection(set_dict['C`'])

    set_dict['B_n_C'] = set_dict['B'].intersection(set_dict['C'])
    set_dict['B`_n_C'] = set_dict['B`'].intersection(set_dict['C'])
    set_dict['B_n_C`'] = set_dict['B'].intersection(set_dict['C`'])
    set_dict['B`_n_C`'] = set_dict['B`'].intersection(set_dict['C`'])