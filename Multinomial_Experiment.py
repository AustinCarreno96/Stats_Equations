import math
from Basic_Equations import convert_string_to_float as CSTF



def main():
    variable_dict = grab_variables()
    first = first_multiplier(variable_dict['x_list'], variable_dict['n'])
    second = prob_math(variable_dict['prob_list'], variable_dict['x_list'])
    final = first * second
    print(final)

def grab_variables():
    x_list = []
    ratio_list = []
    variable_dict = {
        'x_list': [],
        'prob_list': [],
        'n': 0.0
    }
    prob_list = []

    variable_dict['x_list'] = input("Enter the values of each x: ").split(",")
    variable_dict['x_list'] = CSTF(variable_dict['x_list'])


    ratio_list = input("Enter the ratio: ").split(":")
    ratio_list = CSTF(ratio_list)
    denominator = float(sum((ratio_list)))
    for ratio in ratio_list:
        variable_dict['prob_list'].append(ratio / denominator)

    variable_dict['n'] = float(input("Enter the number of objects: "))


    return variable_dict

def first_multiplier(x_list, n):
    numerator = math.factorial(int(n))
    denominator = 1

    for x in x_list:
        denominator *= math.factorial(int(x))

    return numerator / denominator

def prob_math(prob_list, x_list):
    second_multiplier = 1
    for index in range(len(prob_list)):
        second_multiplier *= prob_list[index] ** x_list[index]

    return second_multiplier


main()