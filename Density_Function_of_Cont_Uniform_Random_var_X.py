import numpy
import sympy


def main():
    variable_dict = grab_variables()
    A = variable_dict['A']
    B = variable_dict['B']
    bottom = variable_dict['bottom_limit']
    top = variable_dict['top_limit']



def grab_variables():
    variable_dict = {
        'A': float(input("Enter the value of A: ")),
        'B': float(input("Enter the value of B: ")),
        'bottom_limit': float(input("Enter the value of the bottom limit: ")),
        'top_limit': float(input('Enter the value of the top limit: '))
    }

    return variable_dict