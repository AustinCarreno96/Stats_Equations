import math
from Probability_Distribution_of_X import factorial_equation as FE

def main_function():
    variable_dict = grab_variables()
    N = variable_dict['N']
    n = variable_dict['n']
    k = variable_dict['k']
    x_list = variable_dict['x']

    h_list = find_hypergeometric_prob(N, n, k, x_list)
    print_statement(h_list, N, n, k, x_list)
def grab_variables():
    variable_dict = {
        'N': int(input("Enter the total number of objects: ")),
        'n': int(input("Enter the number of objects grabbed: ")),
        'k': int(input("Enter the number of faulty objects: ")),
        'x': []
    }

    highest_x = int(input("Enter the most number of objects that will not fire: "))
    for index in range(highest_x + 1):
        variable_dict['x'].append(index)

    return variable_dict


def find_hypergeometric_prob(N, n, k, x_list):
    h = 0
    h_list = []

    for x in x_list:
        first_mult = FE(k, x)
        second_mult = FE((N - k), (n - x))

        numerator = first_mult * second_mult
        denominator = float(FE(N, n))
        h_list.append(round(numerator / denominator, 4))
    return h_list

def print_statement(h_list, N, n, k, x_list):
    for index in range(len(x_list)):
        print("h(" + str(x_list[index]) + "; " + str(N) + ", " + str(n) + ", " + str(k) + ") = " + str(h_list[index]))

    print("The probability that at most " + str(len(x_list) - 1) + " wont fire: " + str(round(sum(h_list), 4)))


main_function()